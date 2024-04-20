import typing as T
import re
import uuid
from enum import Enum
import edgedb
from pydantic import BaseModel, Field, parse_obj_as
from edge_orm import execute
from edge_orm.node.models import PropertyCardinality, Cardinality


class IntrospectionException(Exception):
    pass


edgedb_to_python_type_mapping = {
    "str": "str",
    "bool": "bool",
    "int16": "int",
    "int32": "int",
    "int64": "int",
    "float32": "float",
    "float64": "float",
    "bigint": "float",
    "decimal": "Decimal",
    "json": "str",
    "uuid": "UUID",
    "bytes": "bytes",
    "datetime": "datetime",
    "duration": "timedelta",
    "local_datetime": "datetime",
    "local_date": "date",
    "local_time": "time",
    "relative_duration": "RelativeDuration",
    "sequence": "int",
}


class ElementType(BaseModel):
    name: str

    @property
    def type_name(self) -> str:
        return self.name.split("::")[-1]


class Base(BaseModel):
    name: str


class Target(BaseModel):
    name: str
    # prob do not need element type
    element_type: ElementType | None = None
    bases: list[Base] | None = None

    @property
    def model_name(self) -> str:
        return self.name.split("::")[-1]


class Annotation(BaseModel):
    name: str
    value: str = Field(..., alias="@value")

    @property
    def not_insertable(self) -> bool:
        return "not_insertable" in self.name and bool(self.value)


class Constraint(BaseModel):
    name: str

    @property
    def is_exclusive(self) -> bool:
        return self.name == "std::exclusive"


class TriggerKind(str, Enum):
    Insert = "Insert"
    Update = "Update"


class Rewrite(BaseModel):
    id: uuid.UUID
    name: str
    kind: TriggerKind
    expr: str


class Ancestor(BaseModel):
    name: str


class Index(BaseModel):
    expr: str

    @property
    def fields(self) -> T.List[str]:
        pattern = r"\.(\w+)"
        return list(re.findall(pattern, self.expr))


class ParamType(str, Enum):
    LINK = "LINK"
    PROPERTY = "PROPERTY"


class Param(BaseModel):
    name: str
    default: T.Optional[str] = None
    cardinality: Cardinality
    required: bool
    target: Target
    readonly: bool

    constraints: T.List[Constraint]
    annotations: T.List[Annotation]

    expr: T.Optional[str] = None

    @property
    def not_insertable(self) -> bool:
        if not self.annotations:
            return False
        for annotation in self.annotations:
            if annotation.not_insertable:
                return True
        return False

    @property
    def is_computed(self) -> bool:
        return bool(self.expr)

    @property
    def is_exclusive(self) -> bool:
        for constraint in self.constraints:
            if constraint.is_exclusive:
                return True
        return False

    def edgedb_core_type(self, enums_path: str = None) -> str:
        if (
            self.target.bases
            and self.target.name.startswith("default::")
            and self.target.bases[0].name != "std::anyenum"
        ):
            target_base_name = self.target.bases[0].name
        else:
            target_base_name = self.target.name
        pattern = r"::(\w+)"
        core_types = re.findall(pattern, target_base_name)
        if len(core_types) != 1:
            raise IntrospectionException(
                f"Problem parsing core types {core_types=} for {self.name=}, {self.dict()=}"
            )
        s = core_types[0]
        if enums_path:
            if target_base_name.startswith("default::") or target_base_name.startswith(
                "array<default::"
            ):
                s = f"{enums_path}.{s}"
        return s

    @property
    def type_str(self) -> str:
        """returns [Person] or T.Optional[Person] or T.List[str] or str"""
        # if it is a property, make MANY a SET. If it is a link, make it a List
        edgedb_type_str = self.target.name
        edgedb_core_type = self.edgedb_core_type(enums_path="enums")

        python_type = (
            edgedb_to_python_type_mapping.get(edgedb_core_type) or edgedb_core_type
        )
        s = python_type
        if edgedb_type_str.startswith("array"):
            s = f"T.List[{s}]"
        elif edgedb_type_str.startswith("tuple"):
            s = f"T.Tuple[{s}]"
        if self.cardinality == Cardinality.Many:
            iterable = "Set" if self.__class__.__name__ == "Property" else "List"
            s = f"T.{iterable}[{s}]"
        if self.required is False:
            s = f"T.Optional[{s}]"
        return s

    def type_str_basemodel(
        self, module_name: str, cardinality: PropertyCardinality
    ) -> str:
        type_str = self.type_str
        if cardinality == PropertyCardinality.MANY:
            module_name = f"T.List[{module_name}]"
        if "[" in type_str:
            type_str = re.sub(r"\[(\w+)\]", f"[{module_name}]", type_str)
        else:
            type_str = module_name
        return type_str


class Link(Param):
    pass


class Property(Param):
    rewrites: T.List[Rewrite]

    @property
    def rewrite_on(self) -> set[TriggerKind]:
        return {r.kind for r in self.rewrites}


class ObjectType(BaseModel):
    name: str
    links: T.List[Link]
    properties: T.List[Property]
    constraints: T.List[Constraint]
    indexes: T.List[Index]

    @property
    def node_name(self) -> str:
        return self.name.split("::")[-1]


def build_object_types_query_str(objects_to_ignore: set[str]) -> str:
    object_types_query_str = """
    with
        module schema
    select ObjectType {
        name,
        abstract,
        links: {
            name,
            default,
            cardinality,
            required,
            expr,
            target: {
                name,
                [is Array].element_type: {
                    name
                }
            },
            constraints: {
                name
            },
            readonly,
            annotations: {
                name,
                @value
            },
        },
        properties: {
            name,
            default,
            cardinality,
            required,
            expr,
            target: {
                name,
                [is Array].element_type: {
                    name
                },
                [is ScalarType].bases: {
                    name
                }
            },
            constraints: {
                name
            },
            readonly,
            annotations: {
                name,
                @value
            },
            rewrites: {
                id,
                name,
                kind,
                expr,
            },
        },
        constraints: {
            name
        },
        indexes: {
            expr
        }
    } filter contains(.name, 'default::') and .name not in schema::Global.name
    """
    if objects_to_ignore:
        inner = [
            f"'{'default::' if '::' not in o else ''}{o}'" for o in objects_to_ignore
        ]
        global_objects_str = f" and .name not in {{ {', '.join(inner)} }}"
        object_types_query_str += global_objects_str
    return object_types_query_str


async def introspect_objects(
    client: edgedb.AsyncIOClient, objects_to_ignore: set[str]
) -> T.List[ObjectType]:
    object_types_raw = await execute.query(
        client=client,
        query_str=build_object_types_query_str(objects_to_ignore=objects_to_ignore),
        only_one=False,
    )
    object_types = parse_obj_as(T.List[ObjectType], object_types_raw)
    return object_types


scalar_types_query_str = """
with module schema
select ScalarType {
    name,
    enum_values,
    abstract,
    annotations: {
        name,
        @value
    },
    constraints: {
        name
    },
    bases: {
        name
    },
    ancestors: {
        name
    }
} filter contains(.name, 'default::') and .name not in schema::Global.name;
"""


class ScalarType(BaseModel):
    name: str
    enum_values: T.List[str] | None = None
    abstract: bool
    annotations: T.List[Annotation]
    constraints: T.List[Constraint]
    bases: T.List[Base]
    ancestors: T.List[Ancestor]

    @property
    def node_name(self) -> str:
        return self.name.split("::")[-1]


async def introspect_scalars(client: edgedb.AsyncIOClient) -> T.List[ScalarType]:
    scalar_types_raw = await execute.query(
        client=client, query_str=scalar_types_query_str, only_one=False
    )
    scalar_types = parse_obj_as(T.List[ScalarType], scalar_types_raw)
    return scalar_types

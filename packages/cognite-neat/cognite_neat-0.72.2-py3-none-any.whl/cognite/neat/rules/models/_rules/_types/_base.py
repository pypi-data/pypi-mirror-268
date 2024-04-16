import re
import sys
from functools import total_ordering
from typing import Any, ClassVar, Literal, cast, overload

from cognite.client.data_classes.data_modeling import ContainerId, DataModelId, PropertyId, ViewId
from pydantic import BaseModel

from cognite.neat.rules.models.rdfpath import (
    SINGLE_PROPERTY_REGEX_COMPILED,
    AllReferences,
    RDFPath,
    SingleProperty,
    TransformationRuleType,
    parse_rule,
)
from cognite.neat.utils.text import to_pascal

if sys.version_info >= (3, 11):
    from enum import StrEnum
    from typing import Self
else:
    from backports.strenum import StrEnum
    from typing_extensions import Self


class EntityTypes(StrEnum):
    subject = "subject"
    predicate = "predicate"
    object = "object"
    class_ = "class"
    parent_class = "parent_class"
    property_ = "property"
    object_property = "ObjectProperty"
    data_property = "DatatypeProperty"
    annotation_property = "AnnotationProperty"
    object_value_type = "object_value_type"
    data_value_type = "data_value_type"  # these are strings, floats, ...
    xsd_value_type = "xsd_value_type"
    dms_value_type = "dms_value_type"
    view = "view"
    view_prop = "view_prop"
    reference_entity = "reference_entity"
    container = "container"
    datamodel = "datamodel"
    undefined = "undefined"


# ALLOWED
ALLOWED_PATTERN = r"[^a-zA-Z0-9-_.]"

# FOR PARSING STRINGS:
PREFIX_REGEX = r"[a-zA-Z]+[a-zA-Z0-9-_.]*[a-zA-Z0-9]+"
SUFFIX_REGEX = r"[a-zA-Z0-9-_.]+[a-zA-Z0-9]|[-_.]*[a-zA-Z0-9]+"
VERSION_REGEX = r"[a-zA-Z0-9]([.a-zA-Z0-9_-]{0,41}[a-zA-Z0-9])?"
PROPERTY_REGEX = r"[a-zA-Z0-9][a-zA-Z0-9_-]*[a-zA-Z0-9]?"
ENTITY_ID_REGEX = rf"{PREFIX_REGEX}:({SUFFIX_REGEX})"
ENTITY_ID_REGEX_COMPILED = re.compile(rf"^(?P<prefix>{PREFIX_REGEX}):(?P<suffix>{SUFFIX_REGEX})$")
VERSIONED_ENTITY_REGEX_COMPILED = re.compile(
    rf"^(?P<prefix>{PREFIX_REGEX}):(?P<suffix>{SUFFIX_REGEX})\(version=(?P<version>{VERSION_REGEX})\)$"
)
PROPERTY_ENTITY_REGEX_COMPILED = re.compile(
    rf"^((?P<prefix>{PREFIX_REGEX}):)?(?P<suffix>{SUFFIX_REGEX})"
    rf"\((version=(?P<version>{VERSION_REGEX}), )?property=(?P<property>{PROPERTY_REGEX})\)$"
)
CLASS_ID_REGEX = rf"(?P<{EntityTypes.class_}>{ENTITY_ID_REGEX})"
CLASS_ID_REGEX_COMPILED = re.compile(rf"^{CLASS_ID_REGEX}$")
PROPERTY_ID_REGEX = rf"\((?P<{EntityTypes.property_}>{ENTITY_ID_REGEX})\)"
VERSION_ID_REGEX = rf"\(version=(?P<version>{VERSION_REGEX})\)"
MORE_THAN_ONE_NONE_ALPHANUMERIC_REGEX = r"([_-]{2,})"
PREFIX_COMPLIANCE_REGEX = r"^([a-zA-Z]+)([a-zA-Z0-9]*[_-]{0,1}[a-zA-Z0-9_-]*)([a-zA-Z0-9]*)$"
DATA_MODEL_ID_COMPLIANCE_REGEX = r"^[a-zA-Z]([a-zA-Z0-9_]{0,253}[a-zA-Z0-9])?$"
CDF_SPACE_COMPLIANCE_REGEX = (
    r"(?!^(space|cdf|dms|pg3|shared|system|node|edge)$)(^[a-zA-Z][a-zA-Z0-9_-]{0,41}[a-zA-Z0-9]?$)"
)
VIEW_ID_COMPLIANCE_REGEX = (
    r"(?!^(Query|Mutation|Subscription|String|Int32|Int64|Int|Float32|Float64|Float|"
    r"Timestamp|JSONObject|Date|Numeric|Boolean|PageInfo|File|Sequence|TimeSeries)$)"
    r"(^[a-zA-Z][a-zA-Z0-9_]{0,253}[a-zA-Z0-9]?$)"
)
DMS_PROPERTY_ID_COMPLIANCE_REGEX = (
    r"(?!^(space|externalId|createdTime|lastUpdatedTime|deletedTime|edge_id|"
    r"node_id|project_id|property_group|seq|tg_table_name|extensions)$)"
    r"(^[a-zA-Z][a-zA-Z0-9_]{0,253}[a-zA-Z0-9]?$)"
)
CLASS_ID_COMPLIANCE_REGEX = r"(?!^(Class|class)$)(^[a-zA-Z][a-zA-Z0-9._-]{0,253}[a-zA-Z0-9]?$)"
PROPERTY_ID_COMPLIANCE_REGEX = r"^(\*)|(?!^(Property|property)$)(^[a-zA-Z][a-zA-Z0-9._-]{0,253}[a-zA-Z0-9]?$)"
VERSION_COMPLIANCE_REGEX = r"^[a-zA-Z0-9]([.a-zA-Z0-9_-]{0,41}[a-zA-Z0-9])?$"


Undefined = type(object())
Unknown = type(object())


# mypy does not like the sentinel value, and it is not possible to ignore only the line with it below.
# so we ignore all errors beyond this point.
# mypy: ignore-errors
@total_ordering
class Entity(BaseModel, arbitrary_types_allowed=True):
    """Entity is a class or property in OWL/RDF sense."""

    type_: ClassVar[EntityTypes] = EntityTypes.undefined
    prefix: str | Undefined = Undefined
    suffix: str | Unknown
    version: str | None = None
    name: str | None = None
    description: str | None = None

    def __lt__(self, other: object) -> bool:
        if type(self) is not type(other) or not isinstance(other, Entity):
            return NotImplemented
        return self.versioned_id < other.versioned_id

    def __eq__(self, other: object) -> bool:
        if type(self) is not type(other) or not isinstance(other, Entity):
            return NotImplemented
        return self.versioned_id == other.versioned_id

    def __hash__(self) -> int:
        return hash(self.versioned_id)

    def as_non_versioned_entity(self) -> Self:
        return self.from_string(f"{self.prefix}:{self.suffix}")

    @property
    def id(self) -> str:
        if self.suffix is Unknown:
            return "#N/A"
        elif self.prefix is Undefined:
            return self.suffix
        else:
            return f"{self.prefix}:{self.suffix}"

    @property
    def versioned_id(self) -> str:
        if self.version is None:
            return self.id
        else:
            return f"{self.id}(version={self.version})"

    @property
    def space(self) -> str:
        """Returns entity space in CDF."""
        return self.prefix

    @property
    def external_id(self) -> str:
        """Returns entity external id in CDF."""
        return self.suffix

    def __repr__(self):
        return self.versioned_id

    def __str__(self):
        return self.versioned_id

    @classmethod
    def from_string(cls, entity_string: str, base_prefix: str | None = None) -> Self:
        if entity_string == "#N/A":
            return cls(prefix=Undefined, suffix=Unknown)
        elif result := VERSIONED_ENTITY_REGEX_COMPILED.match(entity_string):
            return cls(
                prefix=result.group("prefix"),
                suffix=result.group("suffix"),
                version=result.group("version"),
            )
        elif result := ENTITY_ID_REGEX_COMPILED.match(entity_string):
            return cls(prefix=result.group("prefix"), suffix=result.group("suffix"))
        elif base_prefix and re.match(SUFFIX_REGEX, entity_string) and re.match(PREFIX_REGEX, base_prefix):
            return cls(prefix=base_prefix, suffix=entity_string)
        else:
            raise ValueError(f"{cls.__name__} is expected to be prefix:suffix, got {entity_string}")

    @classmethod
    def from_list(cls, entity_strings: list[str], base_prefix: str | None = None) -> list[Self]:
        return [
            cls.from_string(entity_string=entity_string, base_prefix=base_prefix) for entity_string in entity_strings
        ]


class ContainerEntity(Entity):
    type_: ClassVar[EntityTypes] = EntityTypes.container

    @classmethod
    def from_raw(cls, value: Any) -> "ContainerEntity":
        if not value:
            return ContainerEntity(prefix=Undefined, suffix=value)
        elif isinstance(value, ContainerEntity):
            return value

        if ENTITY_ID_REGEX_COMPILED.match(value):
            return ContainerEntity.from_string(entity_string=value)
        else:
            return ContainerEntity(prefix=Undefined, suffix=value)

    @classmethod
    def from_id(cls, container_id: ContainerId) -> "ContainerEntity":
        return ContainerEntity(prefix=container_id.space, suffix=container_id.external_id)

    def as_id(self, default_space: str | None, standardize_casing: bool = True) -> ContainerId:
        if self.space is Undefined and default_space is None:
            raise ValueError("Space is Undefined! Set default_space!")

        external_id = to_pascal(self.external_id) if standardize_casing else self.external_id
        if self.space is Undefined:
            return ContainerId(space=cast(str, default_space), external_id=external_id)
        else:
            return ContainerId(space=self.space, external_id=external_id)


class ViewEntity(Entity):
    type_: ClassVar[EntityTypes] = EntityTypes.view

    @classmethod
    def from_raw(cls, value: Any) -> "ViewEntity":
        if not value:
            return ViewEntity(prefix=Undefined, suffix=value)
        elif isinstance(value, ViewEntity):
            return value

        if ENTITY_ID_REGEX_COMPILED.match(value) or VERSIONED_ENTITY_REGEX_COMPILED.match(value):
            return cls.from_string(entity_string=value)
        else:
            return cls(prefix=Undefined, suffix=value)

    @classmethod
    def from_id(cls, view_id: ViewId) -> Self:
        return cls(prefix=view_id.space, suffix=view_id.external_id, version=view_id.version)

    @overload
    def as_id(
        self,
        allow_none: Literal[False] = False,
        default_space: str | None = None,
        default_version: str | None = None,
        standardize_casing: bool = True,
    ) -> ViewId:
        ...

    @overload
    def as_id(
        self,
        allow_none: Literal[True],
        default_space: str | None = None,
        default_version: str | None = None,
        standardize_casing: bool = True,
    ) -> ViewId | None:
        ...

    def as_id(
        self,
        allow_none: bool = False,
        default_space: str | None = None,
        default_version: str | None = None,
        standardize_casing: bool = True,
    ) -> ViewId | None:
        if self.suffix is Unknown and allow_none:
            return None
        elif self.suffix is Unknown:
            raise ValueError("suffix is Unknown and cannot be converted to ViewId")
        space = default_space if self.space is Undefined else self.space
        version = self.version or default_version

        if space is None or space is Undefined:
            raise ValueError("space is required")
        if version is None:
            raise ValueError("version is required")
        external_id = to_pascal(self.external_id) if standardize_casing else self.external_id
        return ViewId(space=space, external_id=external_id, version=version)


class ViewPropEntity(ViewEntity):
    type_: ClassVar[EntityTypes] = EntityTypes.view_prop
    property_: str | None = None

    @classmethod
    def from_raw(cls, value: Any) -> "ViewPropEntity":
        if not value:
            return ViewPropEntity(prefix=Undefined, suffix=value)
        elif isinstance(value, ViewPropEntity):
            return value
        elif isinstance(value, ViewEntity):
            return cls(prefix=value.prefix, suffix=value.suffix, version=value.version)

        if result := PROPERTY_ENTITY_REGEX_COMPILED.match(value):
            return cls(
                prefix=result.group("prefix") or Undefined,
                suffix=result.group("suffix"),
                version=result.group("version"),
                property_=result.group("property"),
            )
        elif ENTITY_ID_REGEX_COMPILED.match(value) or VERSIONED_ENTITY_REGEX_COMPILED.match(value):
            return cls.from_string(entity_string=value)
        else:
            return cls(prefix=Undefined, suffix=value)

    @classmethod
    def from_prop_id(cls, prop_id: PropertyId) -> "ViewPropEntity":
        return ViewPropEntity(
            prefix=prop_id.source.space,
            suffix=prop_id.source.external_id,
            version=prop_id.source.version,
            property_=prop_id.property,
        )

    def as_prop_id(
        self, default_space: str | None = None, default_version: str | None = None, standardize_casing: bool = True
    ) -> PropertyId:
        if self.property_ is None:
            raise ValueError("property is required to create PropertyId")
        return PropertyId(
            source=self.as_id(False, default_space, default_version, standardize_casing), property=self.property_
        )

    @property
    def versioned_id(self) -> str:
        if self.version is None and self.property_ is None:
            output = self.id
        elif self.version is None:
            output = f"{self.id}(property={self.property_})"
        elif self.property_ is None:
            output = f"{self.id}(version={self.version})"
        else:
            output = f"{self.id}(version={self.version}, property={self.property_})"
        return output


class DataModelEntity(Entity):
    type_: ClassVar[EntityTypes] = EntityTypes.datamodel

    @classmethod
    def from_raw(cls, value: Any) -> "DataModelEntity":
        if not value:
            return DataModelEntity(prefix=Undefined, suffix=value)
        elif isinstance(value, DataModelEntity):
            return value

        if ENTITY_ID_REGEX_COMPILED.match(value) or VERSIONED_ENTITY_REGEX_COMPILED.match(value):
            return DataModelEntity.from_string(entity_string=value)
        else:
            return DataModelEntity(prefix=Undefined, suffix=value)

    @classmethod
    def from_id(cls, data_model_id: DataModelId) -> "DataModelEntity":
        return DataModelEntity(
            prefix=data_model_id.space, suffix=data_model_id.external_id, version=data_model_id.version
        )

    def as_id(self, default_space: str | None = None, default_version: str | None = None) -> DataModelId:
        space = default_space if self.space is Undefined else self.space
        version = self.version or default_version

        if space is None or space is Undefined:
            raise ValueError("space is required")

        return DataModelId(space=space, external_id=self.external_id, version=version)


class ClassEntity(Entity):
    type_: ClassVar[EntityTypes] = EntityTypes.class_

    @classmethod
    def from_raw(cls, value: Any) -> Self:
        if not value:
            return cls(prefix=Undefined, suffix=value)
        elif isinstance(value, cls):
            return value

        if ENTITY_ID_REGEX_COMPILED.match(value) or VERSIONED_ENTITY_REGEX_COMPILED.match(value):
            return cls.from_string(entity_string=value)
        else:
            return cls(prefix=Undefined, suffix=value)

    @classmethod
    def from_view_id(cls, view_id: ViewId) -> Self:
        return cls(prefix=view_id.space, suffix=view_id.external_id, version=view_id.version)

    @property
    def view_id(self) -> ViewId:
        return ViewId(space=self.space, external_id=self.external_id, version=self.version)


class ParentClassEntity(ClassEntity):
    type_: ClassVar[EntityTypes] = EntityTypes.parent_class

    @classmethod
    def from_raw(cls, value: Any) -> Self:
        if isinstance(value, ClassEntity):
            return cls(prefix=value.prefix, suffix=value.suffix, version=value.version)
        return super().from_raw(value)

    def as_class_entity(self) -> ClassEntity:
        return ClassEntity(prefix=self.prefix, suffix=self.suffix, version=self.version)


class ReferenceEntity(ViewPropEntity):
    type_: ClassVar[EntityTypes] = EntityTypes.reference_entity

    @classmethod
    def from_raw(cls, value: Any) -> "ReferenceEntity":
        if not value:
            return ReferenceEntity(prefix=Undefined, suffix=value)
        elif isinstance(value, ReferenceEntity):
            return value
        elif isinstance(value, ViewEntity):
            return cls(prefix=value.prefix, suffix=value.suffix, version=value.version)

        if result := PROPERTY_ENTITY_REGEX_COMPILED.match(value):
            return cls(
                prefix=result.group("prefix") or Undefined,
                suffix=result.group("suffix"),
                version=result.group("version"),
                property_=result.group("property"),
            )
        elif ENTITY_ID_REGEX_COMPILED.match(value) or VERSIONED_ENTITY_REGEX_COMPILED.match(value):
            return cls.from_string(entity_string=value)
        elif result := SINGLE_PROPERTY_REGEX_COMPILED.match(value):
            return cls.from_rdfpath(value)
        else:
            return cls(prefix=Undefined, suffix=value)

    @classmethod
    def from_rdfpath(cls, rdfpath: RDFPath | str) -> "ReferenceEntity":
        if isinstance(rdfpath, str):
            rdfpath = parse_rule(rdfpath, TransformationRuleType.rdfpath)

        if isinstance(rdfpath.traversal, AllReferences):
            return cls(prefix=rdfpath.traversal.class_.prefix, suffix=rdfpath.traversal.class_.suffix)
        elif isinstance(rdfpath.traversal, SingleProperty):
            return cls(
                prefix=rdfpath.traversal.class_.prefix,
                suffix=rdfpath.traversal.class_.suffix,
                property_=rdfpath.traversal.property.suffix,
            )
        else:
            raise ValueError(f"Invalid RDFPath traversal type: {rdfpath.traversal}")

    def as_rdfpath(self, default_prefix: str | None = None) -> RDFPath:
        prefix = self.prefix if self.prefix is not Undefined else default_prefix

        if prefix is None:
            raise ValueError("prefix is required")

        if self.property_:
            return parse_rule(f"{prefix}:{self.suffix}({self.prefix}:{self.property_})", TransformationRuleType.rdfpath)
        else:
            return parse_rule(f"{self.prefix}:{self.suffix}", TransformationRuleType.rdfpath)

    def as_class_entity(self) -> ClassEntity:
        return ClassEntity(prefix=self.prefix, suffix=self.suffix, version=self.version)

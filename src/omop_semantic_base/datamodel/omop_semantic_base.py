# Auto generated from omop_semantic_base.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-02T20:48:35
# Schema: omop_semantic_object
#
# id: https://example.org/omop_semantics
# description: Core structure for OMOP concept identifiers used for complex semantic definitions, such as staging of neoplastic  disease through condition modifiers and their appropriate handling in episodes.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OMOP = CurieNamespace('omop', 'https://athena.ohdsi.org/search-terms/terms/')
DEFAULT_ = OMOP


# Types

# Class references



@dataclass(repr=False)
class OmopSemanticObject(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopSemanticObject"]
    class_class_curie: ClassVar[str] = "omop:OmopSemanticObject"
    class_name: ClassVar[str] = "OmopSemanticObject"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopSemanticObject

    class_uri: str = None
    name: str = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        if not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopGroup(OmopSemanticObject):
    """
    Named group of OMOP concepts defined by their membership in a particular group, such as hierarchy and / or domain.
    Importantly, this is not a static definition and if the vocabularies are updated, the membership of these groups
    may change. This is intended to be used for defining sets of concepts that are used in semantic definitions, such
    as the set of all T stage concepts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopGroup"]
    class_class_curie: ClassVar[str] = "omop:OmopGroup"
    class_name: ClassVar[str] = "OmopGroup"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopGroup

    name: str = None
    class_uri: str = None
    parent_concepts: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        if not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        if not isinstance(self.parent_concepts, list):
            self.parent_concepts = [self.parent_concepts] if self.parent_concepts is not None else []
        self.parent_concepts = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.parent_concepts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopConcept(OmopSemanticObject):
    """
    A single OMOP concept with semantic annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopConcept"]
    class_class_curie: ClassVar[str] = "omop:OmopConcept"
    class_name: ClassVar[str] = "OmopConcept"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopConcept

    name: str = None
    class_uri: str = None
    concept_id: Optional[int] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        if not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        if self.concept_id is not None and not isinstance(self.concept_id, int):
            self.concept_id = int(self.concept_id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopEnum(OmopSemanticObject):
    """
    Enumeration of permissible values for a particular slot. This is intended to be used for defining slots that have
    a fixed set of permissible values, such as the staging axis (T, N, M, Group). This will not update dynamically
    with vocabulary updates, so should be used for concepts that are short lists and not expected to change over time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopEnum"]
    class_class_curie: ClassVar[str] = "omop:OmopEnum"
    class_name: ClassVar[str] = "OmopEnum"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopEnum

    name: str = None
    enum_members: Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]] = None
    class_uri: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enum_members):
            self.MissingRequiredField("enum_members")
        if not isinstance(self.enum_members, list):
            self.enum_members = [self.enum_members] if self.enum_members is not None else []
        self.enum_members = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.enum_members]

        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        if not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopValueSet(OmopSemanticObject):
    """
    A semantic grouping of permissible values for a template slot. Members may be OmopConcepts, OmopGroups, or
    OmopEnums. This represents a registry-level value domain, not a direct OMOP structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopValueSet"]
    class_class_curie: ClassVar[str] = "omop:OmopValueSet"
    class_name: ClassVar[str] = "OmopValueSet"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopValueSet

    name: str = None
    class_uri: str = None
    members: Optional[Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        if not isinstance(self.class_uri, str):
            self.class_uri = str(self.class_uri)

        self._normalize_inlined_as_dict(slot_name="members", slot_type=OmopSemanticObject, key_name="class_uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    Concept that serves as a member of an OmopEnum. This is intended to be used for defining the permissible values of
    an OmopEnum, which is a fixed enumeration of concepts that does not change dynamically with vocabulary updates.
    The concept_id and label slots are used to specify the concept_id and label of the concept that serves as a member
    of the enumeration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["Concept"]
    class_class_curie: ClassVar[str] = "omop:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = OMOP.Concept

    concept_id: Optional[int] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.concept_id is not None and not isinstance(self.concept_id, int):
            self.concept_id = int(self.concept_id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=OMOP.name, name="name", curie=OMOP.curie('name'),
                   model_uri=OMOP.name, domain=None, range=str)

slots.concept_id = Slot(uri=OMOP.concept_id, name="concept_id", curie=OMOP.curie('concept_id'),
                   model_uri=OMOP.concept_id, domain=None, range=Optional[int])

slots.label = Slot(uri=OMOP.label, name="label", curie=OMOP.curie('label'),
                   model_uri=OMOP.label, domain=None, range=Optional[str])

slots.parent_concepts = Slot(uri=OMOP.parent_concepts, name="parent_concepts", curie=OMOP.curie('parent_concepts'),
                   model_uri=OMOP.parent_concepts, domain=None, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.enum_members = Slot(uri=OMOP.enum_members, name="enum_members", curie=OMOP.curie('enum_members'),
                   model_uri=OMOP.enum_members, domain=None, range=Union[Union[dict, Concept], list[Union[dict, Concept]]])

slots.members = Slot(uri=OMOP.members, name="members", curie=OMOP.curie('members'),
                   model_uri=OMOP.members, domain=None, range=Optional[Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]]])

slots.notes = Slot(uri=OMOP.notes, name="notes", curie=OMOP.curie('notes'),
                   model_uri=OMOP.notes, domain=None, range=Optional[str])

slots.class_uri = Slot(uri=OMOP.class_uri, name="class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.class_uri, domain=None, range=str)

slots.OmopGroup_class_uri = Slot(uri=OMOP.class_uri, name="OmopGroup_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopGroup_class_uri, domain=OmopGroup, range=str)

slots.OmopConcept_class_uri = Slot(uri=OMOP.class_uri, name="OmopConcept_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopConcept_class_uri, domain=OmopConcept, range=str)

slots.OmopEnum_class_uri = Slot(uri=OMOP.class_uri, name="OmopEnum_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopEnum_class_uri, domain=OmopEnum, range=str)

slots.OmopValueSet_class_uri = Slot(uri=OMOP.class_uri, name="OmopValueSet_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopValueSet_class_uri, domain=OmopValueSet, range=str)

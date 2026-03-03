# Auto generated from omop_profiles.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-03T11:50:19
# Schema: omop_templates
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
class OmopTemplate(YAMLRoot):
    """
    A compositional semantic template describing how one or more OMOP concepts are represented in OMOP CDM tables
    (e.g. observation, measurement).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopTemplate"]
    class_class_curie: ClassVar[str] = "omop:OmopTemplate"
    class_name: ClassVar[str] = "OmopTemplate"
    class_model_uri: ClassVar[URIRef] = OMOP.OmopTemplate

    name: str = None
    role: str = None
    cdm_profile: str = None
    entity_concept: Optional[Union[dict, "OmopSemanticObject"]] = None
    value_concept: Optional[Union[dict, "OmopSemanticObject"]] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, str):
            self.role = str(self.role)

        if self._is_empty(self.cdm_profile):
            self.MissingRequiredField("cdm_profile")
        if not isinstance(self.cdm_profile, str):
            self.cdm_profile = str(self.cdm_profile)

        if self.entity_concept is not None and not isinstance(self.entity_concept, OmopSemanticObject):
            self.entity_concept = OmopSemanticObject(**as_dict(self.entity_concept))

        if self.value_concept is not None and not isinstance(self.value_concept, OmopSemanticObject):
            self.value_concept = OmopSemanticObject(**as_dict(self.value_concept))

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopSemanticObject(YAMLRoot):
    """
    Abstract base class for OMOP semantic objects. Used to represent concepts, groups of concepts, enumerations of
    concepts, and value sets of concepts in the context of defining complex semantic structures for the OMOP CDM.
    """
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
        self.class_uri = str(self.class_name)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "class_uri"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



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
        self.class_uri = str(self.class_name)

        if not isinstance(self.parent_concepts, list):
            self.parent_concepts = [self.parent_concepts] if self.parent_concepts is not None else []
        self.parent_concepts = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.parent_concepts]

        super().__post_init__(**kwargs)
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        self.class_uri = str(self.class_name)


@dataclass(repr=False)
class OmopConcept(OmopSemanticObject):
    """
    A single labelled OMOP concept for use in higher level semantic annotations
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
        self.class_uri = str(self.class_name)

        if self.concept_id is not None and not isinstance(self.concept_id, int):
            self.concept_id = int(self.concept_id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        self.class_uri = str(self.class_name)


@dataclass(repr=False)
class OmopEnum(OmopSemanticObject):
    """
    Enumeration (static) of permissible values for a particular slot. This is intended to be used for defining slots
    that have a fixed set of permissible values, such as the staging axis (T, N, M, Group). This will not update
    dynamically with vocabulary updates, so should be used for concepts that are short lists and not expected to
    change over time.
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
        self.class_uri = str(self.class_name)

        super().__post_init__(**kwargs)
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        self.class_uri = str(self.class_name)


@dataclass(repr=False)
class OmopValueSet(OmopSemanticObject):
    """
    A semantic grouping of mixed types of permissible values for a template slot. Members may be OmopConcepts,
    OmopGroups, or OmopEnums. This represents a registry-level value domain, not a direct OMOP structure.
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
        self.class_uri = str(self.class_name)

        self._normalize_inlined_as_dict(slot_name="members", slot_type=OmopSemanticObject, key_name="class_uri", keyed=False)

        super().__post_init__(**kwargs)
        if self._is_empty(self.class_uri):
            self.MissingRequiredField("class_uri")
        self.class_uri = str(self.class_name)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    Concept that serves as a member of a semantic object. This is intended to be used for defining the permissible
    values of an OmopSemanticObject, such as the members of an OmopGroup or OmopEnum. The concept_id and label slots
    are used to specify the concept_id and label of the concept that serves as a member of the enumeration.
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


@dataclass(repr=False)
class CDMValueSets(YAMLRoot):
    """
    A collection of value sets used for defining permissible values for template slots in the OMOP CDM. This is
    intended to be used as a registry of value sets that can be referenced in template definitions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMValueSets")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDMValueSets"
    class_model_uri: ClassVar[URIRef] = OMOP.CDMValueSets

    valuesets: Union[Union[dict, "CDMValueSet"], list[Union[dict, "CDMValueSet"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.valuesets):
            self.MissingRequiredField("valuesets")
        self._normalize_inlined_as_dict(slot_name="valuesets", slot_type=CDMValueSet, key_name="valueset_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CDMValueSet(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMValueSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDMValueSet"
    class_model_uri: ClassVar[URIRef] = OMOP.CDMValueSet

    valueset_name: str = None
    valueset_members: Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.valueset_name):
            self.MissingRequiredField("valueset_name")
        if not isinstance(self.valueset_name, str):
            self.valueset_name = str(self.valueset_name)

        if self._is_empty(self.valueset_members):
            self.MissingRequiredField("valueset_members")
        self._normalize_inlined_as_dict(slot_name="valueset_members", slot_type=OmopSemanticObject, key_name="class_uri", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CDMSemanticUnits(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMSemanticUnits")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDMSemanticUnits"
    class_model_uri: ClassVar[URIRef] = OMOP.CDMSemanticUnits

    name: str = None
    named_enumerators: Optional[Union[Union[dict, OmopEnum], list[Union[dict, OmopEnum]]]] = empty_list()
    named_concepts: Optional[Union[Union[dict, OmopConcept], list[Union[dict, OmopConcept]]]] = empty_list()
    named_groups: Optional[Union[Union[dict, OmopGroup], list[Union[dict, OmopGroup]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="named_enumerators", slot_type=OmopEnum, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="named_concepts", slot_type=OmopConcept, key_name="name", keyed=False)

        self._normalize_inlined_as_dict(slot_name="named_groups", slot_type=OmopGroup, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.role = Slot(uri=OMOP.role, name="role", curie=OMOP.curie('role'),
                   model_uri=OMOP.role, domain=None, range=str)

slots.entity_concept = Slot(uri=OMOP.entity_concept, name="entity_concept", curie=OMOP.curie('entity_concept'),
                   model_uri=OMOP.entity_concept, domain=None, range=Optional[Union[dict, OmopSemanticObject]])

slots.value_concept = Slot(uri=OMOP.value_concept, name="value_concept", curie=OMOP.curie('value_concept'),
                   model_uri=OMOP.value_concept, domain=None, range=Optional[Union[dict, OmopSemanticObject]])

slots.cdm_profile = Slot(uri=OMOP.cdm_profile, name="cdm_profile", curie=OMOP.curie('cdm_profile'),
                   model_uri=OMOP.cdm_profile, domain=None, range=str)

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

slots.named_enumerators = Slot(uri="str(uriorcurie)", name="named_enumerators", curie=None,
                   model_uri=OMOP.named_enumerators, domain=None, range=Optional[Union[Union[dict, OmopEnum], list[Union[dict, OmopEnum]]]])

slots.named_concepts = Slot(uri="str(uriorcurie)", name="named_concepts", curie=None,
                   model_uri=OMOP.named_concepts, domain=None, range=Optional[Union[Union[dict, OmopConcept], list[Union[dict, OmopConcept]]]])

slots.named_valuesets = Slot(uri="str(uriorcurie)", name="named_valuesets", curie=None,
                   model_uri=OMOP.named_valuesets, domain=None, range=Optional[Union[Union[dict, OmopValueSet], list[Union[dict, OmopValueSet]]]])

slots.named_groups = Slot(uri="str(uriorcurie)", name="named_groups", curie=None,
                   model_uri=OMOP.named_groups, domain=None, range=Optional[Union[Union[dict, OmopGroup], list[Union[dict, OmopGroup]]]])

slots.valueset_name = Slot(uri="str(uriorcurie)", name="valueset_name", curie=None,
                   model_uri=OMOP.valueset_name, domain=None, range=str)

slots.valueset_members = Slot(uri="str(uriorcurie)", name="valueset_members", curie=None,
                   model_uri=OMOP.valueset_members, domain=None, range=Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]])

slots.valuesets = Slot(uri="str(uriorcurie)", name="valuesets", curie=None,
                   model_uri=OMOP.valuesets, domain=None, range=Union[Union[dict, CDMValueSet], list[Union[dict, CDMValueSet]]])

slots.OmopGroup_class_uri = Slot(uri=OMOP.class_uri, name="OmopGroup_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopGroup_class_uri, domain=OmopGroup, range=str)

slots.OmopConcept_class_uri = Slot(uri=OMOP.class_uri, name="OmopConcept_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopConcept_class_uri, domain=OmopConcept, range=str)

slots.OmopEnum_class_uri = Slot(uri=OMOP.class_uri, name="OmopEnum_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopEnum_class_uri, domain=OmopEnum, range=str)

slots.OmopValueSet_class_uri = Slot(uri=OMOP.class_uri, name="OmopValueSet_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=OMOP.OmopValueSet_class_uri, domain=OmopValueSet, range=str)

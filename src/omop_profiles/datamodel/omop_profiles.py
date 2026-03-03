# Auto generated from omop_profiles.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-03T13:42:50
# Schema: omop_profiles
#
# id: https://athena.ohdsi.org/search-terms/terms/omop_profiles
# description: LinkML schema for defining the set of profiles, or 'shapes' of data that can be  validly populated with clinical endpoints in the OMOP CDM.  This is intended to be used for defining the permissible semantic structures that  can be used to populate the CDM, such as EAV form, or direct concept identifier slots.
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
DEFAULT_ = CurieNamespace('', 'https://athena.ohdsi.org/search-terms/terms/omop_profiles/')


# Types

# Class references



@dataclass(repr=False)
class CDMProfiles(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["omop_profiles/CDMProfiles"]
    class_class_curie: ClassVar[str] = "omop:omop_profiles/CDMProfiles"
    class_name: ClassVar[str] = "CDMProfiles"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/CDMProfiles")

    profiles: Optional[Union[Union[dict, "OmopCdmProfile"], list[Union[dict, "OmopCdmProfile"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="profiles", slot_type=OmopCdmProfile, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OmopCdmProfile(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["omop_profiles/OmopCdmProfile"]
    class_class_curie: ClassVar[str] = "omop:omop_profiles/OmopCdmProfile"
    class_name: ClassVar[str] = "OmopCdmProfile"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopCdmProfile")

    name: str = None
    cdm_table: Union[str, "CdmTable"] = None
    concept_slot: str = None
    value_slot: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.cdm_table):
            self.MissingRequiredField("cdm_table")
        if not isinstance(self.cdm_table, CdmTable):
            self.cdm_table = CdmTable(self.cdm_table)

        if self._is_empty(self.concept_slot):
            self.MissingRequiredField("concept_slot")
        if not isinstance(self.concept_slot, str):
            self.concept_slot = str(self.concept_slot)

        if self.value_slot is not None and not isinstance(self.value_slot, str):
            self.value_slot = str(self.value_slot)

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopSemanticObject")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopGroup")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopConcept")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopEnum")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopValueSet")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/Concept")

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

    class_class_uri: ClassVar[URIRef] = OMOP["omop_named_sets/CDMValueSets"]
    class_class_curie: ClassVar[str] = "omop:omop_named_sets/CDMValueSets"
    class_name: ClassVar[str] = "CDMValueSets"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/CDMValueSets")

    valuesets: Union[Union[dict, "CDMValueSet"], list[Union[dict, "CDMValueSet"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.valuesets):
            self.MissingRequiredField("valuesets")
        self._normalize_inlined_as_dict(slot_name="valuesets", slot_type=CDMValueSet, key_name="valueset_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CDMValueSet(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["omop_named_sets/CDMValueSet"]
    class_class_curie: ClassVar[str] = "omop:omop_named_sets/CDMValueSet"
    class_name: ClassVar[str] = "CDMValueSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/CDMValueSet")

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

    class_class_uri: ClassVar[URIRef] = OMOP["omop_named_sets/CDMSemanticUnits"]
    class_class_curie: ClassVar[str] = "omop:omop_named_sets/CDMSemanticUnits"
    class_name: ClassVar[str] = "CDMSemanticUnits"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/CDMSemanticUnits")

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


@dataclass(repr=False)
class OmopTemplates(YAMLRoot):
    """
    A collection of OMOP semantic templates for defining complex semantic structures in the OMOP CDM. This is intended
    to be used as a registry of templates that can be referenced in template definitions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopTemplates"]
    class_class_curie: ClassVar[str] = "omop:OmopTemplates"
    class_name: ClassVar[str] = "OmopTemplates"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopTemplates")

    templates: Union[Union[dict, "OmopTemplate"], list[Union[dict, "OmopTemplate"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.templates):
            self.MissingRequiredField("templates")
        self._normalize_inlined_as_dict(slot_name="templates", slot_type=OmopTemplate, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


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
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms/omop_profiles/OmopTemplate")

    name: str = None
    role: str = None
    cdm_profile: str = None
    entity_concept: Optional[Union[dict, OmopSemanticObject]] = None
    value_concept: Optional[Union[dict, OmopSemanticObject]] = None
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


# Enumerations
class CdmTable(EnumDefinitionImpl):
    """
    OMOP CDM table to which a semantic template applies
    """
    observation = PermissibleValue(text="observation")
    measurement = PermissibleValue(text="measurement")
    drug_exposure = PermissibleValue(text="drug_exposure")
    procedure_occurrence = PermissibleValue(text="procedure_occurrence")
    condition_occurrence = PermissibleValue(text="condition_occurrence")
    visit_occurrence = PermissibleValue(text="visit_occurrence")
    device_exposure = PermissibleValue(text="device_exposure")
    specimen = PermissibleValue(text="specimen")

    _defn = EnumDefinition(
        name="CdmTable",
        description="OMOP CDM table to which a semantic template applies",
    )

# Slots
class slots:
    pass

slots.profiles = Slot(uri=DEFAULT_.profiles, name="profiles", curie=DEFAULT_.curie('profiles'),
                   model_uri=DEFAULT_.profiles, domain=None, range=Optional[Union[Union[dict, OmopCdmProfile], list[Union[dict, OmopCdmProfile]]]])

slots.cdm_table = Slot(uri=DEFAULT_.cdm_table, name="cdm_table", curie=DEFAULT_.curie('cdm_table'),
                   model_uri=DEFAULT_.cdm_table, domain=None, range=Union[str, "CdmTable"])

slots.concept_slot = Slot(uri=DEFAULT_.concept_slot, name="concept_slot", curie=DEFAULT_.curie('concept_slot'),
                   model_uri=DEFAULT_.concept_slot, domain=None, range=str)

slots.value_slot = Slot(uri=DEFAULT_.value_slot, name="value_slot", curie=DEFAULT_.curie('value_slot'),
                   model_uri=DEFAULT_.value_slot, domain=None, range=Optional[str])

slots.name = Slot(uri=OMOP.name, name="name", curie=OMOP.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=str)

slots.concept_id = Slot(uri=OMOP.concept_id, name="concept_id", curie=OMOP.curie('concept_id'),
                   model_uri=DEFAULT_.concept_id, domain=None, range=Optional[int])

slots.label = Slot(uri=OMOP.label, name="label", curie=OMOP.curie('label'),
                   model_uri=DEFAULT_.label, domain=None, range=Optional[str])

slots.parent_concepts = Slot(uri=OMOP.parent_concepts, name="parent_concepts", curie=OMOP.curie('parent_concepts'),
                   model_uri=DEFAULT_.parent_concepts, domain=None, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.enum_members = Slot(uri=OMOP.enum_members, name="enum_members", curie=OMOP.curie('enum_members'),
                   model_uri=DEFAULT_.enum_members, domain=None, range=Union[Union[dict, Concept], list[Union[dict, Concept]]])

slots.members = Slot(uri=OMOP.members, name="members", curie=OMOP.curie('members'),
                   model_uri=DEFAULT_.members, domain=None, range=Optional[Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]]])

slots.notes = Slot(uri=OMOP.notes, name="notes", curie=OMOP.curie('notes'),
                   model_uri=DEFAULT_.notes, domain=None, range=Optional[str])

slots.class_uri = Slot(uri=OMOP.class_uri, name="class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.class_uri, domain=None, range=str)

slots.named_enumerators = Slot(uri=OMOP['omop_named_sets/named_enumerators'], name="named_enumerators", curie=OMOP.curie('omop_named_sets/named_enumerators'),
                   model_uri=DEFAULT_.named_enumerators, domain=None, range=Optional[Union[Union[dict, OmopEnum], list[Union[dict, OmopEnum]]]])

slots.named_concepts = Slot(uri=OMOP['omop_named_sets/named_concepts'], name="named_concepts", curie=OMOP.curie('omop_named_sets/named_concepts'),
                   model_uri=DEFAULT_.named_concepts, domain=None, range=Optional[Union[Union[dict, OmopConcept], list[Union[dict, OmopConcept]]]])

slots.named_valuesets = Slot(uri=OMOP['omop_named_sets/named_valuesets'], name="named_valuesets", curie=OMOP.curie('omop_named_sets/named_valuesets'),
                   model_uri=DEFAULT_.named_valuesets, domain=None, range=Optional[Union[Union[dict, OmopValueSet], list[Union[dict, OmopValueSet]]]])

slots.named_groups = Slot(uri=OMOP['omop_named_sets/named_groups'], name="named_groups", curie=OMOP.curie('omop_named_sets/named_groups'),
                   model_uri=DEFAULT_.named_groups, domain=None, range=Optional[Union[Union[dict, OmopGroup], list[Union[dict, OmopGroup]]]])

slots.valueset_name = Slot(uri=OMOP['omop_named_sets/valueset_name'], name="valueset_name", curie=OMOP.curie('omop_named_sets/valueset_name'),
                   model_uri=DEFAULT_.valueset_name, domain=None, range=str)

slots.valueset_members = Slot(uri=OMOP['omop_named_sets/valueset_members'], name="valueset_members", curie=OMOP.curie('omop_named_sets/valueset_members'),
                   model_uri=DEFAULT_.valueset_members, domain=None, range=Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]])

slots.valuesets = Slot(uri=OMOP['omop_named_sets/valuesets'], name="valuesets", curie=OMOP.curie('omop_named_sets/valuesets'),
                   model_uri=DEFAULT_.valuesets, domain=None, range=Union[Union[dict, CDMValueSet], list[Union[dict, CDMValueSet]]])

slots.role = Slot(uri=OMOP.role, name="role", curie=OMOP.curie('role'),
                   model_uri=DEFAULT_.role, domain=None, range=str)

slots.entity_concept = Slot(uri=OMOP.entity_concept, name="entity_concept", curie=OMOP.curie('entity_concept'),
                   model_uri=DEFAULT_.entity_concept, domain=None, range=Optional[Union[dict, OmopSemanticObject]])

slots.value_concept = Slot(uri=OMOP.value_concept, name="value_concept", curie=OMOP.curie('value_concept'),
                   model_uri=DEFAULT_.value_concept, domain=None, range=Optional[Union[dict, OmopSemanticObject]])

slots.cdm_profile = Slot(uri=OMOP.cdm_profile, name="cdm_profile", curie=OMOP.curie('cdm_profile'),
                   model_uri=DEFAULT_.cdm_profile, domain=None, range=str)

slots.templates = Slot(uri=OMOP.templates, name="templates", curie=OMOP.curie('templates'),
                   model_uri=DEFAULT_.templates, domain=None, range=Union[Union[dict, OmopTemplate], list[Union[dict, OmopTemplate]]])

slots.OmopGroup_class_uri = Slot(uri=OMOP.class_uri, name="OmopGroup_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopGroup_class_uri, domain=OmopGroup, range=str)

slots.OmopConcept_class_uri = Slot(uri=OMOP.class_uri, name="OmopConcept_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopConcept_class_uri, domain=OmopConcept, range=str)

slots.OmopEnum_class_uri = Slot(uri=OMOP.class_uri, name="OmopEnum_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopEnum_class_uri, domain=OmopEnum, range=str)

slots.OmopValueSet_class_uri = Slot(uri=OMOP.class_uri, name="OmopValueSet_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopValueSet_class_uri, domain=OmopValueSet, range=str)

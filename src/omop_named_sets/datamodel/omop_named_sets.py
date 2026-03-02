# Auto generated from omop_named_sets.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-02T21:44:01
# Schema: omop_named_sets
#
# id: https://example.org/omop_named_sets
# description:
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
DEFAULT_ = CurieNamespace('', 'https://example.org/omop_named_sets/')


# Types

# Class references



@dataclass(repr=False)
class CDMValueSets(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMValueSets")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDMValueSets"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMValueSets")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMValueSet")

    valueset_name: str = None
    valueset_members: Union[Union[dict, "OmopSemanticObject"], list[Union[dict, "OmopSemanticObject"]]] = None

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/CDMSemanticUnits")

    name: str = None
    named_enumerators: Optional[Union[Union[dict, "OmopEnum"], list[Union[dict, "OmopEnum"]]]] = empty_list()
    named_concepts: Optional[Union[Union[dict, "OmopConcept"], list[Union[dict, "OmopConcept"]]]] = empty_list()
    named_groups: Optional[Union[Union[dict, "OmopGroup"], list[Union[dict, "OmopGroup"]]]] = empty_list()

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
class OmopSemanticObject(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopSemanticObject"]
    class_class_curie: ClassVar[str] = "omop:OmopSemanticObject"
    class_name: ClassVar[str] = "OmopSemanticObject"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/OmopSemanticObject")

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
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/OmopGroup")

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
    A single OMOP concept with semantic annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopConcept"]
    class_class_curie: ClassVar[str] = "omop:OmopConcept"
    class_name: ClassVar[str] = "OmopConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/OmopConcept")

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
    Enumeration of permissible values for a particular slot. This is intended to be used for defining slots that have
    a fixed set of permissible values, such as the staging axis (T, N, M, Group). This will not update dynamically
    with vocabulary updates, so should be used for concepts that are short lists and not expected to change over time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopEnum"]
    class_class_curie: ClassVar[str] = "omop:OmopEnum"
    class_name: ClassVar[str] = "OmopEnum"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/OmopEnum")

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
    A semantic grouping of permissible values for a template slot. Members may be OmopConcepts, OmopGroups, or
    OmopEnums. This represents a registry-level value domain, not a direct OMOP structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["OmopValueSet"]
    class_class_curie: ClassVar[str] = "omop:OmopValueSet"
    class_name: ClassVar[str] = "OmopValueSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/OmopValueSet")

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
    Concept that serves as a member of an OmopEnum. This is intended to be used for defining the permissible values of
    an OmopEnum, which is a fixed enumeration of concepts that does not change dynamically with vocabulary updates.
    The concept_id and label slots are used to specify the concept_id and label of the concept that serves as a member
    of the enumeration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["Concept"]
    class_class_curie: ClassVar[str] = "omop:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://example.org/omop_named_sets/Concept")

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

slots.named_enumerators = Slot(uri=DEFAULT_.named_enumerators, name="named_enumerators", curie=DEFAULT_.curie('named_enumerators'),
                   model_uri=DEFAULT_.named_enumerators, domain=None, range=Optional[Union[Union[dict, OmopEnum], list[Union[dict, OmopEnum]]]])

slots.named_concepts = Slot(uri=DEFAULT_.named_concepts, name="named_concepts", curie=DEFAULT_.curie('named_concepts'),
                   model_uri=DEFAULT_.named_concepts, domain=None, range=Optional[Union[Union[dict, OmopConcept], list[Union[dict, OmopConcept]]]])

slots.named_valuesets = Slot(uri=DEFAULT_.named_valuesets, name="named_valuesets", curie=DEFAULT_.curie('named_valuesets'),
                   model_uri=DEFAULT_.named_valuesets, domain=None, range=Optional[Union[Union[dict, OmopValueSet], list[Union[dict, OmopValueSet]]]])

slots.named_groups = Slot(uri=DEFAULT_.named_groups, name="named_groups", curie=DEFAULT_.curie('named_groups'),
                   model_uri=DEFAULT_.named_groups, domain=None, range=Optional[Union[Union[dict, OmopGroup], list[Union[dict, OmopGroup]]]])

slots.valueset_name = Slot(uri=DEFAULT_.valueset_name, name="valueset_name", curie=DEFAULT_.curie('valueset_name'),
                   model_uri=DEFAULT_.valueset_name, domain=None, range=str)

slots.valueset_members = Slot(uri=DEFAULT_.valueset_members, name="valueset_members", curie=DEFAULT_.curie('valueset_members'),
                   model_uri=DEFAULT_.valueset_members, domain=None, range=Union[Union[dict, OmopSemanticObject], list[Union[dict, OmopSemanticObject]]])

slots.valuesets = Slot(uri=DEFAULT_.valuesets, name="valuesets", curie=DEFAULT_.curie('valuesets'),
                   model_uri=DEFAULT_.valuesets, domain=None, range=Union[Union[dict, CDMValueSet], list[Union[dict, CDMValueSet]]])

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

slots.OmopGroup_class_uri = Slot(uri=OMOP.class_uri, name="OmopGroup_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopGroup_class_uri, domain=OmopGroup, range=str)

slots.OmopConcept_class_uri = Slot(uri=OMOP.class_uri, name="OmopConcept_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopConcept_class_uri, domain=OmopConcept, range=str)

slots.OmopEnum_class_uri = Slot(uri=OMOP.class_uri, name="OmopEnum_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopEnum_class_uri, domain=OmopEnum, range=str)

slots.OmopValueSet_class_uri = Slot(uri=OMOP.class_uri, name="OmopValueSet_class_uri", curie=OMOP.curie('class_uri'),
                   model_uri=DEFAULT_.OmopValueSet_class_uri, domain=OmopValueSet, range=str)

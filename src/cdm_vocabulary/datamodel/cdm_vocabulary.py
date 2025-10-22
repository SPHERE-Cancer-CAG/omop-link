# Auto generated from cdm_vocabulary.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-10-23T00:30:56
# Schema: concept
#
# id: https://athena.ohdsi.org/search-terms/terms#concept
# description: Template for OMOP CDM Concept class, which represents a concept record in the OMOP Common Data Model.
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

from linkml_runtime.linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OMOP = CurieNamespace('omop', 'https://athena.ohdsi.org/search-terms/terms#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
DEFAULT_ = CurieNamespace('', 'https://athena.ohdsi.org/search-terms/terms#concept/')


# Types

# Class references
class ConceptConceptId(extended_int):
    pass


class DomainDomainId(extended_str):
    pass


class VocabularyVocabularyId(extended_str):
    pass


class ConceptClassConceptClassId(extended_str):
    pass


class RelationshipRelationshipId(extended_str):
    pass


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    The Standardized Vocabularies contains records, or Concepts, that uniquely identify each fundamental unit of
    meaning used to express clinical information in all domain tables of the CDM. Concepts are derived from
    vocabularies, which represent clinical information across a domain (e.g. conditions, drugs, procedures) through
    the use of codes and associated descriptions. Some Concepts are designated Standard Concepts, meaning these
    Concepts can be used as normative expressions of a clinical entity within the OMOP Common Data Model and
    standardized analytics. Each Standard Concept belongs to one Domain, which defines the location where the Concept
    would be expected to occur within the data tables of the CDM. Concepts can represent broad categories
    ('Cardiovascular disease'), detailed clinical elements ('Myocardial infarction of the anterolateral wall'), or
    modifying characteristics and attributes that define Concepts at various levels of detail (severity of a disease,
    associated morphology, etc.). Records in the Standardized Vocabularies tables are derived from national or
    international vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover various
    aspects of observational data analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["concept/Concept"]
    class_class_curie: ClassVar[str] = "omop:concept/Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms#concept/Concept")

    concept_id: Union[int, ConceptConceptId] = None
    concept_name: str = None
    concept_code: str = None
    domain_id: Union[str, DomainDomainId] = None
    vocabulary_id: Union[str, VocabularyVocabularyId] = None
    concept_class_id: Union[str, ConceptClassConceptClassId] = None
    valid_start_date: Union[str, XSDDate] = None
    valid_end_date: Union[str, XSDDate] = None
    standard_concept: Optional[Union[str, "StandardConcept"]] = None
    invalid_reason: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, ConceptConceptId):
            self.concept_id = ConceptConceptId(self.concept_id)

        if self._is_empty(self.concept_name):
            self.MissingRequiredField("concept_name")
        if not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self._is_empty(self.concept_code):
            self.MissingRequiredField("concept_code")
        if not isinstance(self.concept_code, str):
            self.concept_code = str(self.concept_code)

        if self._is_empty(self.domain_id):
            self.MissingRequiredField("domain_id")
        if not isinstance(self.domain_id, DomainDomainId):
            self.domain_id = DomainDomainId(self.domain_id)

        if self._is_empty(self.vocabulary_id):
            self.MissingRequiredField("vocabulary_id")
        if not isinstance(self.vocabulary_id, VocabularyVocabularyId):
            self.vocabulary_id = VocabularyVocabularyId(self.vocabulary_id)

        if self._is_empty(self.concept_class_id):
            self.MissingRequiredField("concept_class_id")
        if not isinstance(self.concept_class_id, ConceptClassConceptClassId):
            self.concept_class_id = ConceptClassConceptClassId(self.concept_class_id)

        if self._is_empty(self.valid_start_date):
            self.MissingRequiredField("valid_start_date")
        if not isinstance(self.valid_start_date, XSDDate):
            self.valid_start_date = XSDDate(self.valid_start_date)

        if self._is_empty(self.valid_end_date):
            self.MissingRequiredField("valid_end_date")
        if not isinstance(self.valid_end_date, XSDDate):
            self.valid_end_date = XSDDate(self.valid_end_date)

        if self.standard_concept is not None and not isinstance(self.standard_concept, StandardConcept):
            self.standard_concept = StandardConcept(self.standard_concept)

        if self.invalid_reason is not None and not isinstance(self.invalid_reason, str):
            self.invalid_reason = str(self.invalid_reason)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Domain(YAMLRoot):
    """
    The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the Standardized Vocabularies
    can belong. A Domain represents a clinical definition whereby we assign matching Concepts for the standardized
    fields in the CDM tables. For example, the Condition Domain contains Concepts that describe a patient condition,
    and these Concepts can only be used in the condition_concept_id field of the CONDITION_OCCURRENCE and
    CONDITION_ERA tables. This reference table is populated with a single record for each Domain, including a Domain
    ID and a descriptive name for every Domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["concept/Domain"]
    class_class_curie: ClassVar[str] = "omop:concept/Domain"
    class_name: ClassVar[str] = "Domain"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms#concept/Domain")

    domain_id: Union[str, DomainDomainId] = None
    domain_name: str = None
    domain_concept_id: Union[int, ConceptConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.domain_id):
            self.MissingRequiredField("domain_id")
        if not isinstance(self.domain_id, DomainDomainId):
            self.domain_id = DomainDomainId(self.domain_id)

        if self._is_empty(self.domain_name):
            self.MissingRequiredField("domain_name")
        if not isinstance(self.domain_name, str):
            self.domain_name = str(self.domain_name)

        if self._is_empty(self.domain_concept_id):
            self.MissingRequiredField("domain_concept_id")
        if not isinstance(self.domain_concept_id, ConceptConceptId):
            self.domain_concept_id = ConceptConceptId(self.domain_concept_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vocabulary(YAMLRoot):
    """
    The VOCABULARY table includes a list of the Vocabularies integrated from various sources or created de novo in
    OMOP CDM. This reference table contains a single record for each Vocabulary and includes a descriptive name and
    other associated attributes for the Vocabulary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["concept/Vocabulary"]
    class_class_curie: ClassVar[str] = "omop:concept/Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms#concept/Vocabulary")

    vocabulary_id: Union[str, VocabularyVocabularyId] = None
    vocabulary_name: str = None
    vocabulary_reference: str = None
    vocabulary_concept_id: Union[int, ConceptConceptId] = None
    vocabulary_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vocabulary_id):
            self.MissingRequiredField("vocabulary_id")
        if not isinstance(self.vocabulary_id, VocabularyVocabularyId):
            self.vocabulary_id = VocabularyVocabularyId(self.vocabulary_id)

        if self._is_empty(self.vocabulary_name):
            self.MissingRequiredField("vocabulary_name")
        if not isinstance(self.vocabulary_name, str):
            self.vocabulary_name = str(self.vocabulary_name)

        if self._is_empty(self.vocabulary_reference):
            self.MissingRequiredField("vocabulary_reference")
        if not isinstance(self.vocabulary_reference, str):
            self.vocabulary_reference = str(self.vocabulary_reference)

        if self._is_empty(self.vocabulary_concept_id):
            self.MissingRequiredField("vocabulary_concept_id")
        if not isinstance(self.vocabulary_concept_id, ConceptConceptId):
            self.vocabulary_concept_id = ConceptConceptId(self.vocabulary_concept_id)

        if self.vocabulary_version is not None and not isinstance(self.vocabulary_version, str):
            self.vocabulary_version = str(self.vocabulary_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptClass(YAMLRoot):
    """
    The CONCEPT_CLASS table includes semantic categories that reference the source structure of each Vocabulary.
    Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels (e.g. SNOMED) of the
    vocabulary structure. Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the
    Concept Class. This reference table is populated with a single record for each Concept Class, which includes a
    Concept Class ID and a fully specified Concept Class name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["concept/ConceptClass"]
    class_class_curie: ClassVar[str] = "omop:concept/ConceptClass"
    class_name: ClassVar[str] = "ConceptClass"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms#concept/ConceptClass")

    concept_class_id: Union[str, ConceptClassConceptClassId] = None
    concept_class_name: str = None
    concept_class_concept_id: Union[int, ConceptConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_class_id):
            self.MissingRequiredField("concept_class_id")
        if not isinstance(self.concept_class_id, ConceptClassConceptClassId):
            self.concept_class_id = ConceptClassConceptClassId(self.concept_class_id)

        if self._is_empty(self.concept_class_name):
            self.MissingRequiredField("concept_class_name")
        if not isinstance(self.concept_class_name, str):
            self.concept_class_name = str(self.concept_class_name)

        if self._is_empty(self.concept_class_concept_id):
            self.MissingRequiredField("concept_class_concept_id")
        if not isinstance(self.concept_class_concept_id, ConceptConceptId):
            self.concept_class_concept_id = ConceptConceptId(self.concept_class_concept_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    The RELATIONSHIP table provides a reference list of all types of relationships that can be used to associate any
    two Concepts in the CONCEPT_RELATIONSHIP table, the respective reverse relationships, and their hierarchical
    characteristics. Note, that Concepts representing relationships between the clinical facts, used for filling in
    the FACT_RELATIONSHIP table are stored in the CONCEPT table and belong to the Relationship Domain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP["concept/Relationship"]
    class_class_curie: ClassVar[str] = "omop:concept/Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = URIRef("https://athena.ohdsi.org/search-terms/terms#concept/Relationship")

    relationship_id: Union[str, RelationshipRelationshipId] = None
    relationship_name: str = None
    is_hierarchical: int = None
    defines_ancestry: int = None
    reverse_relationship_id: Union[str, RelationshipRelationshipId] = None
    relationship_concept_id: Union[int, ConceptConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relationship_id):
            self.MissingRequiredField("relationship_id")
        if not isinstance(self.relationship_id, RelationshipRelationshipId):
            self.relationship_id = RelationshipRelationshipId(self.relationship_id)

        if self._is_empty(self.relationship_name):
            self.MissingRequiredField("relationship_name")
        if not isinstance(self.relationship_name, str):
            self.relationship_name = str(self.relationship_name)

        if self._is_empty(self.is_hierarchical):
            self.MissingRequiredField("is_hierarchical")
        if not isinstance(self.is_hierarchical, int):
            self.is_hierarchical = int(self.is_hierarchical)

        if self._is_empty(self.defines_ancestry):
            self.MissingRequiredField("defines_ancestry")
        if not isinstance(self.defines_ancestry, int):
            self.defines_ancestry = int(self.defines_ancestry)

        if self._is_empty(self.reverse_relationship_id):
            self.MissingRequiredField("reverse_relationship_id")
        if not isinstance(self.reverse_relationship_id, RelationshipRelationshipId):
            self.reverse_relationship_id = RelationshipRelationshipId(self.reverse_relationship_id)

        if self._is_empty(self.relationship_concept_id):
            self.MissingRequiredField("relationship_concept_id")
        if not isinstance(self.relationship_concept_id, ConceptConceptId):
            self.relationship_concept_id = ConceptConceptId(self.relationship_concept_id)

        super().__post_init__(**kwargs)


# Enumerations
class StandardConcept(EnumDefinitionImpl):

    S = PermissibleValue(
        text="S",
        description="Standard")
    C = PermissibleValue(
        text="C",
        description="Classification")

    _defn = EnumDefinition(
        name="StandardConcept",
    )

class DeletedConcept(EnumDefinitionImpl):

    D = PermissibleValue(
        text="D",
        description="Deleted")
    U = PermissibleValue(
        text="U",
        description="Updated")

    _defn = EnumDefinition(
        name="DeletedConcept",
    )

# Slots
class slots:
    pass

slots.concept__concept_id = Slot(uri=DEFAULT_.concept_id, name="concept__concept_id", curie=DEFAULT_.curie('concept_id'),
                   model_uri=DEFAULT_.concept__concept_id, domain=None, range=URIRef)

slots.concept__concept_name = Slot(uri=DEFAULT_.concept_name, name="concept__concept_name", curie=DEFAULT_.curie('concept_name'),
                   model_uri=DEFAULT_.concept__concept_name, domain=None, range=str)

slots.concept__concept_code = Slot(uri=DEFAULT_.concept_code, name="concept__concept_code", curie=DEFAULT_.curie('concept_code'),
                   model_uri=DEFAULT_.concept__concept_code, domain=None, range=str)

slots.concept__domain_id = Slot(uri=DEFAULT_.domain_id, name="concept__domain_id", curie=DEFAULT_.curie('domain_id'),
                   model_uri=DEFAULT_.concept__domain_id, domain=None, range=Union[str, DomainDomainId])

slots.concept__vocabulary_id = Slot(uri=DEFAULT_.vocabulary_id, name="concept__vocabulary_id", curie=DEFAULT_.curie('vocabulary_id'),
                   model_uri=DEFAULT_.concept__vocabulary_id, domain=None, range=Union[str, VocabularyVocabularyId])

slots.concept__concept_class_id = Slot(uri=DEFAULT_.concept_class_id, name="concept__concept_class_id", curie=DEFAULT_.curie('concept_class_id'),
                   model_uri=DEFAULT_.concept__concept_class_id, domain=None, range=Union[str, ConceptClassConceptClassId])

slots.concept__standard_concept = Slot(uri=DEFAULT_.standard_concept, name="concept__standard_concept", curie=DEFAULT_.curie('standard_concept'),
                   model_uri=DEFAULT_.concept__standard_concept, domain=None, range=Optional[Union[str, "StandardConcept"]])

slots.concept__valid_start_date = Slot(uri=DEFAULT_.valid_start_date, name="concept__valid_start_date", curie=DEFAULT_.curie('valid_start_date'),
                   model_uri=DEFAULT_.concept__valid_start_date, domain=None, range=Union[str, XSDDate])

slots.concept__valid_end_date = Slot(uri=DEFAULT_.valid_end_date, name="concept__valid_end_date", curie=DEFAULT_.curie('valid_end_date'),
                   model_uri=DEFAULT_.concept__valid_end_date, domain=None, range=Union[str, XSDDate])

slots.concept__invalid_reason = Slot(uri=DEFAULT_.invalid_reason, name="concept__invalid_reason", curie=DEFAULT_.curie('invalid_reason'),
                   model_uri=DEFAULT_.concept__invalid_reason, domain=None, range=Optional[str])

slots.domain__domain_id = Slot(uri=DEFAULT_.domain_id, name="domain__domain_id", curie=DEFAULT_.curie('domain_id'),
                   model_uri=DEFAULT_.domain__domain_id, domain=None, range=URIRef)

slots.domain__domain_name = Slot(uri=DEFAULT_.domain_name, name="domain__domain_name", curie=DEFAULT_.curie('domain_name'),
                   model_uri=DEFAULT_.domain__domain_name, domain=None, range=str)

slots.domain__domain_concept_id = Slot(uri=DEFAULT_.domain_concept_id, name="domain__domain_concept_id", curie=DEFAULT_.curie('domain_concept_id'),
                   model_uri=DEFAULT_.domain__domain_concept_id, domain=None, range=Union[int, ConceptConceptId])

slots.vocabulary__vocabulary_id = Slot(uri=DEFAULT_.vocabulary_id, name="vocabulary__vocabulary_id", curie=DEFAULT_.curie('vocabulary_id'),
                   model_uri=DEFAULT_.vocabulary__vocabulary_id, domain=None, range=URIRef)

slots.vocabulary__vocabulary_name = Slot(uri=DEFAULT_.vocabulary_name, name="vocabulary__vocabulary_name", curie=DEFAULT_.curie('vocabulary_name'),
                   model_uri=DEFAULT_.vocabulary__vocabulary_name, domain=None, range=str)

slots.vocabulary__vocabulary_reference = Slot(uri=DEFAULT_.vocabulary_reference, name="vocabulary__vocabulary_reference", curie=DEFAULT_.curie('vocabulary_reference'),
                   model_uri=DEFAULT_.vocabulary__vocabulary_reference, domain=None, range=str)

slots.vocabulary__vocabulary_version = Slot(uri=DEFAULT_.vocabulary_version, name="vocabulary__vocabulary_version", curie=DEFAULT_.curie('vocabulary_version'),
                   model_uri=DEFAULT_.vocabulary__vocabulary_version, domain=None, range=Optional[str])

slots.vocabulary__vocabulary_concept_id = Slot(uri=DEFAULT_.vocabulary_concept_id, name="vocabulary__vocabulary_concept_id", curie=DEFAULT_.curie('vocabulary_concept_id'),
                   model_uri=DEFAULT_.vocabulary__vocabulary_concept_id, domain=None, range=Union[int, ConceptConceptId])

slots.conceptClass__concept_class_id = Slot(uri=DEFAULT_.concept_class_id, name="conceptClass__concept_class_id", curie=DEFAULT_.curie('concept_class_id'),
                   model_uri=DEFAULT_.conceptClass__concept_class_id, domain=None, range=URIRef)

slots.conceptClass__concept_class_name = Slot(uri=DEFAULT_.concept_class_name, name="conceptClass__concept_class_name", curie=DEFAULT_.curie('concept_class_name'),
                   model_uri=DEFAULT_.conceptClass__concept_class_name, domain=None, range=str)

slots.conceptClass__concept_class_concept_id = Slot(uri=DEFAULT_.concept_class_concept_id, name="conceptClass__concept_class_concept_id", curie=DEFAULT_.curie('concept_class_concept_id'),
                   model_uri=DEFAULT_.conceptClass__concept_class_concept_id, domain=None, range=Union[int, ConceptConceptId])

slots.relationship__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="relationship__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.relationship__relationship_id, domain=None, range=URIRef)

slots.relationship__relationship_name = Slot(uri=DEFAULT_.relationship_name, name="relationship__relationship_name", curie=DEFAULT_.curie('relationship_name'),
                   model_uri=DEFAULT_.relationship__relationship_name, domain=None, range=str)

slots.relationship__is_hierarchical = Slot(uri=DEFAULT_.is_hierarchical, name="relationship__is_hierarchical", curie=DEFAULT_.curie('is_hierarchical'),
                   model_uri=DEFAULT_.relationship__is_hierarchical, domain=None, range=int)

slots.relationship__defines_ancestry = Slot(uri=DEFAULT_.defines_ancestry, name="relationship__defines_ancestry", curie=DEFAULT_.curie('defines_ancestry'),
                   model_uri=DEFAULT_.relationship__defines_ancestry, domain=None, range=int)

slots.relationship__reverse_relationship_id = Slot(uri=DEFAULT_.reverse_relationship_id, name="relationship__reverse_relationship_id", curie=DEFAULT_.curie('reverse_relationship_id'),
                   model_uri=DEFAULT_.relationship__reverse_relationship_id, domain=None, range=Union[str, RelationshipRelationshipId])

slots.relationship__relationship_concept_id = Slot(uri=DEFAULT_.relationship_concept_id, name="relationship__relationship_concept_id", curie=DEFAULT_.curie('relationship_concept_id'),
                   model_uri=DEFAULT_.relationship__relationship_concept_id, domain=None, range=Union[int, ConceptConceptId])

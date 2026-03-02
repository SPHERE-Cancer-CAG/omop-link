from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://athena.ohdsi.org/search-terms/terms#concept/',
     'description': 'Template for OMOP CDM Concept class, which represents a '
                    'concept record in the OMOP Common Data Model.',
     'id': 'https://athena.ohdsi.org/search-terms/terms#concept',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'concept',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'omop': {'prefix_prefix': 'omop',
                           'prefix_reference': 'https://athena.ohdsi.org/search-terms/terms#'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'}},
     'source_file': 'src/cdm_vocabulary/schema/cdm_vocabulary.yaml',
     'title': 'OMOP CDM Concept'} )

class StandardConcept(str, Enum):
    S = "S"
    """
    Standard
    """
    C = "C"
    """
    Classification
    """


class DeletedConcept(str, Enum):
    D = "D"
    """
    Deleted
    """
    U = "U"
    """
    Updated
    """



class Concept(ConfiguredBaseModel):
    """
    The Standardized Vocabularies contains records, or Concepts, that uniquely identify each fundamental unit of meaning used to express clinical information in all domain tables of the CDM.  Concepts are derived from vocabularies, which represent clinical information across a domain (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions.  Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative expressions of a clinical entity within the OMOP Common Data Model and standardized analytics.  Each Standard Concept belongs to one Domain, which defines the location where the Concept would be expected to occur within the data tables of the CDM.  Concepts can represent broad categories ('Cardiovascular disease'), detailed clinical elements ('Myocardial infarction of the anterolateral wall'), or modifying characteristics and attributes that define Concepts at various levels of detail (severity of a disease, associated morphology, etc.).  Records in the Standardized Vocabularies tables are derived from national or international vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover various aspects of observational data analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms#concept'})

    concept_id: int = Field(default=..., description="""Unique identifier for the concept in the OMOP CDM.""", json_schema_extra = { "linkml_meta": {'alias': 'concept_id', 'domain_of': ['Concept']} })
    concept_name: str = Field(default=..., description="""An unambiguous, meaningful and descriptive name for the Concept.""", json_schema_extra = { "linkml_meta": {'alias': 'concept_name', 'domain_of': ['Concept']} })
    concept_code: str = Field(default=..., description="""The concept code represents the identifier of the Concept in the source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies.""", json_schema_extra = { "linkml_meta": {'alias': 'concept_code', 'domain_of': ['Concept']} })
    domain_id: str = Field(default=..., description="""A foreign key to the [DOMAIN](https://ohdsi.github.io/CommonDataModel/cdm54.html#domain) table the Concept belongs to.""", json_schema_extra = { "linkml_meta": {'alias': 'domain_id', 'domain_of': ['Concept', 'Domain']} })
    vocabulary_id: str = Field(default=..., description="""A foreign key to the [VOCABULARY](https://ohdsi.github.io/CommonDataModel/cdm54.html#vocabulary) table indicating from which source the Concept has been adapted.""", json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_id', 'domain_of': ['Concept', 'Vocabulary']} })
    concept_class_id: str = Field(default=..., description="""The attribute or concept class of the Concept. Examples are 'Clinical Drug', 'Ingredient', 'Clinical Finding' etc.""", json_schema_extra = { "linkml_meta": {'alias': 'concept_class_id', 'domain_of': ['Concept', 'ConceptClass']} })
    standard_concept: Optional[StandardConcept] = Field(default=None, description="""This flag determines where a Concept is a Standard Concept, i.e. is used in the data, a Classification Concept, or a non-standard Source Concept. The allowable values are 'S' (Standard Concept) and 'C' (Classification Concept), otherwise the content is NULL.""", json_schema_extra = { "linkml_meta": {'alias': 'standard_concept', 'domain_of': ['Concept']} })
    valid_start_date: date = Field(default=..., description="""The date when the Concept was first recorded. The default value is 1-Jan-1970, meaning, the Concept has no (known) date of inception.""", json_schema_extra = { "linkml_meta": {'alias': 'valid_start_date', 'domain_of': ['Concept']} })
    valid_end_date: date = Field(default=..., description="""The date when the Concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning, the Concept is valid until it becomes deprecated.""", json_schema_extra = { "linkml_meta": {'alias': 'valid_end_date', 'domain_of': ['Concept']} })
    invalid_reason: Optional[str] = Field(default=None, description="""Reason the Concept was invalidated. Possible values are D (deleted), U (replaced with an update) or NULL when valid_end_date has the default value.""", json_schema_extra = { "linkml_meta": {'alias': 'invalid_reason', 'domain_of': ['Concept']} })


class Domain(ConfiguredBaseModel):
    """
    The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the Standardized Vocabularies can belong.  A Domain represents a clinical definition whereby we assign matching Concepts for the standardized fields in the CDM tables.  For example, the Condition Domain contains Concepts that describe a patient condition, and these Concepts can only be used in the condition_concept_id field of the CONDITION_OCCURRENCE and CONDITION_ERA tables.  This reference table is populated with a single record for each Domain, including a Domain ID and a descriptive name for every Domain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms#concept'})

    domain_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'domain_id', 'domain_of': ['Concept', 'Domain']} })
    domain_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'domain_name', 'domain_of': ['Domain']} })
    domain_concept_id: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'domain_concept_id', 'domain_of': ['Domain']} })


class Vocabulary(ConfiguredBaseModel):
    """
    The VOCABULARY table includes a list of the Vocabularies integrated from various sources or created de novo in OMOP CDM.  This reference table contains a single record for each Vocabulary and includes a descriptive name and other associated attributes for the Vocabulary.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms#concept'})

    vocabulary_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_id', 'domain_of': ['Concept', 'Vocabulary']} })
    vocabulary_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_name', 'domain_of': ['Vocabulary']} })
    vocabulary_reference: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_reference', 'domain_of': ['Vocabulary']} })
    vocabulary_version: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_version', 'domain_of': ['Vocabulary']} })
    vocabulary_concept_id: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'vocabulary_concept_id', 'domain_of': ['Vocabulary']} })


class ConceptClass(ConfiguredBaseModel):
    """
    The CONCEPT_CLASS table includes semantic categories that reference the source structure of each Vocabulary.  Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels (e.g. SNOMED) of the vocabulary structure.  Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the Concept Class.  This reference table is populated with a single record for each Concept Class, which includes a Concept Class ID and a fully specified Concept Class name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms#concept'})

    concept_class_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'concept_class_id', 'domain_of': ['Concept', 'ConceptClass']} })
    concept_class_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'concept_class_name', 'domain_of': ['ConceptClass']} })
    concept_class_concept_id: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'concept_class_concept_id', 'domain_of': ['ConceptClass']} })


class Relationship(ConfiguredBaseModel):
    """
    The RELATIONSHIP table provides a reference list of all types of relationships that can be used to associate any two Concepts in the CONCEPT_RELATIONSHIP table, the respective reverse relationships, and their hierarchical characteristics.  Note, that Concepts representing relationships between the clinical facts, used for filling in the FACT_RELATIONSHIP table are stored in the CONCEPT table and belong to the Relationship Domain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms#concept'})

    relationship_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'relationship_id', 'domain_of': ['Relationship']} })
    relationship_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'relationship_name', 'domain_of': ['Relationship']} })
    is_hierarchical: int = Field(default=..., ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'is_hierarchical', 'domain_of': ['Relationship']} })
    defines_ancestry: int = Field(default=..., ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'defines_ancestry', 'domain_of': ['Relationship']} })
    reverse_relationship_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'reverse_relationship_id', 'domain_of': ['Relationship']} })
    relationship_concept_id: int = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'relationship_concept_id', 'domain_of': ['Relationship']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Concept.model_rebuild()
Domain.model_rebuild()
Vocabulary.model_rebuild()
ConceptClass.model_rebuild()
Relationship.model_rebuild()


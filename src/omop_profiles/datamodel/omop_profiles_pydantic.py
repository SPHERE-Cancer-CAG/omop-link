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


linkml_meta = LinkMLMeta({'default_prefix': 'https://athena.ohdsi.org/search-terms/terms/omop_profiles/',
     'description': "LinkML schema for defining the set of profiles, or 'shapes' "
                    'of data that can be  validly populated with clinical '
                    'endpoints in the OMOP CDM.  This is intended to be used for '
                    'defining the permissible semantic structures that  can be '
                    'used to populate the CDM, such as EAV form, or direct concept '
                    'identifier slots. \n',
     'id': 'https://athena.ohdsi.org/search-terms/terms/omop_profiles',
     'imports': ['omop_semantic_base', 'omop_named_sets'],
     'name': 'omop_profiles',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'omop': {'prefix_prefix': 'omop',
                           'prefix_reference': 'https://athena.ohdsi.org/search-terms/terms/'}},
     'source_file': 'src/omop_profiles/schema/omop_profiles.yaml',
     'title': 'OMOP Profiles'} )

class CdmTable(str, Enum):
    """
    OMOP CDM table to which a semantic template applies
    """
    observation = "observation"
    measurement = "measurement"
    drug_exposure = "drug_exposure"
    procedure_occurrence = "procedure_occurrence"
    condition_occurrence = "condition_occurrence"
    visit_occurrence = "visit_occurrence"
    device_exposure = "device_exposure"
    specimen = "specimen"



class OmopSemanticObject(ConfiguredBaseModel):
    """
    Abstract base class for OMOP semantic objects.  Used to represent concepts, groups of concepts, enumerations of concepts, and value sets of concepts in the context of defining complex semantic structures for the OMOP CDM.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base'})

    class_uri: Literal["OmopSemanticObject"] = Field(default="OmopSemanticObject", json_schema_extra = { "linkml_meta": {'alias': 'class_uri',
         'designates_type': True,
         'domain_of': ['OmopSemanticObject']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['OmopSemanticObject']} })


class OmopGroup(OmopSemanticObject):
    """
    Named group of OMOP concepts defined by their membership in a particular group, such  as hierarchy and / or domain. Importantly, this is not a static definition and if the vocabularies are updated, the membership of these groups may change. This is intended to be used for defining sets of concepts that are used in semantic definitions, such as the set of all  T stage concepts.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base',
         'slot_usage': {'class_uri': {'equals_string': 'OmopGroup',
                                      'name': 'class_uri'}}})

    parent_concepts: Optional[list[Concept]] = Field(default=None, description="""Semantic parent concepts or grouping parents.""", json_schema_extra = { "linkml_meta": {'alias': 'parent_concepts', 'domain_of': ['OmopGroup']} })
    class_uri: Literal["OmopGroup"] = Field(default="OmopGroup", json_schema_extra = { "linkml_meta": {'alias': 'class_uri',
         'designates_type': True,
         'domain_of': ['OmopSemanticObject'],
         'equals_string': 'OmopGroup'} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['OmopSemanticObject']} })


class OmopConcept(OmopSemanticObject):
    """
    A single labelled OMOP concept for use in higher level semantic annotations
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base',
         'slot_usage': {'class_uri': {'equals_string': 'OmopConcept',
                                      'name': 'class_uri'}}})

    concept_id: Optional[int] = Field(default=None, description="""OMOP concept_id""", json_schema_extra = { "linkml_meta": {'alias': 'concept_id', 'domain_of': ['OmopConcept', 'Concept']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['OmopConcept', 'Concept']} })
    class_uri: Literal["OmopConcept"] = Field(default="OmopConcept", json_schema_extra = { "linkml_meta": {'alias': 'class_uri',
         'designates_type': True,
         'domain_of': ['OmopSemanticObject'],
         'equals_string': 'OmopConcept'} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['OmopSemanticObject']} })


class OmopEnum(OmopSemanticObject):
    """
    Enumeration (static) of permissible values for a particular slot. This is intended to be used for defining slots that have a fixed set of permissible values, such as the staging axis (T, N, M, Group). This will not update dynamically with vocabulary updates, so should be used for concepts that are  short lists and not expected to change over time.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base',
         'slot_usage': {'class_uri': {'equals_string': 'OmopEnum',
                                      'name': 'class_uri'}}})

    enum_members: list[Concept] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'enum_members', 'domain_of': ['OmopEnum']} })
    class_uri: Literal["OmopEnum"] = Field(default="OmopEnum", json_schema_extra = { "linkml_meta": {'alias': 'class_uri',
         'designates_type': True,
         'domain_of': ['OmopSemanticObject'],
         'equals_string': 'OmopEnum'} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['OmopSemanticObject']} })


class OmopValueSet(OmopSemanticObject):
    """
    A semantic grouping of mixed types of permissible values for a template slot. Members may be OmopConcepts, OmopGroups, or OmopEnums. This represents a registry-level value domain, not a direct OMOP structure.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base',
         'slot_usage': {'class_uri': {'equals_string': 'OmopValueSet',
                                      'name': 'class_uri'}}})

    members: Optional[list[Union[OmopSemanticObject,OmopGroup,OmopConcept,OmopEnum,OmopValueSet]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'members', 'domain_of': ['OmopValueSet']} })
    class_uri: Literal["OmopValueSet"] = Field(default="OmopValueSet", json_schema_extra = { "linkml_meta": {'alias': 'class_uri',
         'designates_type': True,
         'domain_of': ['OmopSemanticObject'],
         'equals_string': 'OmopValueSet'} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    notes: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'notes', 'domain_of': ['OmopSemanticObject']} })


class Concept(ConfiguredBaseModel):
    """
    Concept that serves as a member of a semantic object. This is intended to be used for defining the permissible values of an OmopSemanticObject, such as the members of an OmopGroup or OmopEnum.  The concept_id and label slots are used to specify the concept_id and label of the concept that serves as a  member of the enumeration.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_semantic_base'})

    concept_id: Optional[int] = Field(default=None, description="""OMOP concept_id""", json_schema_extra = { "linkml_meta": {'alias': 'concept_id', 'domain_of': ['OmopConcept', 'Concept']} })
    label: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['OmopConcept', 'Concept']} })


class CDMValueSets(ConfiguredBaseModel):
    """
    A collection of value sets used for defining permissible values for template slots in the OMOP CDM. This is intended to be used as a registry of value sets that can be referenced in template definitions.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_named_sets'})

    valuesets: list[CDMValueSet] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'valuesets', 'domain_of': ['CDMValueSets']} })


class CDMValueSet(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_named_sets'})

    valueset_name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'valueset_name', 'domain_of': ['CDMValueSet']} })
    valueset_members: list[Union[OmopSemanticObject,OmopGroup,OmopConcept,OmopEnum,OmopValueSet]] = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'valueset_members', 'domain_of': ['CDMValueSet']} })


class CDMSemanticUnits(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_named_sets'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    named_enumerators: Optional[list[OmopEnum]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'named_enumerators', 'domain_of': ['CDMSemanticUnits']} })
    named_concepts: Optional[list[OmopConcept]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'named_concepts', 'domain_of': ['CDMSemanticUnits']} })
    named_groups: Optional[list[OmopGroup]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'named_groups', 'domain_of': ['CDMSemanticUnits']} })


class CDMProfiles(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_profiles',
         'tree_root': True})

    profiles: Optional[list[OmopCdmProfile]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'profiles', 'domain_of': ['CDMProfiles']} })


class OmopCdmProfile(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://athena.ohdsi.org/search-terms/terms/omop_profiles'})

    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['OmopSemanticObject', 'CDMSemanticUnits', 'OmopCdmProfile']} })
    cdm_table: CdmTable = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'cdm_table', 'domain_of': ['OmopCdmProfile']} })
    concept_slot: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'concept_slot', 'domain_of': ['OmopCdmProfile']} })
    value_slot: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'value_slot', 'domain_of': ['OmopCdmProfile']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OmopSemanticObject.model_rebuild()
OmopGroup.model_rebuild()
OmopConcept.model_rebuild()
OmopEnum.model_rebuild()
OmopValueSet.model_rebuild()
Concept.model_rebuild()
CDMValueSets.model_rebuild()
CDMValueSet.model_rebuild()
CDMSemanticUnits.model_rebuild()
CDMProfiles.model_rebuild()
OmopCdmProfile.model_rebuild()


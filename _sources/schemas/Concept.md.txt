

# Class: Concept 


_The Standardized Vocabularies contains records, or Concepts, that uniquely identify each fundamental unit of meaning used to express clinical information in all domain tables of the CDM.  Concepts are derived from vocabularies, which represent clinical information across a domain (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions.  Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative expressions of a clinical entity within the OMOP Common Data Model and standardized analytics.  Each Standard Concept belongs to one Domain, which defines the location where the Concept would be expected to occur within the data tables of the CDM.  Concepts can represent broad categories ('Cardiovascular disease'), detailed clinical elements ('Myocardial infarction of the anterolateral wall'), or modifying characteristics and attributes that define Concepts at various levels of detail (severity of a disease, associated morphology, etc.).  Records in the Standardized Vocabularies tables are derived from national or international vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover various aspects of observational data analysis._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/Concept](https://athena.ohdsi.org/search-terms/terms#concept/Concept)





```mermaid
 classDiagram
    class Concept
    click Concept href "../Concept/"
      Concept : concept_class_id
        
          
    
        
        
        Concept --> "1" ConceptClass : concept_class_id
        click ConceptClass href "../ConceptClass/"
    

        
      Concept : concept_code
        
      Concept : concept_id
        
      Concept : concept_name
        
      Concept : domain_id
        
          
    
        
        
        Concept --> "1" Domain : domain_id
        click Domain href "../Domain/"
    

        
      Concept : invalid_reason
        
      Concept : standard_concept
        
          
    
        
        
        Concept --> "0..1" standard_concept : standard_concept
        click standard_concept href "../standard_concept/"
    

        
      Concept : valid_end_date
        
      Concept : valid_start_date
        
      Concept : vocabulary_id
        
          
    
        
        
        Concept --> "1" Vocabulary : vocabulary_id
        click Vocabulary href "../Vocabulary/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concept_id](concept_id.md) | 1 <br/> [Integer](Integer.md) | Unique identifier for the concept in the OMOP CDM | direct |
| [concept_name](concept_name.md) | 1 <br/> [String](String.md) | An unambiguous, meaningful and descriptive name for the Concept | direct |
| [concept_code](concept_code.md) | 1 <br/> [String](String.md) | The concept code represents the identifier of the Concept in the source vocab... | direct |
| [domain_id](domain_id.md) | 1 <br/> [Domain](Domain.md) | A foreign key to the [DOMAIN](https://ohdsi | direct |
| [vocabulary_id](vocabulary_id.md) | 1 <br/> [Vocabulary](Vocabulary.md) | A foreign key to the [VOCABULARY](https://ohdsi | direct |
| [concept_class_id](concept_class_id.md) | 1 <br/> [ConceptClass](ConceptClass.md) | The attribute or concept class of the Concept | direct |
| [standard_concept](standard_concept.md) | 0..1 <br/> [standard_concept](standard_concept.md) | This flag determines where a Concept is a Standard Concept, i | direct |
| [valid_start_date](valid_start_date.md) | 1 <br/> [Date](Date.md) | The date when the Concept was first recorded | direct |
| [valid_end_date](valid_end_date.md) | 1 <br/> [Date](Date.md) | The date when the Concept became invalid because it was deleted or superseded... | direct |
| [invalid_reason](invalid_reason.md) | 0..1 <br/> [String](String.md) | Reason the Concept was invalidated | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Domain](Domain.md) | [domain_concept_id](domain_concept_id.md) | range | [Concept](Concept.md) |
| [Vocabulary](Vocabulary.md) | [vocabulary_concept_id](vocabulary_concept_id.md) | range | [Concept](Concept.md) |
| [ConceptClass](ConceptClass.md) | [concept_class_concept_id](concept_class_concept_id.md) | range | [Concept](Concept.md) |
| [Relationship](Relationship.md) | [relationship_concept_id](relationship_concept_id.md) | range | [Concept](Concept.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/Concept |
| native | https://athena.ohdsi.org/search-terms/terms#concept/Concept |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Concept
description: The Standardized Vocabularies contains records, or Concepts, that uniquely
  identify each fundamental unit of meaning used to express clinical information in
  all domain tables of the CDM.  Concepts are derived from vocabularies, which represent
  clinical information across a domain (e.g. conditions, drugs, procedures) through
  the use of codes and associated descriptions.  Some Concepts are designated Standard
  Concepts, meaning these Concepts can be used as normative expressions of a clinical
  entity within the OMOP Common Data Model and standardized analytics.  Each Standard
  Concept belongs to one Domain, which defines the location where the Concept would
  be expected to occur within the data tables of the CDM.  Concepts can represent
  broad categories ('Cardiovascular disease'), detailed clinical elements ('Myocardial
  infarction of the anterolateral wall'), or modifying characteristics and attributes
  that define Concepts at various levels of detail (severity of a disease, associated
  morphology, etc.).  Records in the Standardized Vocabularies tables are derived
  from national or international vocabularies such as SNOMED-CT, RxNorm, and LOINC,
  or custom OMOP Concepts defined to cover various aspects of observational data analysis.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  concept_id:
    name: concept_id
    description: Unique identifier for the concept in the OMOP CDM.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    identifier: true
    domain_of:
    - Concept
    range: integer
    required: true
  concept_name:
    name: concept_name
    description: An unambiguous, meaningful and descriptive name for the Concept.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: string
    required: true
  concept_code:
    name: concept_code
    description: The concept code represents the identifier of the Concept in the
      source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that
      concept codes are not unique across vocabularies.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: string
    required: true
  domain_id:
    name: domain_id
    description: A foreign key to the [DOMAIN](https://ohdsi.github.io/CommonDataModel/cdm54.html#domain)
      table the Concept belongs to.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    - Domain
    range: Domain
    required: true
  vocabulary_id:
    name: vocabulary_id
    description: A foreign key to the [VOCABULARY](https://ohdsi.github.io/CommonDataModel/cdm54.html#vocabulary)
      table indicating from which source the Concept has been adapted.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    - Vocabulary
    range: Vocabulary
    required: true
  concept_class_id:
    name: concept_class_id
    description: The attribute or concept class of the Concept. Examples are 'Clinical
      Drug', 'Ingredient', 'Clinical Finding' etc.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    - ConceptClass
    range: ConceptClass
    required: true
  standard_concept:
    name: standard_concept
    description: This flag determines where a Concept is a Standard Concept, i.e.
      is used in the data, a Classification Concept, or a non-standard Source Concept.
      The allowable values are 'S' (Standard Concept) and 'C' (Classification Concept),
      otherwise the content is NULL.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: standard_concept
    required: false
  valid_start_date:
    name: valid_start_date
    description: The date when the Concept was first recorded. The default value is
      1-Jan-1970, meaning, the Concept has no (known) date of inception.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: date
    required: true
  valid_end_date:
    name: valid_end_date
    description: The date when the Concept became invalid because it was deleted or
      superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning,
      the Concept is valid until it becomes deprecated.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: date
    required: true
  invalid_reason:
    name: invalid_reason
    description: Reason the Concept was invalidated. Possible values are D (deleted),
      U (replaced with an update) or NULL when valid_end_date has the default value.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Concept
    range: string
    required: false

```
</details>

### Induced

<details>
```yaml
name: Concept
description: The Standardized Vocabularies contains records, or Concepts, that uniquely
  identify each fundamental unit of meaning used to express clinical information in
  all domain tables of the CDM.  Concepts are derived from vocabularies, which represent
  clinical information across a domain (e.g. conditions, drugs, procedures) through
  the use of codes and associated descriptions.  Some Concepts are designated Standard
  Concepts, meaning these Concepts can be used as normative expressions of a clinical
  entity within the OMOP Common Data Model and standardized analytics.  Each Standard
  Concept belongs to one Domain, which defines the location where the Concept would
  be expected to occur within the data tables of the CDM.  Concepts can represent
  broad categories ('Cardiovascular disease'), detailed clinical elements ('Myocardial
  infarction of the anterolateral wall'), or modifying characteristics and attributes
  that define Concepts at various levels of detail (severity of a disease, associated
  morphology, etc.).  Records in the Standardized Vocabularies tables are derived
  from national or international vocabularies such as SNOMED-CT, RxNorm, and LOINC,
  or custom OMOP Concepts defined to cover various aspects of observational data analysis.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  concept_id:
    name: concept_id
    description: Unique identifier for the concept in the OMOP CDM.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    identifier: true
    alias: concept_id
    owner: Concept
    domain_of:
    - Concept
    range: integer
  concept_name:
    name: concept_name
    description: An unambiguous, meaningful and descriptive name for the Concept.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: concept_name
    owner: Concept
    domain_of:
    - Concept
    range: string
    required: true
  concept_code:
    name: concept_code
    description: The concept code represents the identifier of the Concept in the
      source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that
      concept codes are not unique across vocabularies.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: concept_code
    owner: Concept
    domain_of:
    - Concept
    range: string
    required: true
  domain_id:
    name: domain_id
    description: A foreign key to the [DOMAIN](https://ohdsi.github.io/CommonDataModel/cdm54.html#domain)
      table the Concept belongs to.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: domain_id
    owner: Concept
    domain_of:
    - Concept
    - Domain
    range: Domain
    required: true
  vocabulary_id:
    name: vocabulary_id
    description: A foreign key to the [VOCABULARY](https://ohdsi.github.io/CommonDataModel/cdm54.html#vocabulary)
      table indicating from which source the Concept has been adapted.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: vocabulary_id
    owner: Concept
    domain_of:
    - Concept
    - Vocabulary
    range: Vocabulary
    required: true
  concept_class_id:
    name: concept_class_id
    description: The attribute or concept class of the Concept. Examples are 'Clinical
      Drug', 'Ingredient', 'Clinical Finding' etc.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: concept_class_id
    owner: Concept
    domain_of:
    - Concept
    - ConceptClass
    range: ConceptClass
    required: true
  standard_concept:
    name: standard_concept
    description: This flag determines where a Concept is a Standard Concept, i.e.
      is used in the data, a Classification Concept, or a non-standard Source Concept.
      The allowable values are 'S' (Standard Concept) and 'C' (Classification Concept),
      otherwise the content is NULL.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: standard_concept
    owner: Concept
    domain_of:
    - Concept
    range: standard_concept
    required: false
  valid_start_date:
    name: valid_start_date
    description: The date when the Concept was first recorded. The default value is
      1-Jan-1970, meaning, the Concept has no (known) date of inception.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: valid_start_date
    owner: Concept
    domain_of:
    - Concept
    range: date
    required: true
  valid_end_date:
    name: valid_end_date
    description: The date when the Concept became invalid because it was deleted or
      superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning,
      the Concept is valid until it becomes deprecated.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: valid_end_date
    owner: Concept
    domain_of:
    - Concept
    range: date
    required: true
  invalid_reason:
    name: invalid_reason
    description: Reason the Concept was invalidated. Possible values are D (deleted),
      U (replaced with an update) or NULL when valid_end_date has the default value.
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: invalid_reason
    owner: Concept
    domain_of:
    - Concept
    range: string
    required: false

```
</details>
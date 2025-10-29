

# Class: Vocabulary 


_The VOCABULARY table includes a list of the Vocabularies integrated from various sources or created de novo in OMOP CDM.  This reference table contains a single record for each Vocabulary and includes a descriptive name and other associated attributes for the Vocabulary._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/Vocabulary](https://athena.ohdsi.org/search-terms/terms#concept/Vocabulary)





```mermaid
 classDiagram
    class Vocabulary
    click Vocabulary href "../Vocabulary/"
      Vocabulary : vocabulary_concept_id
        
          
    
        
        
        Vocabulary --> "1" Concept : vocabulary_concept_id
        click Concept href "../Concept/"
    

        
      Vocabulary : vocabulary_id
        
      Vocabulary : vocabulary_name
        
      Vocabulary : vocabulary_reference
        
      Vocabulary : vocabulary_version
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [vocabulary_id](vocabulary_id.md) | 1 <br/> [String](String.md) |  | direct |
| [vocabulary_name](vocabulary_name.md) | 1 <br/> [String](String.md) |  | direct |
| [vocabulary_reference](vocabulary_reference.md) | 1 <br/> [String](String.md) |  | direct |
| [vocabulary_version](vocabulary_version.md) | 0..1 <br/> [String](String.md) |  | direct |
| [vocabulary_concept_id](vocabulary_concept_id.md) | 1 <br/> [Concept](Concept.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [vocabulary_id](vocabulary_id.md) | range | [Vocabulary](Vocabulary.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/Vocabulary |
| native | https://athena.ohdsi.org/search-terms/terms#concept/Vocabulary |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Vocabulary
description: The VOCABULARY table includes a list of the Vocabularies integrated from
  various sources or created de novo in OMOP CDM.  This reference table contains a
  single record for each Vocabulary and includes a descriptive name and other associated
  attributes for the Vocabulary.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  vocabulary_id:
    name: vocabulary_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    identifier: true
    domain_of:
    - Concept
    - Vocabulary
    range: string
    required: true
  vocabulary_name:
    name: vocabulary_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Vocabulary
    range: string
    required: true
  vocabulary_reference:
    name: vocabulary_reference
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Vocabulary
    range: string
    required: true
  vocabulary_version:
    name: vocabulary_version
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Vocabulary
    range: string
    required: false
  vocabulary_concept_id:
    name: vocabulary_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Vocabulary
    range: Concept
    required: true

```
</details>

### Induced

<details>
```yaml
name: Vocabulary
description: The VOCABULARY table includes a list of the Vocabularies integrated from
  various sources or created de novo in OMOP CDM.  This reference table contains a
  single record for each Vocabulary and includes a descriptive name and other associated
  attributes for the Vocabulary.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  vocabulary_id:
    name: vocabulary_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    identifier: true
    alias: vocabulary_id
    owner: Vocabulary
    domain_of:
    - Concept
    - Vocabulary
    range: string
    required: true
  vocabulary_name:
    name: vocabulary_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: vocabulary_name
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: string
    required: true
  vocabulary_reference:
    name: vocabulary_reference
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: vocabulary_reference
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: string
    required: true
  vocabulary_version:
    name: vocabulary_version
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: vocabulary_version
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: string
    required: false
  vocabulary_concept_id:
    name: vocabulary_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: vocabulary_concept_id
    owner: Vocabulary
    domain_of:
    - Vocabulary
    range: Concept
    required: true

```
</details>
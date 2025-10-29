

# Class: ConceptClass 


_The CONCEPT_CLASS table includes semantic categories that reference the source structure of each Vocabulary.  Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels (e.g. SNOMED) of the vocabulary structure.  Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the Concept Class.  This reference table is populated with a single record for each Concept Class, which includes a Concept Class ID and a fully specified Concept Class name._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/ConceptClass](https://athena.ohdsi.org/search-terms/terms#concept/ConceptClass)





```mermaid
 classDiagram
    class ConceptClass
    click ConceptClass href "../ConceptClass/"
      ConceptClass : concept_class_concept_id
        
          
    
        
        
        ConceptClass --> "1" Concept : concept_class_concept_id
        click Concept href "../Concept/"
    

        
      ConceptClass : concept_class_id
        
      ConceptClass : concept_class_name
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [concept_class_id](concept_class_id.md) | 1 <br/> [String](String.md) |  | direct |
| [concept_class_name](concept_class_name.md) | 1 <br/> [String](String.md) |  | direct |
| [concept_class_concept_id](concept_class_concept_id.md) | 1 <br/> [Concept](Concept.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [concept_class_id](concept_class_id.md) | range | [ConceptClass](ConceptClass.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/ConceptClass |
| native | https://athena.ohdsi.org/search-terms/terms#concept/ConceptClass |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConceptClass
description: The CONCEPT_CLASS table includes semantic categories that reference the
  source structure of each Vocabulary.  Concept Classes represent so-called horizontal
  (e.g. MedDRA, RxNorm) or vertical levels (e.g. SNOMED) of the vocabulary structure.  Vocabularies
  without any Concept Classes, such as HCPCS, use the vocabulary_id as the Concept
  Class.  This reference table is populated with a single record for each Concept
  Class, which includes a Concept Class ID and a fully specified Concept Class name.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  concept_class_id:
    name: concept_class_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    identifier: true
    domain_of:
    - Concept
    - ConceptClass
    range: string
    required: true
  concept_class_name:
    name: concept_class_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - ConceptClass
    range: string
    required: true
  concept_class_concept_id:
    name: concept_class_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - ConceptClass
    range: Concept
    required: true

```
</details>

### Induced

<details>
```yaml
name: ConceptClass
description: The CONCEPT_CLASS table includes semantic categories that reference the
  source structure of each Vocabulary.  Concept Classes represent so-called horizontal
  (e.g. MedDRA, RxNorm) or vertical levels (e.g. SNOMED) of the vocabulary structure.  Vocabularies
  without any Concept Classes, such as HCPCS, use the vocabulary_id as the Concept
  Class.  This reference table is populated with a single record for each Concept
  Class, which includes a Concept Class ID and a fully specified Concept Class name.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  concept_class_id:
    name: concept_class_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    identifier: true
    alias: concept_class_id
    owner: ConceptClass
    domain_of:
    - Concept
    - ConceptClass
    range: string
    required: true
  concept_class_name:
    name: concept_class_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: concept_class_name
    owner: ConceptClass
    domain_of:
    - ConceptClass
    range: string
    required: true
  concept_class_concept_id:
    name: concept_class_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: concept_class_concept_id
    owner: ConceptClass
    domain_of:
    - ConceptClass
    range: Concept
    required: true

```
</details>
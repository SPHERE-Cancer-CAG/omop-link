

# Class: Relationship 


_The RELATIONSHIP table provides a reference list of all types of relationships that can be used to associate any two Concepts in the CONCEPT_RELATIONSHIP table, the respective reverse relationships, and their hierarchical characteristics.  Note, that Concepts representing relationships between the clinical facts, used for filling in the FACT_RELATIONSHIP table are stored in the CONCEPT table and belong to the Relationship Domain._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/Relationship](https://athena.ohdsi.org/search-terms/terms#concept/Relationship)





```mermaid
 classDiagram
    class Relationship
    click Relationship href "../Relationship/"
      Relationship : defines_ancestry
        
      Relationship : is_hierarchical
        
      Relationship : relationship_concept_id
        
          
    
        
        
        Relationship --> "1" Concept : relationship_concept_id
        click Concept href "../Concept/"
    

        
      Relationship : relationship_id
        
      Relationship : relationship_name
        
      Relationship : reverse_relationship_id
        
          
    
        
        
        Relationship --> "1" Relationship : reverse_relationship_id
        click Relationship href "../Relationship/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [relationship_id](relationship_id.md) | 1 <br/> [String](String.md) |  | direct |
| [relationship_name](relationship_name.md) | 1 <br/> [String](String.md) |  | direct |
| [is_hierarchical](is_hierarchical.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [defines_ancestry](defines_ancestry.md) | 1 <br/> [Integer](Integer.md) |  | direct |
| [reverse_relationship_id](reverse_relationship_id.md) | 1 <br/> [Relationship](Relationship.md) |  | direct |
| [relationship_concept_id](relationship_concept_id.md) | 1 <br/> [Concept](Concept.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Relationship](Relationship.md) | [reverse_relationship_id](reverse_relationship_id.md) | range | [Relationship](Relationship.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/Relationship |
| native | https://athena.ohdsi.org/search-terms/terms#concept/Relationship |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relationship
description: The RELATIONSHIP table provides a reference list of all types of relationships
  that can be used to associate any two Concepts in the CONCEPT_RELATIONSHIP table,
  the respective reverse relationships, and their hierarchical characteristics.  Note,
  that Concepts representing relationships between the clinical facts, used for filling
  in the FACT_RELATIONSHIP table are stored in the CONCEPT table and belong to the
  Relationship Domain.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  relationship_id:
    name: relationship_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    identifier: true
    domain_of:
    - Relationship
    range: string
    required: true
  relationship_name:
    name: relationship_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Relationship
    range: string
    required: true
  is_hierarchical:
    name: is_hierarchical
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Relationship
    range: integer
    required: true
    minimum_value: 0
    maximum_value: 1
  defines_ancestry:
    name: defines_ancestry
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Relationship
    range: integer
    required: true
    minimum_value: 0
    maximum_value: 1
  reverse_relationship_id:
    name: reverse_relationship_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Relationship
    range: Relationship
    required: true
  relationship_concept_id:
    name: relationship_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    domain_of:
    - Relationship
    range: Concept
    required: true

```
</details>

### Induced

<details>
```yaml
name: Relationship
description: The RELATIONSHIP table provides a reference list of all types of relationships
  that can be used to associate any two Concepts in the CONCEPT_RELATIONSHIP table,
  the respective reverse relationships, and their hierarchical characteristics.  Note,
  that Concepts representing relationships between the clinical facts, used for filling
  in the FACT_RELATIONSHIP table are stored in the CONCEPT table and belong to the
  Relationship Domain.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
attributes:
  relationship_id:
    name: relationship_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    identifier: true
    alias: relationship_id
    owner: Relationship
    domain_of:
    - Relationship
    range: string
    required: true
  relationship_name:
    name: relationship_name
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: relationship_name
    owner: Relationship
    domain_of:
    - Relationship
    range: string
    required: true
  is_hierarchical:
    name: is_hierarchical
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: is_hierarchical
    owner: Relationship
    domain_of:
    - Relationship
    range: integer
    required: true
    minimum_value: 0
    maximum_value: 1
  defines_ancestry:
    name: defines_ancestry
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: defines_ancestry
    owner: Relationship
    domain_of:
    - Relationship
    range: integer
    required: true
    minimum_value: 0
    maximum_value: 1
  reverse_relationship_id:
    name: reverse_relationship_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: reverse_relationship_id
    owner: Relationship
    domain_of:
    - Relationship
    range: Relationship
    required: true
  relationship_concept_id:
    name: relationship_concept_id
    from_schema: https://athena.ohdsi.org/search-terms/terms#concept
    rank: 1000
    alias: relationship_concept_id
    owner: Relationship
    domain_of:
    - Relationship
    range: Concept
    required: true

```
</details>
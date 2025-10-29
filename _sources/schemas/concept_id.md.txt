

# Slot: concept_id 


_Unique identifier for the concept in the OMOP CDM._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/concept_id](https://athena.ohdsi.org/search-terms/terms#concept/concept_id)
Alias: concept_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | The Standardized Vocabularies contains records, or Concepts, that uniquely id... |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/concept_id |
| native | https://athena.ohdsi.org/search-terms/terms#concept/concept_id |




## LinkML Source

<details>
```yaml
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
required: true

```
</details>
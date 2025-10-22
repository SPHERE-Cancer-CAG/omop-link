

# Slot: concept_code 


_The concept code represents the identifier of the Concept in the source vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept codes are not unique across vocabularies._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/concept_code](https://athena.ohdsi.org/search-terms/terms#concept/concept_code)
Alias: concept_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | The Standardized Vocabularies contains records, or Concepts, that uniquely id... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/concept_code |
| native | https://athena.ohdsi.org/search-terms/terms#concept/concept_code |




## LinkML Source

<details>
```yaml
name: concept_code
description: The concept code represents the identifier of the Concept in the source
  vocabulary, such as SNOMED-CT concept IDs, RxNorm RXCUIs etc. Note that concept
  codes are not unique across vocabularies.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
rank: 1000
alias: concept_code
owner: Concept
domain_of:
- Concept
range: string
required: true

```
</details>
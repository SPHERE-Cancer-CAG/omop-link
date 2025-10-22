

# Slot: standard_concept 


_This flag determines where a Concept is a Standard Concept, i.e. is used in the data, a Classification Concept, or a non-standard Source Concept. The allowable values are 'S' (Standard Concept) and 'C' (Classification Concept), otherwise the content is NULL._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/standard_concept](https://athena.ohdsi.org/search-terms/terms#concept/standard_concept)
Alias: standard_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | The Standardized Vocabularies contains records, or Concepts, that uniquely id... |  no  |






## Properties

* Range: [standard_concept](standard_concept.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Concept](Concept.md) | [standard_concept](standard_concept.md) | range | [standard_concept](standard_concept.md) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/standard_concept |
| native | https://athena.ohdsi.org/search-terms/terms#concept/standard_concept |




## LinkML Source

<details>
```yaml
name: standard_concept
description: This flag determines where a Concept is a Standard Concept, i.e. is used
  in the data, a Classification Concept, or a non-standard Source Concept. The allowable
  values are 'S' (Standard Concept) and 'C' (Classification Concept), otherwise the
  content is NULL.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
rank: 1000
alias: standard_concept
owner: Concept
domain_of:
- Concept
range: standard_concept
required: false

```
</details>
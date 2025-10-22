

# Slot: valid_end_date 


_The date when the Concept became invalid because it was deleted or superseded (updated) by a new concept. The default value is 31-Dec-2099, meaning, the Concept is valid until it becomes deprecated._





URI: [https://athena.ohdsi.org/search-terms/terms#concept/valid_end_date](https://athena.ohdsi.org/search-terms/terms#concept/valid_end_date)
Alias: valid_end_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | The Standardized Vocabularies contains records, or Concepts, that uniquely id... |  no  |






## Properties

* Range: [Date](Date.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/valid_end_date |
| native | https://athena.ohdsi.org/search-terms/terms#concept/valid_end_date |




## LinkML Source

<details>
```yaml
name: valid_end_date
description: The date when the Concept became invalid because it was deleted or superseded
  (updated) by a new concept. The default value is 31-Dec-2099, meaning, the Concept
  is valid until it becomes deprecated.
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
rank: 1000
alias: valid_end_date
owner: Concept
domain_of:
- Concept
range: date
required: true

```
</details>


# Slot: domain_name 



URI: [https://athena.ohdsi.org/search-terms/terms#concept/domain_name](https://athena.ohdsi.org/search-terms/terms#concept/domain_name)
Alias: domain_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Domain](Domain.md) | The DOMAIN table includes a list of OMOP-defined Domains to which the Concept... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/domain_name |
| native | https://athena.ohdsi.org/search-terms/terms#concept/domain_name |




## LinkML Source

<details>
```yaml
name: domain_name
from_schema: https://athena.ohdsi.org/search-terms/terms#concept
rank: 1000
alias: domain_name
owner: Domain
domain_of:
- Domain
range: string
required: true

```
</details>


# Slot: is_hierarchical 



URI: [https://athena.ohdsi.org/search-terms/terms#concept/is_hierarchical](https://athena.ohdsi.org/search-terms/terms#concept/is_hierarchical)
Alias: is_hierarchical

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Relationship](Relationship.md) | The RELATIONSHIP table provides a reference list of all types of relationship... |  no  |






## Properties

* Range: [Integer](Integer.md)

* Required: True

* Minimum Value: 0

* Maximum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://athena.ohdsi.org/search-terms/terms#concept




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://athena.ohdsi.org/search-terms/terms#concept/is_hierarchical |
| native | https://athena.ohdsi.org/search-terms/terms#concept/is_hierarchical |




## LinkML Source

<details>
```yaml
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

```
</details>
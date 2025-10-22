# OMOP CDM Concept

Template for OMOP CDM Concept class, which represents a concept record in the OMOP Common Data Model.

URI: https://athena.ohdsi.org/search-terms/terms#concept

Name: concept



## Classes

| Class | Description |
| --- | --- |
| [Concept](Concept.md) | The Standardized Vocabularies contains records, or Concepts, that uniquely id... |
| [ConceptClass](ConceptClass.md) | The CONCEPT_CLASS table includes semantic categories that reference the sourc... |
| [Domain](Domain.md) | The DOMAIN table includes a list of OMOP-defined Domains to which the Concept... |
| [Relationship](Relationship.md) | The RELATIONSHIP table provides a reference list of all types of relationship... |
| [Vocabulary](Vocabulary.md) | The VOCABULARY table includes a list of the Vocabularies integrated from vari... |



## Slots

| Slot | Description |
| --- | --- |
| [concept_class_concept_id](concept_class_concept_id.md) |  |
| [concept_class_id](concept_class_id.md) | The attribute or concept class of the Concept |
| [concept_class_name](concept_class_name.md) |  |
| [concept_code](concept_code.md) | The concept code represents the identifier of the Concept in the source vocab... |
| [concept_id](concept_id.md) | Unique identifier for the concept in the OMOP CDM |
| [concept_name](concept_name.md) | An unambiguous, meaningful and descriptive name for the Concept |
| [defines_ancestry](defines_ancestry.md) |  |
| [domain_concept_id](domain_concept_id.md) |  |
| [domain_id](domain_id.md) | A foreign key to the [DOMAIN](https://ohdsi |
| [domain_name](domain_name.md) |  |
| [invalid_reason](invalid_reason.md) | Reason the Concept was invalidated |
| [is_hierarchical](is_hierarchical.md) |  |
| [relationship_concept_id](relationship_concept_id.md) |  |
| [relationship_id](relationship_id.md) |  |
| [relationship_name](relationship_name.md) |  |
| [reverse_relationship_id](reverse_relationship_id.md) |  |
| [standard_concept](standard_concept.md) | This flag determines where a Concept is a Standard Concept, i |
| [valid_end_date](valid_end_date.md) | The date when the Concept became invalid because it was deleted or superseded... |
| [valid_start_date](valid_start_date.md) | The date when the Concept was first recorded |
| [vocabulary_concept_id](vocabulary_concept_id.md) |  |
| [vocabulary_id](vocabulary_id.md) | A foreign key to the [VOCABULARY](https://ohdsi |
| [vocabulary_name](vocabulary_name.md) |  |
| [vocabulary_reference](vocabulary_reference.md) |  |
| [vocabulary_version](vocabulary_version.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [DeletedConcept](DeletedConcept.md) |  |
| [StandardConcept](StandardConcept.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |

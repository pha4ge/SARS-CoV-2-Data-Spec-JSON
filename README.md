# PHA4GE's SARS-CoV-2 Data Specification Processing Tool

## Motivation
In the face of the current SARS-CoV-2 pandemic, [PHA4GE](https://pha4ge.org/) has identified a clear and present need for a fit-for-purpose, open source SARS-CoV-2 contextual data standard. The specification is implementable via a collection template, as well as an array of protocols and tools to support the harmonisation and submission of sequence data and contextual information to public repositories.
 
The purpose of the PHA4GE SARS-CoV-2 specification is to provide a structure that enables consistent collection and formatting of SARS-CoV-2 metadata in order to structure data consistently across disparate laboratory and epidemiological databases so that they can be harmonised for different uses. It embraces FAIR data stewardship principles and emphasises machine-actionability and consistency of data.

The versioned specification is available from [GitHub](https://github.com/pha4ge/SARS-CoV-2-Contextual-Data-Specification). The PHA4GE's SARS-CoV-2 Data Specification Processing Tool aims to collect the human readable terms and convert them to the machine processable formats in JSON schema language. 


## The Data Specification Processing Tool
The aim of this Tool is to take a simple tabular description of fields and converting it to JSON schema language so that the information is machine processable and therefore possible to be harmonised for different uses. 

### Instalation
The The Data Specification Processing Tool is a simple Python script that automatically converts a tabular to JSON schema language. To install you simply require `python >= 3.7.*` and `git` to clone this repository. 

### Usage
`python table_json.py properties_table.csv > schema.json`

#### Input
Currently, the Data Specification Processing Tool takes as input PHA4GE's ["Spec List (Standardized Terms)" tabular](https://docs.google.com/spreadsheets/d/17PuBcA0cCT-j9hV5tbwMFKtwWwKE-a_MYRqOOsIxj7c/edit?usp=sharing). This table lists the terms for SARS-CoV-2 submission template according to the PHA4GE contextual data collection specification and it's structure is described in Table 1. 

*Table 1*
| Column 	| Description 	|
|:-:	|:-:	|
| Interface Label 	| Column headers in the submission template 	|
| Required/Optional 	| Type of requirement according to PHA4GE's template specification. Limited to the values "Optional", "Recommended" and "Required".  	|
| Definition 	| Short description for the expected interface label value. 	|
| Value Type 	| Expected interface label's value type. Limited to "String", "Int" and "Float". 	|
| Example 	| Example for the expected interface label value. 	|
| Guidance 	| Detailed description for the expected interface label value. 	|

#### Output
Currently, only JSON schema format is being created by this tool. An example is available [here](https://github.com/cimendes/SARS-CoV-2-Data-Spec/blob/master/pha4ge_SARS-CoV-2_metadata_schema.json) for SARS-CoV-2 submission template according to the PHA4GE contextual data collection specification.

## Contacts 
For more information and/or assistance, contact `datastructures@pha4ge.org` or the issue page of this repository. 

# ETL Pipeline for Patient Admissions and Outcomes

## Project Description

This project implements an end-to-end Extract-Transform-Load (ETL) pipeline for processing patient admission and outcome data. The pipeline ingests raw patient admission, lab, and diagnosis data, cleans and transforms it using dbt, and loads it into a clean, ready-to-query PostgreSQL database. Apache Airflow is used to schedule and monitor the workflow.

## Key Features

- Extract data from CSV or JSON files
- Clean and validate patient data
- Normalize ICD-10 codes and lab result units
- Transform raw data into a more queryable format (fact tables, dimensional models)
- Load data into a PostgreSQL database

## Tools and Technologies

- Apache Airflow: For orchestration
- PostgreSQL: For data storage
- dbt: For data transformation
- Docker: For containerization and deployment

## Data Description

The pipeline processes artificial patient data generated according to pre-defined criteria. The database contains characteristics similar to a real medical database, including:

- Patient admission details
- Demographics
- Socioeconomic details
- Lab results
- Medications

The database is customizable, allowing for the generation of populations with specific characteristics (e.g., 100,000 patients, 60% male, 40% African American, 15% diabetic, etc.). The number of records can range from several thousands to millions, depending on the desired configuration.

## Data Tables

1. PatientCorePopulatedTable
2. AdmissionsCorePopulatedTable
3. AdmissionsDiagnosesCorePopulatedTable
4. LabsCorePopulatedTable

For detailed information on the structure of each table, please refer to the data dictionary in the `docs` folder.

## Setup and Installation

(Instructions for setting up the project will be added here)

## Usage

(Instructions for running the ETL pipeline will be added here)

## Contributing

(Guidelines for contributing to the project will be added here)

## License

(License information will be added here)
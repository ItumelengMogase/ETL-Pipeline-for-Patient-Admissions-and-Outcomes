# ETL Pipeline for Patient Admissions and Outcomes

## Table of Contents
- [Introduction](#introduction)
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Project Structure](#project-structure)
- [Data](#data)
  - [Downloading the Data](#downloading-the-data)
  - [Data Description](#data-description)
- [Setup](#setup)
- [Process](#process)
  - [1. Data Ingestion](#1-data-ingestion)
  - [2. Data Transformation](#2-data-transformation)
  - [3. Data Visualisation](#3-data-visualisation)
- [Running the Project](#running-the-project)

---

## Introduction

This project is an end-to-end ETL (Extract, Transform, Load) pipeline designed to process artificial patient admission and medical data. The pipeline uses **Apache Airflow** for orchestration, **PostgreSQL** for data storage, **dbt** for data transformation, and **Power BI** for data visualisation. The ETL pipeline automates the ingestion of raw data from CSV files, cleans and transforms it into structured formats, and stores it in a PostgreSQL database ready for querying and visualisation.

The dataset is synthetic and designed to mimic real-world medical records, with the ability to customise characteristics such as demographics, diagnoses, and lab results for thousands to millions of patients.

---

## The Problem

Accessing real-world Electronic Medical Records (EMRs) is often restricted due to privacy concerns and regulatory limitations. In addition, handling and processing large-scale medical data in real time presents challenges such as data integration, normalisation, and privacy protection.

---

## The Solution

This project uses a synthetic **database of artificial patients**. The data is generated with predefined characteristics that replicate real-world medical records, such as patient demographics, admissions, diagnoses, and lab results. The pipeline offers the flexibility to generate populations with customisable demographic distributions (e.g., 60% male, 40% African American) and specific medical conditions.

### Key Features:
- **Customisable database**: Generate a population of patients with custom characteristics.
- **Comprehensive**: Includes information such as patient demographics, lab results, admissions, and diagnosis codes (ICD-10).
- **Scalable**: The data can represent populations ranging from thousands to millions of records.

---

## Project Structure

```plaintext
├── airflow/
│   ├── dags/
│   └── plugins/
├── dbt/
│   ├── models/
│   ├── tests/
│   └── dbt_project.yml  # dbt project configuration
├── data/
│   └── raw/
│       └── patient_data.csv  # Raw data (downloaded)
├── scripts/
│   └── load_data.sql  # SQL script for PostgreSQL setup
├── docs/
├── docker-compose.yml  # Docker setup for PostgreSQL, Airflow, and dbt
└── README.md  # Project documentation
```

---

## Data

### Downloading the Data
The dataset is too large to upload directly to the repository. You can download the data from the following link:

[Download Patient Data (ZIP)](https://figshare.com/ndownloader/files/12941429)

After downloading, extract the files into the `data/raw/` directory. This data will be ingested into the pipeline.

### Data Description

The dataset consists of multiple tables that simulate patient records. Key tables include:

1. **PatientCorePopulatedTable**
   - Contains demographic data for each patient, including gender, race, marital status, and more.

2. **AdmissionsCorePopulatedTable**
   - Represents patient admission records, including admission start and end dates.

3. **AdmissionsDiagnosesCorePopulatedTable**
   - Stores primary diagnosis information for each patient admission, using ICD-10 codes.

4. **LabsCorePopulatedTable**
   - Contains patient lab results, including test names, values, and measurement units.

---

## Setup

### Prerequisites
- **Apache Airflow** (This project requires Airflow for orchestration)
- Docker and Docker Compose
- Power BI (for data visualisation)
- [dbt](https://docs.getdbt.com/docs/installation) installed locally or in Docker (the `dbt_project.yml` file is located in `C:\Users\Itumeleng\DEProjects\dbt\dbt_project.yml`).

### Clone the Repository
```bash
git clone https://github.com/ItumelengMogase/Real-Time-Data-Pipeline-for-Patient-Admissions.git
cd Real-Time-Data-Pipeline-for-Patient-Admissions
```

### Data Setup
1. Download the raw data ZIP file from [here](https://figshare.com/ndownloader/files/12941429) and extract it into the `data/raw/` folder.
2. The extracted CSV files will be used for ingestion into PostgreSQL.

### SQL Setup
- A SQL script for creating necessary PostgreSQL tables is provided in the `scripts/` folder as `load_data.sql`. This script sets up the database schema for patient data storage.

### Docker Setup
To set up the required services (PostgreSQL, Apache Airflow, dbt), start the Docker containers using the following command:
```bash
docker-compose up -d
```


---

![ETL Workflow](https://github.com/user-attachments/assets/4ad0dea0-4389-48fa-a799-9bfa564bc717)

## Process

### 1. Data Ingestion
- **Airflow** runs the **ingestion DAG** that reads raw CSV files from the `data/raw/` folder and inserts the data into **PostgreSQL staging tables**.
- This process ensures that the raw patient data is available in PostgreSQL for further transformation.

### 2. Data Transformation
- **dbt** is responsible for transforming the raw data into clean, structured tables. The transformation includes:
  - Cleaning and normalising patient demographics.
  - Mapping ICD-10 diagnosis codes and lab results to their standardised forms.
  - Creating fact and dimension tables to store cleaned data in a query-optimised format.

The `dbt_project.yml` file is located in the `C:\Users\Itumeleng\DEProjects\dbt\` directory.

### 3. Data Visualisation
- Once the data is transformed, **Power BI** can be used to visualise it. Power BI connects to the PostgreSQL database and provides visual insights, such as:
  - Trends in patient admissions.
  - Distributions of lab test results.
  - Diagnoses by demographic characteristics.

---

## Running the Project

### Step 1: Start Docker Services
Run the following command to start all services (Airflow, PostgreSQL, dbt):
```bash
docker-compose up -d
```

### Step 2: Ingest Data
- Go to the Airflow web UI (typically available at `http://localhost:8080`) and trigger the DAG responsible for ingesting raw data into PostgreSQL.

### Step 3: Run dbt Models
After the data is ingested, run the dbt models to transform the data:
```bash
dbt run
```
This will transform the raw data into cleaned fact and dimension tables within PostgreSQL.

### Step 4: Visualise Data in Power BI
- Open Power BI and connect it to the PostgreSQL database.
- Load the transformed tables into Power BI.
- Build dashboards and visual reports to explore trends in patient admissions, diagnoses, and outcomes.

---
## Setting Up dbt

1. **Create a `profiles.yml` file** in your `~/.dbt/` directory:
   ```yaml
   healthcare_pipeline:
     target: dev
     outputs:
       dev:
         type: postgres
         threads: 1
         host: localhost
         port: 5432
         user: <YOUR_USERNAME>
         password: <YOUR_PASSWORD>
         dbname: healthcare_pipeline_db
         schema: medical_data

## Conclusion

This project demonstrates a real-time ETL pipeline for processing medical data using **Docker**, **Apache Airflow**, **dbt**, and **PostgreSQL**. The pipeline automates the ingestion and transformation of synthetic patient data, making it ready for analysis in **Power BI**. The pipeline can be extended to handle larger datasets or other types of data sources.

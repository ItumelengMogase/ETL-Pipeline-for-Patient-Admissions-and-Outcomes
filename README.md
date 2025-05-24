
# 🏥 ETL Pipeline for Patient Admissions and Outcomes

This is a fully containerised ETL pipeline for managing synthetic patient data, including admissions and outcome tracking. It integrates **PostgreSQL**, **Apache Airflow**, and **dbt** within a **Docker** environment, and is extendable for use with **Power BI**, **spaCy**, or other tools. This project demonstrates how to automate data engineering workflows suitable for healthcare data analysis while complying with best practices in scalability and modularity.

## 📚 Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Access Airflow](#access-airflow)
- [PostgreSQL Access](#postgresql-access)
- [Working with dbt](#working-with-dbt)
- [dbt Documentation](#view-dbt-documentation)
- [Airflow DAG Workflow](#sample-airflow-dag-flow)
- [Power BI Integration (Optional)](#power-bi-integration-optional)
- [Full Reset (Optional)](#full-reset-optional)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)
- [Future Extensions](#future-extensions)
- [License](#license)
- [Maintainer](#maintainer)

## 🧱 Tech Stack

| Tool                | Purpose                                                |
|---------------------|--------------------------------------------------------|
| **Docker**          | Containerisation of all services                       |
| **PostgreSQL**      | Relational database for patient admissions             |
| **Apache Airflow**  | Workflow orchestration and scheduling engine           |
| **dbt**             | SQL-based transformation framework                     |
| **Power BI**        | Optional business intelligence dashboard               |
| **spaCy**           | Optional NLP pipeline for patient notes and metadata   |

## 📂 Project Structure

```
etl-patient-admissions/
├── dags/
├── dbt/
│   ├── models/
│   └── profiles.yml
├── logs/
├── plugins/
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 🛠 Prerequisites

- Docker and Docker Compose installed
- Port `5432` (Postgres) and `8080` (Airflow) must be free

## ⚙️ Setup Instructions

### 1. Clone the Project

```bash
git clone https://github.com/your-username/etl-patient-admissions.git
cd etl-patient-admissions
```

### 2. Launch Docker Containers

```bash
docker-compose up --build -d
```

### 3. Verify Services

```bash
docker ps
```

Ensure `postgres`, `airflow`, and `dbt` containers are running.

## 🌐 Access Airflow

- URL: [http://localhost:8080](http://localhost:8080)
- Username: `Itumeleng`
- Password: `libra`

## 🗄 PostgreSQL Access

| Setting     | Value            |
|-------------|------------------|
| Host        | localhost        |
| Port        | 5432             |
| Database    | patient_database |
| Username    | Itumeleng        |
| Password    | libra            |

## 🧪 Working with dbt

### Open dbt Shell

```bash
docker-compose exec dbt bash
```

### Run dbt

```bash
dbt debug
dbt run
dbt docs generate
dbt docs serve
```

## 📝 Sample Airflow DAG Flow

1. Extract data
2. Load to PostgreSQL
3. Run dbt models
4. Store outcomes in transformed tables

## 📈 Power BI Integration (Optional)

Use PostgreSQL connector with the same credentials above.

## 🧹 Full Reset (Optional)

```bash
docker-compose down -v
docker system prune -af --volumes
docker-compose up --build -d
```

## 🧯 Troubleshooting

| Issue                              | Solution |
|------------------------------------|----------|
| Airflow UI not loading             | Wait 60 seconds or check logs |
| dbt not running                    | Enter the container and retry |
| Postgres not accessible            | Check container status/logs   |

## 🔐 Security Notes

- Use `.env` for secrets in production
- Generate Fernet key: `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`

## ✅ Future Extensions

- Email alerts from Airflow
- spaCy for clinical NLP
- GitHub Actions CI/CD

## 📜 License

MIT License

## 🙋🏽‍♂️ Maintainer

**Itumeleng Mogase**  
📧 itumeleng@outlook.com  
🔗 [LinkedIn](https://www.linkedin.com/in/itumelengmogase)

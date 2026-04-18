# 🚀 Airflow-Based ETL Pipeline for Production-Grade Data Engineering

A production-style ETL pipeline demonstrating **Python, Apache Airflow, Docker, and PostgreSQL** using real-time API data.

---

# 🏗️ Architecture

```text
API Source (JSONPlaceholder)
        │
        ▼
┌───────────────┐
│   Airflow     │
│   Scheduler   │
│ (Manual/Daily)│
└───────────────┘
        │
        ▼

DAG Tasks:
1. extract  → API data fetch
2. transform → data cleaning + validation
3. load      → PostgreSQL insert (incremental)

        │
        ▼

┌─────────────────────────────────────┐
│     PostgreSQL (etl_db)             │
│-------------------------------------│
│ api_users   → Final processed data  │
│ airflow_*   → Metadata tables       │
└─────────────────────────────────────┘

        │
        ▼

(Optional Future)
┌───────────────┐
│  Power BI     │ → Dashboards
└───────────────┘
```

---

# ⚙️ Tech Stack

| Component        | Technology         |
| ---------------- | ------------------ |
| Orchestration    | Apache Airflow 2.6 |
| Processing       | Python + Pandas    |
| Storage          | PostgreSQL         |
| Containerization | Docker             |
| API Source       | JSONPlaceholder    |

---

# 📌 Key Features

* 🔄 API Data Ingestion
* 🧹 Data Cleaning & Validation
* 🚫 Incremental Loading (No duplicates)
* 🔁 Retry & Failure Handling
* 📊 Airflow DAG Orchestration
* 🐳 Fully Dockerized Setup

---

# 📂 Project Structure

```text
etl-pipeline-project/
├── dags/
│   ├── etl_dag.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── __init__.py
│
├── data/
├── logs/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚡ Quick Start

## 1️⃣ Start the system

```bash
docker-compose up --build
```

---

## 2️⃣ Open Airflow UI

```text
http://localhost:8080
```

Login:

```text
admin / admin
```

---

## 3️⃣ Run the pipeline

### Option A — UI

* Enable DAG: `api_etl_pipeline_v3`
* Click ▶ Trigger DAG

### Option B — CLI

```bash
docker exec -it airflow-webserver \
airflow dags trigger api_etl_pipeline_v3
```

---

# 📊 Output

Data is stored in:

```text
api_users
```

Example:

| id | name          | username | email                                         |
| -- | ------------- | -------- | --------------------------------------------- |
| 1  | Leanne Graham | Bret     | [sincere@april.biz](mailto:sincere@april.biz) |

---

# 🔁 Incremental Loading Logic

* First run → inserts all records
* Next runs → inserts only new records
* Prevents duplicate data

---

# 📸 Airflow DAG View

*Add your screenshot here*

```text
Screenshots/airflow_graph.png
```

---

# 🧠 Key Learnings

* Airflow DAG orchestration
* XCom communication between tasks
* Incremental ETL design
* Modular pipeline structure
* Docker-based deployment

---

# 💼 Resume Description

> Built a production-grade ETL pipeline using Apache Airflow, Docker, and PostgreSQL with API ingestion, modular design, and incremental data loading.

---

# 🚀 Future Improvements

* Power BI dashboard integration
* CI/CD pipeline (Azure DevOps / GitHub Actions)
* Streaming pipeline (Kafka)
* Data warehouse integration

---

# ⭐ Conclusion

This project demonstrates **real-world data engineering practices**, including orchestration, scalability, and clean architecture.

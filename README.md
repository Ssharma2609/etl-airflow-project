# Production-Grade ETL Pipeline using Airflow, Docker & PostgreSQL

An end-to-end **data engineering pipeline** that extracts data from an API, transforms it, and loads it into PostgreSQL using **Apache Airflow** for orchestration — built with production-ready practices like modular design, configuration management, and containerization.

---

# Architecture

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
1. extract   → API data ingestion (raw layer)
2. transform → cleaning + validation (processed layer)
3. load      → PostgreSQL insert (incremental)

        │
        ▼

┌─────────────────────────────────────┐
│     PostgreSQL (etl_db)             │
│-------------------------------------│
│ api_users        → Core dataset     │
│ analysis         → Aggregated data  │
│ graphanalysis    → Visualization    │
│ airflow_*        → Metadata tables  │
└─────────────────────────────────────┘

        │
        ▼

┌───────────────┐
│  Power BI     │ → Dashboard & Insights (Live Data)
└───────────────┘
```

---

# ⚙️ Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Orchestration    | Apache Airflow 2.x      |
| Processing       | Python + Pandas         |
| Storage          | PostgreSQL              |
| Visualization    | Power BI                |
| Containerization | Docker & Docker Compose |
| Configuration    | Python Config Module    |
| API Source       | JSONPlaceholder         |

---

# 📌 Key Features

* 🔄 API-based data ingestion
* 🧹 Data cleaning & validation
* 🚫 Incremental loading (duplicate-safe inserts)
* ⚙️ Config-driven pipeline (no hardcoded paths)
* 🔁 Airflow DAG orchestration
* 🐳 Fully Dockerized setup
* 📊 Data modeling for analytics (analysis & graphanalysis tables)
* 🔗 Live database integration with Power BI (no static files)

---

# 📂 Project Structure

```text
etl-pipeline-project/
│
├── dags/                # Airflow DAG definitions
│   └── etl_dag.py
│
├── etl/                 # ETL logic (modular)
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── config/              # Configuration
│   └── config.py
│
├── docker/              # Docker setup
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── data/                # Data layers (ignored in git)
│   ├── raw/
│   └── processed/
│
├── sample_data/         # Sample datasets
├── logs/                # Logs (ignored)
├── .gitignore
└── README.md
```

---

# ⚡ Quick Start

## 1️⃣ Start the system

```bash
docker-compose up -d
```

---

## 🔗 Access Services

### 🔹 Airflow UI

```text
http://localhost:8080
```

**Login:**

```text
admin / admin
```

---

### 🔹 PostgreSQL

| Parameter | Value     |
| --------- | --------- |
| Host      | localhost |
| Port      | 5433      |
| Database  | etl_db    |
| User      | postgres  |
| Password  | postgres  |

---

# ▶️ Run the Pipeline

### Option A — Airflow UI

* Enable DAG: `etl_dag`
* Click ▶ Trigger DAG

---

### Option B — CLI

```bash
docker exec -it airflow-scheduler \
airflow dags trigger etl_dag
```

---

# 🔌 Connect Power BI (Live Data Integration)

This project integrates Power BI directly with PostgreSQL for real-time dashboarding.

Connection Details:

* Host: `localhost`
* Port: `5433`
* Database: `etl_db`
* Username: `postgres`
* Password: `postgres`

Steps:

1. Open Power BI Desktop
2. Click **Get Data → PostgreSQL database**
3. Enter the above connection details
4. Select tables:

```text
api_users
analysis
graphanalysis
```

5. Click **Load**

---

### 🔄 Data Refresh

After running the Airflow pipeline:

```text
Power BI → Home → Refresh
```

👉 Dashboards update automatically based on latest database state

---

### ⚠️ Note

* PostgreSQL runs inside Docker
* Port `5433` is exposed for local access
* Power BI connects using this exposed port

---

# 📊 Output Tables

| Table Name    | Purpose                  |
| ------------- | ------------------------ |
| api_users     | Raw processed user data  |
| analysis      | Aggregated insights      |
| graphanalysis | Visualization-ready data |

---

# 🔁 Incremental Loading Logic

* First run → inserts all records
* Next runs → inserts only new data
* Prevents duplicate entries

---

# 🧠 Key Learnings

* Modular ETL pipeline design
* Airflow orchestration
* Config-driven development
* Incremental loading strategy
* Data modeling for analytics
* Docker-based deployment
* Real-time data visualization using Power BI

---

# 🎯 Interview Talking Points

| What you built       | How to explain it                                                     |
| -------------------- | --------------------------------------------------------------------- |
| Layered architecture | "Raw → Processed → Analytics layers similar to modern data pipelines" |
| Airflow DAG          | "Task-based orchestration with dependencies and retry handling"       |
| Incremental loading  | "Prevents duplicates using controlled insert logic"                   |
| Docker setup         | "Fully containerized environment for reproducibility"                 |
| Data modeling        | "Created analysis & graph tables for BI consumption"                  |
| Visualization        | "Integrated PostgreSQL with Power BI for real-time dashboarding"      |

---

# 💼 Resume Description

> Built a production-grade ETL pipeline using Apache Airflow, Docker, PostgreSQL, and Power BI with modular architecture, incremental loading, and analytics-ready data modeling.

---

# 🚀 Future Improvements

* 🔔 Alerting & monitoring
* ⚡ Bulk insert optimization
* 🔄 CI/CD integration
* 📡 Streaming pipeline (Kafka/Spark)

---

# ⭐ Conclusion

This project demonstrates **real-world data engineering practices**, including orchestration, modular design, data modeling, and real-time visualization — making it suitable for production-level workflows and interviews.

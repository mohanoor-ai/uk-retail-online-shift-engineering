# 🛒 UK Retail & Online Shift Engineering (2025 Baseline)

An end-to-end data engineering pipeline designed to analyze the structural shift in UK consumer behavior. This project automates the transition of raw, complex government indices into a production-grade analytical warehouse.

## 📝 Problem Statement
The UK retail sector is undergoing a massive digital transformation. In **2025**, while retail volumes recovered by **1.3%** after a two-year slump, the online share of sales surged to a peak of **28.6%** in late 2025. 

However, official data from the **Office for National Statistics (ONS)** is difficult for businesses to use because:
1. **Cryptic Identification:** Data relies on four-letter **CDID codes** (e.g., `J58U`) rather than human-readable retail sectors.
2. **Complex Schema:** The raw CSVs (11MB+) use a "Wide" survey format that requires significant unpivoting and cleaning for modern BI tools.
3. **Historical Revisions:** Monthly updates often revise previous months, requiring a robust pipeline to maintain a stable "Golden Record."

## 🚀 The Solution
This project provides a **Local-First, Cloud-Ready** pipeline that:
* **Ingests:** Scrapes and cleans the finalized 2025 ONS Retail Sales Index.
* **Processes:** Utilizes a **12-core optimized PySpark** environment to transform "Wide" survey data into "Long" analytical tables.
* **Models:** Employs **dbt** to create a Star Schema, mapping CDID codes to descriptive retail dimensions.
* **Orchestrates:** Uses **Airflow** to ensure data integrity and automated updates.

## 🏗️ Architecture & Tech Stack
| Stage | Tool | Description |
| :--- | :--- | :--- |
| **Infrastructure** | Terraform | Provisioning GCS and BigQuery on GCP. |
| **Orchestration** | Airflow | Scheduling the ETL workflow and monitoring success. |
| **Processing** | PySpark 3.5 | Distributed data cleaning on a 12-core WSL cluster. |
| **Data Lake** | GCS | "Bronze" (Raw) and "Silver" (Cleaned) storage layers. |
| **Warehouse** | BigQuery | "Gold" layer optimized for sub-second dashboarding. |
| **Modeling** | dbt | Transforming raw tables into Fact and Dimension models. |

## 📊 2025 Key Insights (Project Goals)
* **The Online Ceiling:** Did online sales stabilize at 28% or continue growing post-2025?
* **Sector Performance:** Comparing "Clothing & Footwear" (highly digital) vs. "Food Stores" (physical resilience).
* **The Weather Effect:** Correlating 2025/2026 record rainfall periods with surges in mobile e-commerce.

---
*Created as part of the Data Engineering Zoomcamp 2026.*

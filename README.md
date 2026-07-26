# Airline-Analytics-Pipeline-on-Databricks
# Airline Analytics Pipeline Documentation

## Overview
End-to-end data pipeline using Databricks Medallion Architecture to process US airport and airline data.

## Pipeline Details
- **Type:** Delta Live Tables Pipeline
- **Execution Order:** Bronze → Silver → Gold
- **Frequency:** On-demand / Scheduled Daily

## Architecture Layers

### Bronze Layer (Raw Ingestion)
- **Notebook:** 01_Bronze_Ingestion
- **Tables:** bronze_airports, bronze_airlines
- **Method:** CSV ingestion with schema inference
- **Purpose:** Raw data landing zone

### Silver Layer (Cleansing & Enrichment)
- **Notebook:** 02_Silver_Transformation
- **Tables:** silver_airports, silver_airlines
- **Operations:** 
  - Handle null values
  - Data type casting
  - Quality checks
- **Purpose:** Cleaned, trusted data

### Gold Layer (Analytics)
- **Notebook:** 03_Gold_Analytics
- **Tables:** 
  - gold_airport_fact
  - gold_state_summary
  - gold_airport_airlines_dim
- **Views:**
  - gold_vw_top_cities
  - gold_vw_state_distribution
  - gold_vw_airline_summary
- **Purpose:** Business-ready analytics

## Data Statistics
- **Airports:** 1,500+
- **Airlines:** 14
- **State Coverage:** 50+ US states

## Query Examples

### Top 5 States by Airport Count
```sql
SELECT state, total_airports 
FROM analytics.gold_state_summary 
ORDER BY total_airports DESC 
LIMIT 5;

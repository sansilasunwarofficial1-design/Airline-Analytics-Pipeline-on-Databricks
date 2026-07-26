# Databricks notebook source
# 01_Bronze_Ingestion

# ==========================================
# STEP 1: SET UP CONFIGURATION
# ==========================================

# Paths to your uploaded files
AIRPORTS_PATH = "/Volumes/dbacademy/get_started_de/myfiles/airports.csv"
AIRLINES_PATH = "/Volumes/dbacademy/get_started_de/myfiles/airlines.csv"

# ==========================================
# STEP 2: CREATE BRONZE TABLES
# ==========================================

# Create schema if it doesn't exist
spark.sql("CREATE SCHEMA IF NOT EXISTS bronze")

# Create bronze table for airports
print("Ingesting airports data...")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS bronze.airports
AS
SELECT 
    IATA_CODE AS airport_code,
    AIRPORT AS airport_name,
    CITY,
    STATE,
    COUNTRY,
    CAST(LATITUDE AS DOUBLE) AS latitude,
    CAST(LONGITUDE AS DOUBLE) AS longitude,
    CURRENT_TIMESTAMP() AS ingestion_timestamp
FROM read_files('{AIRPORTS_PATH}', format => 'csv', header => true)
""")

print(f"✅ Airports data loaded: {spark.table('bronze.airports').count()} records")

# Create bronze table for airlines
print("Ingesting airlines data...")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS bronze.airlines
AS
SELECT 
    IATA_CODE AS airline_code,
    AIRLINE AS airline_name,
    CURRENT_TIMESTAMP() AS ingestion_timestamp
FROM read_files('{AIRLINES_PATH}', format => 'csv', header => true)
""")

print(f"✅ Airlines data loaded: {spark.table('bronze.airlines').count()} records")

# ==========================================
# STEP 3: VERIFY DATA
# ==========================================

print("\n📊 Sample of airports data:")
display(spark.table("bronze.airports").limit(10))

print("\n📊 Sample of airlines data:")
display(spark.table("bronze.airlines"))
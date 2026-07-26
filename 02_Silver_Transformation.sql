-- Databricks notebook source


-- COMMAND ----------

-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS silver;

-- Create a cleaned, silver table for airports
CREATE OR REPLACE TABLE silver.airports
COMMENT "Cleaned airports data"
TBLPROPERTIES ("quality" = "silver")
AS
SELECT 
    airport_code,
    airport_name,
    CITY,
    STATE,
    COUNTRY,
    latitude,
    longitude,
    ingestion_timestamp
FROM bronze.airports;

-- Create a cleaned, silver table for airlines
CREATE OR REPLACE TABLE silver.airlines
COMMENT "Cleaned airlines data"
TBLPROPERTIES ("quality" = "silver")
AS
SELECT 
    airline_code,
    airline_name,
    ingestion_timestamp
FROM bronze.airlines;
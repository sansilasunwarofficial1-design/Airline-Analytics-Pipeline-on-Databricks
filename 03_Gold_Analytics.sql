-- Databricks notebook source
-- Create schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS gold;

-- Create a Gold dimension table combining airport and location data
CREATE OR REPLACE TABLE gold.dim_airports
COMMENT "Dimension table for airport analytics"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT 
    airport_code,
    airport_name,
    CITY,
    STATE,
    COUNTRY,
    latitude,
    longitude,
    CONCAT(CITY, ', ', STATE) AS location,
    ingestion_timestamp
FROM silver.airports;

-- Create an aggregated Gold table for airline summary
CREATE OR REPLACE TABLE gold.airline_summary
COMMENT "Summary metrics for airlines"
TBLPROPERTIES ("quality" = "gold")
AS
SELECT 
    airline_code,
    airline_name,
    COUNT(*) AS record_count,
    MAX(ingestion_timestamp) AS last_updated
FROM silver.airlines
GROUP BY airline_code, airline_name;
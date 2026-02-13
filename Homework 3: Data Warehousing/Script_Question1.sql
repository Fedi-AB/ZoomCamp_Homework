--==================================================================
-- Creating external table referring to gcs path with parquet files
--==================================================================
CREATE OR REPLACE EXTERNAL TABLE `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_ext`
-- OPTIONS is used to specify the format and location of the data files to be loaded into the external table. In this case, we are specifying that the data files are in PARQUET format and providing the URIs of the files located in a Google Cloud Storage bucket.
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_bucket_dtc/yellow_tripdata_2024-*.parquet']
);


--======================================================================
-- Querying the external table to calculate the total number of records
--======================================================================
SELECT
  COUNT(*)
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_ext`
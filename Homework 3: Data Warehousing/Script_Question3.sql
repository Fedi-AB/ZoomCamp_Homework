--==============================================================
-- Query PULocationID column from the regular table
--==============================================================
SELECT
    PULocationID
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`


--====================================================================
-- Query PULocationID and DOLocationID columns from the regular table
--====================================================================
SELECT
    PULocationID,
    DOLocationID
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`
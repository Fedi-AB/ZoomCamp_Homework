--======================================================================
-- Create a regular table in BQ using the data from the external table
--======================================================================
CREATE OR REPLACE TABLE `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`
AS
SELECT
    *
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_ext`;


--=========================================================================================
-- Count the distinct number of PULocationIDs for the entire dataset in the external table
--=========================================================================================
SELECT
    COUNT(DISTINCT PULocationID) AS distinct_pulocation_count
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_ext`;


--=========================================================================================
-- Count the distinct number of PULocationIDs for the entire dataset in the regular table
--=========================================================================================
SELECT
    COUNT(DISTINCT PULocationID) AS distinct_pulocation_count
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`;
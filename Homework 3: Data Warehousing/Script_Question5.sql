--===================================================================================
-- Create a new table partitioned by tpep_dropoff_datetime and clustered by VendorID
--===================================================================================
CREATE OR REPLACE TABLE `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_partitioned_clustered`
PARTITION BY 
    DATE(tpep_dropoff_datetime)
CLUSTER BY
    VendorID 
AS
SELECT
    *
FROM
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_ext`;
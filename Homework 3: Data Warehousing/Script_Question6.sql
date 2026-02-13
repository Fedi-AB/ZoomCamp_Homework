--======================================================
-- Querying data from the regular table
--======================================================
SELECT
    DISTINCT VendorID
FROM
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';



--=========================================================
-- Querying data from the partitioned and clustered table
--=========================================================
SELECT
    DISTINCT VendorID
FROM
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_partitioned_clustered`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
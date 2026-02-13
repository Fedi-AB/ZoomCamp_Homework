--==============================================================
-- Query to count the zero fare trips ( fare_amount = 0 )
--==============================================================
SELECT
    COUNT(*) AS zero_fare_trips
FROM 
    `data-engineering-project-dtc.de_gcp_dataset_dtc.yellow_tripdata_regular`
WHERE
    fare_amount = 0;
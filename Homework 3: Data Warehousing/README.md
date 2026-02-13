# ZoomCamp_Homework
## Module 3 Homework: Data Warehousing

---

## Question 1: Counting records

**SQL Scripts to create a table in our dataset and to query the data**  
[Script_Question1.sql](./Script_Question1.sql)


**The right answer:** 20,332,093 records

---

## Question 2: Data read estimation

**SQL Scripts to create a table in our dataset and to query the data**  
[Script_Question2.sql](./Script_Question2.sql)


**The right answer:** 0 MB for the External Table and 155.12 MB for the Materialized Table

---

## Question 3: Understanding columnar storage

**SQL Script in our dataset to query the data**  
[Script_Question3.sql](./Script_Question3.sql)

**Data amounts for queries execution are** 155 Mo for querying one column and 310 Mo for querying two columns.

**The right answer:**  BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

---

## Question 4: Counting zero fare trips

**SQL Script in our dataset to query the data**  
[Script_Question4.sql](./Script_Question4.sql)

**The right answer:** 8,333 trip

---

## Question 5: Partitioning and clustering

**SQL Script to create a partitioned and clustered table in our dataset**  
[Script_Question5.sql](./Script_Question5.sql)

**The right answer:** Partition by tpep_dropoff_datetime and Cluster on VendorID

---

## Question 6: Partition benefits

**SQL Script in our dataset to query the data**  
[Script_Question6.sql](./Script_Question6.sql)

**The right answer:**  310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

---

## Question 7: External table storage

**The right answer:**  GCP Bucket

---

## Question 8: Clustering best practices

**The right answer:** False

---

## Question 9: Understanding table scans

**SQL Script in our dataset to query the data**  
[Script_Question9.sql](./Script_Question9.sql)

**The right answer:**  The estimated bytes to read the data is arround 0 MB.
BigQuery uses internal(regular) table metadata, storage statistics and row count information maintained by the storage engine.
Because of this, it can return the total row count without reading column data blocks.
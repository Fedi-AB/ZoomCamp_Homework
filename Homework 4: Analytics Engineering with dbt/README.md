# ZoomCamp_Homework
## Module 4 Homework: Analytics Engineering with dbt

---

## Question 1: dbt Lineage and Execution

**The right answer:** stg_green_tripdata, stg_yellow_tripdata, and int_trips_unioned

---

## Question 2: dbt Tests

**The right answer:** dbt fails the test with non-zero exit code
**Explication:** 
    The test checks that all values present in the column are among the listed ones.
    If a new value (in this case, 6) appears in the data:
        - The test fails
        - dbt returns a non-zero exit code
        - You are immediately notified that there is unexpected data

---


## Question 3: Counting Records in fct_monthly_zone_revenue

**SQL Script in our dataset to query the data**  
[Script_Question3.sql](./Script_Question3.sql)

**The right answer:**  12,184 records

---

## Question 4: Best Performing Zone for Green Taxis (2020)

**SQL Script in our dataset to query the data**  
[Script_Question4.sql](./Script_Question4.sql)

**The right answer:** East Harlem North

---

## Question 5: Green Taxi Trip Counts (October 2019)

**SQL Script to create a partitioned and clustered table in our dataset**  
[Script_Question5.sql](./Script_Question5.sql)

**The right answer:** my quesry give me the value 387,006 trips (the nearest value in QCM is 384,624)

---

## Question 6: Build a Staging Model for FHV Data

**SQL Script in our dataset to query the data**  
[Script_Question6.sql](./Script_Question6.sql)

**The right answer:**  43,244,693 records

---
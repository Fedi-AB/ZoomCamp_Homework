# ZoomCamp_Homework
## Module 2 Homework: Workflow Orchestration - GCP

---

## Question 1

**Kestra script used to extract the CSV file:**  
[Question-1&2_Script.yaml](./Question-1&2_Script.yaml)

**Output logs:**

DEBUG 2026-02-11T14:15:20.463019Z Starting command with pid 725 [/bin/sh -c set -e wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-12.csv.gz | gunzip > yellow_tripdata_2020-12.csv]

**The right answer:** 128.3 MiB

---

## Question 2

**Kestra script used to extract the CSV file:**  
[Question-1&2&5_Script.yaml](./Question-1&2&5_Script.yaml)

**Output logs:**

DEBUG 2026-02-11T14:19:36.920513Z Starting command with pid 746 [/bin/sh -c set -e wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-04.csv.gz | gunzip > green_tripdata_2020-04.csv]

**The right answer:** green_tripdata_2020-04.csv

---

## Question 3

**Kestra script used:**  
[Question-3_Script.yaml](./Question-3_Script.yaml)

**The right answer:** 24,648,499 rows

---

## Question 4

**Kestra script used:**  
[Question-4_Script.yaml](./Question-4_Script.yaml)

**The right answer:** 1,734,051 rows

---

## Question 5

**Kestra script used:**  
[Question-1&2&5_Script.yaml](./Question-1&2&5_Script.yaml)

**The right answer:** 1,925,152 rows

---

## Question 6

**Trigger configuration to add:**

triggers:
  - id: ny_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 * * *"
    timezone: America/New_York

**The right answer:**  
Add a timezone property set to America/New_York in the Schedule trigger configuration.

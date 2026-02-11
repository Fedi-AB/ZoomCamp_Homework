# ZoomCamp_Homework
## Module 2 Homework: WorkFlow - Orchestration - GCP

* Question 1:
- The tapped script in the kestra to extract the csv file is [Question-1&2_Script.yaml](./Question-1&2_Script.yaml)
- The output logs :
    DEBUG 2026-02-11T14:15:20.463019Z Starting command with pid 725 [/bin/sh -c set -e
    wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-12.csv.gz | gunzip > yellow_tripdata_2020-12.csv]

==> The right answer is : 128.3 MiB
======================================================


* Question 2:
- The tapped script in the kestra to extract the csv file is [Question-1&2&5_Script.yaml](./Question-1&2&5_Script.yaml)
- The output logs :
    DEBUG 2026-02-11T14:19:36.920513Z Starting command with pid 746 [/bin/sh -c set -e
    wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-04.csv.gz | gunzip > green_tripdata_2020-04.csv]

==> The right answer is : green_tripdata_2020-04.csv
======================================================


* Question 3:
- The tapped script in the kestra to extract the csv file is [Question-3_Script.yaml](./Question-3_Script.yaml)

==> The right answer is : 24,648,499 rows
======================================================


* Question 4:
- The tapped script in the kestra to extract the csv file is [Question-4_Script.yaml](./Question-4_Script.yaml)

==> The right answer is : 1,734,051 rows
======================================================


* Question 5:
- The tapped script in the kestra to extract the csv file is [Question-1&2&5_Script.yaml](./Question-1&2&5_Script.yaml)

==> The right answer is : 1,925,152 rows
======================================================


* Question 6:
The configuration script to add to trigger config is :
    triggers:
      - id: ny_schedule
        type: io.kestra.plugin.core.trigger.Schedule
        cron: "0 9 * * *"
        timezone: America/New_York

==> The right answer is : Add a timezone property set to America/New_York in the Schedule trigger configuration
======================================================

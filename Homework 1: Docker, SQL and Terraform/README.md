# Module 1 Homework: Docker, Terraform & SQL

## Table of Contents
1. [Question 1: Understanding Docker Images](#question-1-understanding-docker-images)
2. [Question 2: Understanding Docker Networking and Docker Compose](#question-2-understanding-docker-networking-and-docker-compose)
3. [Question 3: Counting Short Trips](#question-3-counting-short-trips)
4. [Question 4: Longest Trip for Each Day](#question-4-longest-trip-for-each-day)
5. [Question 5: Biggest Pickup Zone](#question-5-biggest-pickup-zone)
6. [Question 6: Largest Tip](#question-6-largest-tip)
7. [Question 7: Terraform Workflow](#question-7-terraform-workflow)

---

## Question 1: Understanding Docker Images

**Script tapé dans le terminal :**

@Fedi-AB ➜ /workspaces/ZoomCamp_Homework (main) $ docker run -it --entrypoint bash python:3.13  
Unable to find image 'python:3.13' locally  
3.13: Pulling from library/python  
ef235bf1a09a: Pull complete  
954d6059ca7b: Pull complete  
b5e2021c4c8b: Pull complete  
128c71264009: Pull complete  
316fe9f6ee66: Pull complete  
0fc62e315fe6: Pull complete  
69b6f217f998: Pull complete  
Digest: sha256:e5fc5242206917be77a48689fd25f693eb2ae17b707f35c4645d08052d6e0d6e  
Status: Downloaded newer image for python:3.13  
root@ec2d6b4a98cf:/# pip --version  
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)  

**The right answer:** 25.3

---

## Question 2: Understanding Docker Networking and Docker Compose

**Script tapé dans le terminal :**

@Fedi-AB ➜ /workspaces/ZoomCamp_Homework/Homework 1: Docker, SQL and Terraform (main) $ docker compose up  

**The right answers:**  
- postgres:5432  
- db:5432

---

## Question 3: Counting Short Trips

**Data ingestion on Postgres (zone.py and ingest_green_parquet.py):**

python zone.py \
  --pg-user postgres \
  --pg-password postgres \
  --pg-host localhost \
  --pg-port 5433 \
  --pg-database ny_taxi  

**SQL Query on Postgres:**

SELECT  
    COUNT(*) AS trip_total_number  
FROM   
    public.green_taxi_data  
WHERE  
    trip_distance <= 1 AND  
    CAST(lpep_pickup_datetime AS DATE) BETWEEN '2025-11-01' AND '2025-11-30';  

**The right answer:** 8007

---

## Question 4: Longest Trip for Each Day

**SQL Query on Postgres:**

SELECT  
    CAST(lpep_pickup_datetime AS DATE) AS "DAY"  
FROM   
    public.green_taxi_data  
WHERE  
    trip_distance = (  
        SELECT  
            MAX(trip_distance)  
        FROM   
            public.green_taxi_data  
        WHERE   
            trip_distance < 100  
    );  

**The right answer:** 2025-11-14

---

## Question 5: Biggest Pickup Zone

**SQL Query on Postgres:**

SELECT   
    SUM(total_amount) AS largest_total_amount,  
    z."Zone"  
FROM   
    public.green_taxi_data AS gtd  
LEFT JOIN   
    public.taxi_zone_lookup AS z  
ON  
    gtd."PULocationID" = z."LocationID"  
WHERE   
    CAST(lpep_pickup_datetime AS DATE) = '2025-11-18'  
GROUP BY   
    z."Zone"  
ORDER BY   
    largest_total_amount DESC  
LIMIT 1;  

**The right answer:** East Harlem North

---

## Question 6: Largest Tip

**SQL Query on Postgres:**

SELECT   
    zdo."Zone" AS dropoff_zone,  
    SUM(gtd.tip_amount) AS total_tips  
FROM   
    public.green_taxi_data AS gtd  
JOIN   
    public.taxi_zone_lookup AS zpu  
ON   
    gtd."PULocationID" = zpu."LocationID"  
JOIN   
    public.taxi_zone_lookup AS zdo  
ON   
    gtd."DOLocationID" = zdo."LocationID"  
WHERE   
    TO_CHAR(gtd.lpep_pickup_datetime, 'YYYY-MM') = '2025-11'  
    AND zpu."Zone" = 'East Harlem North'  
GROUP BY   
    zdo."Zone"  
ORDER BY   
    total_tips DESC  
LIMIT 1;  

**The right answer:** Upper East Side North

---

## Question 7: Terraform Workflow

**The right answer:**  

terraform init  
terraform apply -auto-approve  
terraform destroy

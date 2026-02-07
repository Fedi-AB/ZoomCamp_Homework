# ZoomCamp_Homework
=================================
## Module 1 Homework: Docker & SQL

* Question 1. Understanding Docker images
  
Taped Script in the terminal : 

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
	
==> The right answer is : 25.3
==========


* Question 2. Understanding Docker networking and docker-compose

Taped scriot in terminal :

    @Fedi-AB ➜ /workspaces/ZoomCamp_Homework/Homework 1: Docker, SQL and Terraform (main) $ docker compose up

==> The right answers are : 
-postges:5432
-db:5432



* Question 3. Counting short trips

Data Ingestion on postgres for zone.py and ingest_green_parquet.py before starting analytics.

      python zone.py \
        --pg-user postgres \
        --pg-password postgres \
        --pg-host localhost \
        --pg-port 5433 \
        --pg-database ny_taxi


The SQL Query on Postgres:

        SELECT
	        COUNT(*) AS trip_total_number
	
        FROM 
	        public.green_taxi_data
	
        WHERE
	        trip_distance <= 1 AND
	        CAST(lpep_pickup_datetime AS DATE) BETWEEN '2025-11-01' AND '2025-11-30'

==> The right answer is 8007
==========


* Question 4. Longest trip for each day

The SQL Query on Postgres:

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
	        )

==> The right answer is 2025-11-14
==========


* Question 5. Biggest pickup zone

The SQL Query on Postgres:

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


==> The right answer is East Harlem North
==========


* Question 6. Largest tip

The SQL Query on Postgres:

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

==> The right answer is Upper East Side North
==========


* Question 7. Terraform Workflow

==> The right answer is terraform init, terraform apply -auto-approve, terraform destroy

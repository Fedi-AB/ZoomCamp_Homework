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
The right answer is : 25.3


* Question 2. Understanding Docker networking and docker-compose

Taped scriot in terminal :
    @Fedi-AB ➜ /workspaces/ZoomCamp_Homework/Homework 1: Docker, SQL and Terraform (main) $ docker compose up

The right answers are : 
-postges:5432
-db:5432




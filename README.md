# Data Pipeline for Real Estate Analytics


## Project Overview:

This project implements a high-performance Airflow data pipeline for scraping home listings from remax.com. It leverages Selenium for web scraping and employs a multithreaded approach to enhance the scraping speed. The pipeline is designed to scrape pages in parallel using Airflow's Celery Executor backed by Redis, ensuring efficient and scalable data processing.


##  Key Features:
* <b>Multithreaded Scraping</b>: Utilizes multiple threads to scrape home listings concurrently, significantly speeding up the process.
* Parallel Page Processing: Employs Airflow's Celery Executor with Redis to scrape multiple pages in parallel.
* Data Contract: Implements a data contract for validating scraped data before storage.
* PostgreSQL Integration: Stores validated data in a PostgreSQL database.
* Slowly Changing Dimensions (SCD) Modeling: Executes a subsequent job to model SCDs in the database.
* AWS Deployment: The entire pipeline is deployed on AWS.
* CD with GitHub Actions: Automated deployment and integration using GitHub Actions.
* Infrastructure as Code: Uses Terraform for creating and managing infrastructure.

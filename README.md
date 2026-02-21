# Event Ticket System Data Pipeline

## Project Overview
This project builds a basic data pipeline using Python and MySQL.
It loads third-party ticket sales data from a CSV file into a MySQL database
and generates a report of the most popular tickets in the past month.

## Requirements

- Python 3.x
- MySQL Server
- mysql-connector-python

Install dependency:

pip3 install mysql-connector-python

## Setup Steps

1. Create database:
   CREATE DATABASE ticket_db;

2. Run create_table.sql to create the sales table.

3. Update database credentials in ticket_pipeline.py.

4. Place third_party_sales.csv in project directory.

5. Run the pipeline:

   python3 ticket_pipeline.py

## Expected Output

Database connection successful
CSV Data Loaded Successfully

Here are the most popular tickets in the past month:
- The North American International Auto Show
- Carlisle Ford Nationals
- Washington Spirits vs Sky Blue FC

Pipeline completed successfully.

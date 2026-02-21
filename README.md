# Event Ticket Sales Data Pipeline

## Project Overview

This mini project implements a basic ETL (Extract, Transform, Load) data pipeline using Python and MySQL.

The system simulates a ticket platform that ingests third-party ticket sales data from a CSV file, stores it in a MySQL database, and analyzes ticket sales to determine the most popular events.

This project demonstrates database design, data loading, and aggregation queries using Python database connectors.

---

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- CSV file processing

---

## 📂 Project Structure

sales-ticket-pipeline/
│
├── create_table.sql
├── db_connection.py
├── load_data.py
├── queries.py
├── main.py
├── third_party_sales_1.csv
├── execution_log.txt
└── README.md


---

##  Setup Instructions

### Install MySQL (Mac - using Homebrew)

Install Homebrew (if not installed):

Install MySQL:
### 2 Create Database


---

## 📊 What the Pipeline Does

### Step 1: Database Connection
Establishes connection to MySQL using `mysql.connector`.

### Step 2: CSV Data Loading
Reads `third_party_sales_1.csv` and inserts each record into the `sales` table.

Dates are converted into proper DATE format before insertion.

### Step 3: Data Analysis
Runs an aggregation query to determine the most popular ticket events based on total tickets sold.

---

## 📈 Example Output



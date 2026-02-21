import mysql.connector


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            port='3306',
            database='ticket_db'
        )
        print("Database connection successful.")
        return connection
    except Exception as error:
        print("Error connecting to database:", error)
        return None
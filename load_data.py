import csv
from datetime import datetime


def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO sales (
            ticket_id, trans_date, event_id, event_name,
            event_date, event_type, event_city,
            customer_id, price, num_tickets
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with open(file_path_csv, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row

            for row in csv_reader:
                # Convert event_date to DATE format
                row[4] = datetime.strptime(row[4], "%Y-%m-%d").date()
                cursor.execute(insert_query, tuple(row))

        connection.commit()
        print("CSV data loaded successfully.")

    except Exception as e:
        print("Error loading CSV:", e)
        connection.rollback()

    finally:
        cursor.close()
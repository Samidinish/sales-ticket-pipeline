from db_connection import get_db_connection
from load_data import load_third_party
from queries import query_popular_tickets, display_results


if __name__ == "__main__":

    connection = get_db_connection()

    if connection:
        load_third_party(connection, "third_party_sales_1.csv")

        records = query_popular_tickets(connection)

        display_results(records)

        connection.close()
        print("\nPipeline completed successfully.")
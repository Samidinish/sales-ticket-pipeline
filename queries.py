def query_popular_tickets(connection):
    cursor = connection.cursor()

    sql_statement = """
        SELECT event_name, SUM(num_tickets) AS total_sold
        FROM sales
        GROUP BY event_name
        ORDER BY total_sold DESC
        LIMIT 5;
    """

    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()

    return records


def display_results(records):
    print("\nHere are the most popular tickets in the past month:")
    for record in records:
        print(f"- {record[0]} (Total Sold: {record[1]})")
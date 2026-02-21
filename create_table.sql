CREATE TABLE sales (
    ticket_id INT PRIMARY KEY,
    trans_date INT NOT NULL,
    event_id INT NOT NULL,
    event_name VARCHAR(50) NOT NULL,
    event_date DATE NOT NULL,
    event_type VARCHAR(10),
    event_city VARCHAR(20),
    customer_id INT,
    price DECIMAL(10,2),
    num_tickets INT
);
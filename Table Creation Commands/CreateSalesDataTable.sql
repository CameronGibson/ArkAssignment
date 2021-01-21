CREATE TABLE salesData (
	customer_name varchar(50) NOT NULL PRIMARY KEY,
	salesman_id varchar(100) NOT NULL,
	product_id varchar(100) NOT NULL,
	quantity_sold int NOT NULL,
	sales_date date NOT NULL
	);
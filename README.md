# Relational Database Assignment

This project demonstrates the use of SQLAlchemy to interact with a relational database. It includes the creation of database models, relationships, and CRUD (Create, Read, Update, Delete) operations. The database is implemented using MySQL, and the code is written in Python.

---

## Features

- **Database Models**:
  - `User`: Represents users with attributes like `id`, `name`, and `email`.
  - `Product`: Represents products with attributes like `id`, `name`, and `price`.
  - `Order`: Represents orders with attributes like `id`, `user_id`, `product_id`, `quantity`, and `shipped`.

- **Relationships**:
  - One-to-Many relationship between `User` and `Order`.
  - Many-to-One relationship between `Order` and `Product`.

- **CRUD Operations**:
  - Insert sample data into `Users`, `Products`, and `Orders` tables.
  - Query all users, products, and orders.
  - Update product prices.
  - Delete a user by ID.
  - Query non-shipped orders.
  - Count total orders per user.

---

## Prerequisites

- Python 3.9 or higher
- MySQL database
- Required Python packages:
  - `sqlalchemy`
  - `mysql-connector-python`

Install the required packages using pip:
```bash
pip install sqlalchemy mysql-connector-python
```

---

## Database Setup

Create the database using the following SQL command:
```sql
CREATE DATABASE relationaldatabaseassignment;
```

---

## Database Connection

Connect to the database using SQLAlchemy:
```python
engine = create_engine('mysql+mysqlconnector://<username>:<password>@localhost/relationaldatabaseassignment')
```

---

## Sample Data and Queries

### Users:
ID: 1, Name: Jarred, Email: Jarred@gmail.com  
ID: 2, Name: Kay, Email: Kay@gmail.com  
ID: 3, Name: Jakey, Email: Jakey@gmail.com  

### Products:
ID: 1, Name: Laptop, Price: 999  
ID: 2, Name: Smartphone, Price: 699  
ID: 3, Name: Headphones, Price: 199  

### Orders:
ID: 1, User ID: 1, Product ID: 2, Quantity: 1  
ID: 2, User ID: 2, Product ID: 1, Quantity: 2  
ID: 3, User ID: 1, Product ID: 3, Quantity: 3  
ID: 4, User ID: 2, Product ID: 2, Quantity: 4  

### Non-Shipped Orders:
Order ID: 1 - User ID: 1 - Product ID: 2 - Quantity: 1  
Order ID: 2 - User ID: 2 - Product ID: 1 - Quantity: 2  

### Total Orders per User:
User ID: 1, Name: Jarred, Order Count: 2  
User ID: 2, Name: Kay, Order Count: 2

Operations
Insert Sample Data: Adds sample users, products, and orders to the database.

Query Data: Retrieves and prints all users, products, and orders.

Update Product Price: Updates the price of a product with a specific ID.

Delete User: Deletes a user by their ID.

Query Non-Shipped Orders: Retrieves all orders that have not been shipped.

Count Orders per User: Counts the total number of orders placed by each user.

Notes
Ensure that the database connection string is updated with your MySQL credentials.
The script handles duplicate email entries using a try-except block for IntegrityError.
Modify the sample data or queries as needed for your use case.
License
This project is licensed under the MIT License. Feel free to use and modify it as needed. ```
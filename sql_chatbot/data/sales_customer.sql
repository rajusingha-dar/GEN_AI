# Creating a SQL script for 'sales' and 'customers' tables with ~10 rows each as requested

sales_customers_sql = """
-- Drop tables if they exist
DROP TABLE IF EXISTS sales_achievements;
DROP TABLE IF EXISTS sales_targets;
DROP TABLE IF EXISTS customer_feedback;
DROP TABLE IF EXISTS customers;

-- Create sales_targets table
CREATE TABLE sales_targets (
    target_id INT PRIMARY KEY,
    employee_id INT,
    year INT,
    target_amount DECIMAL(12,2)
);

-- Insert sample data into sales_targets
INSERT INTO sales_targets VALUES
(1, 101, 2023, 100000.00),
(2, 102, 2023, 85000.00),
(3, 103, 2023, 90000.00),
(4, 104, 2023, 95000.00),
(5, 105, 2023, 88000.00),
(6, 106, 2023, 92000.00),
(7, 107, 2023, 87000.00),
(8, 108, 2023, 94000.00),
(9, 109, 2023, 89000.00),
(10, 110, 2023, 97000.00);

-- Create sales_achievements table
CREATE TABLE sales_achievements (
    achievement_id INT PRIMARY KEY,
    employee_id INT,
    year INT,
    achieved_amount DECIMAL(12,2),
    bonus_awarded DECIMAL(10,2)
);

-- Insert sample data into sales_achievements
INSERT INTO sales_achievements VALUES
(1, 101, 2023, 95000.00, 500.00),
(2, 102, 2023, 87000.00, 750.00),
(3, 103, 2023, 91000.00, 600.00),
(4, 104, 2023, 97000.00, 850.00),
(5, 105, 2023, 86000.00, 450.00),
(6, 106, 2023, 93000.00, 700.00),
(7, 107, 2023, 88000.00, 620.00),
(8, 108, 2023, 95000.00, 900.00),
(9, 109, 2023, 91000.00, 640.00),
(10, 110, 2023, 98000.00, 1000.00);

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    join_date DATE
);

-- Insert sample data into customers
INSERT INTO customers VALUES
(1, 'David Green', 'david@example.com', 'New York', '2022-05-10'),
(2, 'Emily Stone', 'emily@example.com', 'Los Angeles', '2021-11-15'),
(3, 'Mark White', 'mark@example.com', 'Chicago', '2023-02-20'),
(4, 'Sophie Turner', 'sophie@example.com', 'Houston', '2020-09-18'),
(5, 'Jake Paul', 'jake@example.com', 'Phoenix', '2022-12-25'),
(6, 'Nina Dobrev', 'nina@example.com', 'Dallas', '2021-08-30'),
(7, 'Chris Evans', 'chris@example.com', 'Austin', '2023-03-10'),
(8, 'Scarlett Fox', 'scarlett@example.com', 'Seattle', '2021-04-22'),
(9, 'Bruce Wayne', 'bruce@example.com', 'Gotham', '2022-06-01'),
(10, 'Clark Kent', 'clark@example.com', 'Metropolis', '2020-10-10');

-- Create customer_feedback table
CREATE TABLE customer_feedback (
    feedback_id INT PRIMARY KEY,
    customer_id INT,
    feedback_text TEXT,
    rating INT,
    feedback_date DATE
);

-- Insert sample data into customer_feedback
INSERT INTO customer_feedback VALUES
(1, 1, 'Excellent service!', 5, '2023-03-01'),
(2, 2, 'Helpful staff.', 4, '2023-03-10'),
(3, 3, 'Could be faster.', 3, '2023-03-15'),
(4, 4, 'Very professional.', 5, '2023-04-01'),
(5, 5, 'Okay experience.', 3, '2023-04-05'),
(6, 6, 'Smooth account opening.', 4, '2023-04-10'),
(7, 7, 'Support was slow.', 2, '2023-04-15'),
(8, 8, 'Great app UI.', 5, '2023-04-18'),
(9, 9, 'Good loan options.', 4, '2023-04-20'),
(10, 10, 'Too many calls.', 2, '2023-04-25');
"""

-- Reset tables if they exist
DROP TABLE IF EXISTS accounts_handled;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS branches;


-- Create table: branches
CREATE TABLE branches (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100),
    location VARCHAR(100)
);

-- Create table: employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    job_title VARCHAR(50),
    branch_id INT,
    hire_date DATE,
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Create table: accounts_handled
CREATE TABLE accounts_handled (
    account_id INT PRIMARY KEY,
    employee_id INT,
    customer_name VARCHAR(100),
    account_type VARCHAR(50),
    balance DECIMAL(12, 2),
    open_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Insert into branches
INSERT INTO branches VALUES
(1, 'Downtown Branch', 'New York'),
(2, 'Westside Branch', 'Los Angeles'),
(3, 'Uptown Branch', 'Chicago'),
(4, 'Central Branch', 'Houston'),
(5, 'Bayview Branch', 'San Francisco'),
(6, 'Lakeside Branch', 'Seattle'),
(7, 'Sunrise Branch', 'Miami'),
(8, 'Capitol Branch', 'Washington DC'),
(9, 'Metro Branch', 'Atlanta'),
(10, 'Parkside Branch', 'Denver'),
(11, 'Hilltop Branch', 'Boston'),
(12, 'Eastend Branch', 'Philadelphia'),
(13, 'Southgate Branch', 'Dallas');

-- Insert into employees
INSERT INTO employees VALUES
(101, 'Alice Johnson', 'alice@bank.com', 'Relationship Manager', 1, '2019-04-15'),
(102, 'Bob Smith', 'bob@bank.com', 'Loan Officer', 2, '2020-08-01'),
(103, 'Charlie Lee', 'charlie@bank.com', 'Teller', 3, '2018-01-10'),
(104, 'Diana Prince', 'diana@bank.com', 'Branch Manager', 4, '2017-03-20'),
(105, 'Ethan Hunt', 'ethan@bank.com', 'Loan Officer', 5, '2021-05-11'),
(106, 'Fiona Gallagher', 'fiona@bank.com', 'Customer Service Rep', 6, '2022-02-01'),
(107, 'George Lucas', 'george@bank.com', 'Relationship Manager', 7, '2016-11-12'),
(108, 'Hannah Baker', 'hannah@bank.com', 'Teller', 8, '2023-01-09'),
(109, 'Ian Malcolm', 'ian@bank.com', 'Teller', 9, '2020-06-30'),
(110, 'Jane Foster', 'jane@bank.com', 'Loan Officer', 10, '2019-09-14'),
(111, 'Kevin Hart', 'kevin@bank.com', 'Branch Manager', 11, '2015-07-22'),
(112, 'Lara Croft', 'lara@bank.com', 'Customer Service Rep', 12, '2021-12-03'),
(113, 'Michael Scott', 'michael@bank.com', 'Regional Manager', 13, '2014-08-18');

-- Insert into accounts_handled
INSERT INTO accounts_handled VALUES
(1001, 101, 'David Brown', 'Savings', 5500.75, '2022-03-10'),
(1002, 102, 'Emma Wilson', 'Checking', 2300.50, '2023-06-15'),
(1003, 101, 'Frank White', 'Savings', 8700.00, '2021-11-22'),
(1004, 103, 'Grace Hall', 'Checking', 1200.25, '2023-01-05'),
(1005, 104, 'Henry Ford', 'Savings', 9600.00, '2022-07-20'),
(1006, 105, 'Isla Fisher', 'Checking', 3100.35, '2023-03-28'),
(1007, 106, 'Jack Sparrow', 'Savings', 7200.00, '2022-10-18'),
(1008, 107, 'Kelly Clarkson', 'Checking', 4400.60, '2021-09-13'),
(1009, 108, 'Liam Neeson', 'Savings', 8300.00, '2023-02-10'),
(1010, 109, 'Monica Geller', 'Checking', 2100.00, '2022-12-25'),
(1011, 110, 'Nathan Drake', 'Savings', 5000.00, '2021-05-19'),
(1012, 111, 'Olivia Benson', 'Checking', 6700.80, '2023-06-01'),
(1013, 112, 'Paul Rudd', 'Savings', 3900.45, '2022-04-04');

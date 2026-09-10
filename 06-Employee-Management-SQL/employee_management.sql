-- Assignment 5: MySQL - Employees

CREATE DATABASE IF NOT EXISTS company_db;

USE company_db;

DROP TABLE IF EXISTS employees;

-- Employees table create karna
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    emp_age INT,
    emp_department VARCHAR(50),
    emp_salary DECIMAL(10, 2),
    emp_city VARCHAR(50)
);

-- 10 employees insert karna
INSERT INTO employees
(emp_id, emp_name, emp_age, emp_department, emp_salary, emp_city)
VALUES
(1, 'Aman', 24, 'IT', 55000, 'Lucknow'),
(2, 'Anjali', 28, 'HR', 62000, 'Delhi'),
(3, 'Rahul', 32, 'Finance', 75000, 'Lucknow'),
(4, 'Priya', 26, 'IT', 48000, 'Delhi'),
(5, 'Arjun', 29, 'HR', 58000, 'Lucknow'),
(6, 'Neha', 23, 'IT', 45000, 'Kanpur'),
(7, 'Ravi', 35, 'Finance', 85000, 'Delhi'),
(8, 'Pooja', 27, 'IT', 65000, 'Lucknow'),
(9, 'Vikas', 31, 'HR', NULL, 'Kanpur'),
(10, 'Sneha', 25, 'Finance', 52000, 'Lucknow');

-- Sabhi employees display karna
SELECT * FROM employees;

-- Ek employee ki salary update karna
UPDATE employees
SET emp_salary = 60000
WHERE emp_id = 1;

-- Ek employee ka city change karna
UPDATE employees
SET emp_city = 'Kanpur'
WHERE emp_id = 5;

-- Ek employee delete karna
DELETE FROM employees
WHERE emp_id = 10;

-- Employees earning more than 50000
SELECT *
FROM employees
WHERE emp_salary > 50000;

-- Employees from IT
SELECT *
FROM employees
WHERE emp_department = 'IT';

-- Employees from Lucknow
SELECT *
FROM employees
WHERE emp_city = 'Lucknow';

-- Employees earning between 40000 and 60000
SELECT *
FROM employees
WHERE emp_salary BETWEEN 40000 AND 60000;

-- Employees whose name starts with A
SELECT *
FROM employees
WHERE emp_name LIKE 'A%';

-- Employees whose name ends with a
SELECT *
FROM employees
WHERE emp_name LIKE '%a';

-- Employees belonging to IT or HR
SELECT *
FROM employees
WHERE emp_department IN ('IT', 'HR');

-- Employees older than 25 and earning more than 50000
SELECT *
FROM employees
WHERE emp_age > 25
AND emp_salary > 50000;

-- Employees whose salary is NULL
SELECT *
FROM employees
WHERE emp_salary IS NULL;

-- Employees whose salary is not NULL
SELECT *
FROM employees
WHERE emp_salary IS NOT NULL;

-- Employees sorted by salary
SELECT *
FROM employees
ORDER BY emp_salary;

-- Employees sorted from highest salary to lowest
SELECT *
FROM employees
ORDER BY emp_salary DESC;

-- Count employees in every department
SELECT emp_department, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_department;

-- Average salary per department
SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department;

-- Maximum salary per department
SELECT emp_department, MAX(emp_salary) AS maximum_salary
FROM employees
GROUP BY emp_department;

-- Departments having more than 5 employees
SELECT emp_department, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_department
HAVING COUNT(*) > 5;

-- Departments whose average salary is greater than 60000
SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
HAVING AVG(emp_salary) > 60000;

-- Departments sorted by average salary
SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
ORDER BY average_salary;

-- Number of employees in every city
SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city;

-- Cities having more than 3 employees
SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city
HAVING COUNT(*) > 3;

-- Total number of employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Total salary
SELECT SUM(emp_salary) AS total_salary
FROM employees;

-- Average salary
SELECT AVG(emp_salary) AS average_salary
FROM employees;

-- Maximum salary
SELECT MAX(emp_salary) AS maximum_salary
FROM employees;

-- Minimum salary
SELECT MIN(emp_salary) AS minimum_salary
FROM employees;

-- Average salary of IT employees
SELECT AVG(emp_salary) AS average_it_salary
FROM employees
WHERE emp_department = 'IT';

-- Highest salary in HR
SELECT MAX(emp_salary) AS highest_hr_salary
FROM employees
WHERE emp_department = 'HR';

-- Total salary paid to Finance employees
SELECT SUM(emp_salary) AS total_finance_salary
FROM employees
WHERE emp_department = 'Finance';

-- Number of employees in Delhi
SELECT COUNT(*) AS delhi_employees
FROM employees
WHERE emp_city = 'Delhi';

-- Average salary of employees earning more than 50000
SELECT AVG(emp_salary) AS average_salary
FROM employees
WHERE emp_salary > 50000;

-- Department-wise total salary
SELECT emp_department, SUM(emp_salary) AS total_salary
FROM employees
GROUP BY emp_department;

-- Department-wise average salary
SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department;

-- Department with the highest average salary
SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
ORDER BY average_salary DESC
LIMIT 1;

-- Department with the highest total salary
SELECT emp_department, SUM(emp_salary) AS total_salary
FROM employees
GROUP BY emp_department
ORDER BY total_salary DESC
LIMIT 1;

-- City-wise employee count
SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city;
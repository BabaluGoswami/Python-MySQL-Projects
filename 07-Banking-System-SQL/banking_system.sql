-- Assignment 6: MySQL - Banking System

DROP DATABASE IF EXISTS banking_db;

CREATE DATABASE banking_db;

USE banking_db;

-- Branches table create karna
CREATE TABLE branches (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100),
    branch_city VARCHAR(50)
);

-- Customers table create karna
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_city VARCHAR(50),
    customer_status VARCHAR(20)
);

-- Accounts table create karna
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    branch_id INT,
    account_type VARCHAR(30),
    balance DECIMAL(12, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Cards table create karna
CREATE TABLE cards (
    card_id INT PRIMARY KEY,
    customer_id INT,
    card_type VARCHAR(30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Transactions table create karna
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_mode VARCHAR(30),
    transaction_amount DECIMAL(12, 2),
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Branch data insert karna
INSERT INTO branches
(branch_id, branch_name, branch_city)
VALUES
(1, 'Main Branch', 'Delhi'),
(2, 'Hazratganj Branch', 'Lucknow'),
(3, 'Civil Lines Branch', 'Kanpur'),
(4, 'Gomti Nagar Branch', 'Lucknow');

-- Customer data insert karna
INSERT INTO customers
(customer_id, customer_name, customer_city, customer_status)
VALUES
(1, 'Aman', 'Delhi', 'Active'),
(2, 'Anjali', 'Lucknow', 'Active'),
(3, 'Rahul', 'Kanpur', 'Active'),
(4, 'Priya', 'Delhi', 'Inactive'),
(5, 'Arjun', 'Lucknow', 'Active'),
(6, 'Neha', 'Kanpur', 'Active'),
(7, 'Ravi', 'Delhi', 'Active'),
(8, 'Pooja', 'Lucknow', 'Inactive'),
(9, 'Vikas', 'Delhi', 'Active'),
(10, 'Sneha', 'Kanpur', 'Active');

-- Account data insert karna
INSERT INTO accounts
(account_id, customer_id, branch_id, account_type, balance)
VALUES
(101, 1, 1, 'Savings', 125000),
(102, 1, 1, 'Current', 75000),
(103, 2, 2, 'Savings', 180000),
(104, 3, 3, 'Savings', 95000),
(105, 4, 1, 'Current', 45000),
(106, 5, 2, 'Savings', 220000),
(107, 6, 3, 'Savings', 65000),
(108, 7, 1, 'Current', 150000),
(109, 8, 4, 'Savings', 55000),
(110, 9, 1, 'Savings', 275000),
(111, 10, 3, 'Current', 85000),
(112, 2, 2, 'Current', 70000);

-- Card data insert karna
INSERT INTO cards
(card_id, customer_id, card_type)
VALUES
(501, 1, 'Debit'),
(502, 2, 'Debit'),
(503, 3, 'Credit'),
(504, 5, 'Debit'),
(505, 7, 'Debit'),
(506, 9, 'Credit');

-- Transaction data insert karna
INSERT INTO transactions
(transaction_id, account_id, transaction_mode, transaction_amount, transaction_date)
VALUES
(1001, 101, 'ATM', 10000, '2026-09-01'),
(1002, 101, 'UPI', 5000, '2026-09-02'),
(1003, 102, 'Online', 15000, '2026-09-02'),
(1004, 103, 'ATM', 20000, '2026-09-03'),
(1005, 103, 'UPI', 8000, '2026-09-03'),
(1006, 104, 'ATM', 7000, '2026-09-04'),
(1007, 106, 'Online', 25000, '2026-09-04'),
(1008, 106, 'UPI', 10000, '2026-09-05'),
(1009, 108, 'ATM', 12000, '2026-09-05'),
(1010, 110, 'Online', 30000, '2026-09-06'),
(1011, 110, 'ATM', 15000, '2026-09-06'),
(1012, 111, 'UPI', 6000, '2026-09-07'),
(1013, 112, 'Online', 9000, '2026-09-07'),
(1014, 101, 'ATM', 5000, '2026-09-08'),
(1015, 103, 'UPI', 12000, '2026-09-08'),
(1016, 106, 'ATM', 18000, '2026-09-08');

-- Q1. Find all active customers
SELECT *
FROM customers
WHERE customer_status = 'Active';

-- Q2. Find all savings accounts
SELECT *
FROM accounts
WHERE account_type = 'Savings';

-- Q3. Find accounts with balance greater than 1 lakh
SELECT *
FROM accounts
WHERE balance > 100000;

-- Q4. Find all ATM transactions
SELECT *
FROM transactions
WHERE transaction_mode = 'ATM';

-- Q5. Find customers from Delhi
SELECT *
FROM customers
WHERE customer_city = 'Delhi';

-- Q6. Total balance by branch
SELECT branch_id,
       SUM(balance) AS total_balance
FROM accounts
GROUP BY branch_id;

-- Q7. Average balance by account type
SELECT account_type,
       AVG(balance) AS average_balance
FROM accounts
GROUP BY account_type;

-- Q8. Number of accounts per customer
SELECT customer_id,
       COUNT(*) AS account_count
FROM accounts
GROUP BY customer_id;

-- Q9. Total transaction amount per customer
SELECT c.customer_id,
       c.customer_name,
       SUM(t.transaction_amount) AS total_transaction_amount
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name;

-- Q10. Total transactions by mode
SELECT transaction_mode,
       COUNT(*) AS transaction_count,
       SUM(transaction_amount) AS total_amount
FROM transactions
GROUP BY transaction_mode;

-- Q11. Customer + Account details
SELECT c.customer_id,
       c.customer_name,
       c.customer_city,
       a.account_id,
       a.account_type,
       a.balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id;

-- Q12. Customer + Account + Branch
SELECT c.customer_name,
       a.account_id,
       a.account_type,
       a.balance,
       b.branch_name,
       b.branch_city
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN branches b
ON a.branch_id = b.branch_id;

-- Q13. Customers having cards
SELECT DISTINCT c.*
FROM customers c
JOIN cards cr
ON c.customer_id = cr.customer_id;

-- Q14. Customers without cards
SELECT c.*
FROM customers c
LEFT JOIN cards cr
ON c.customer_id = cr.customer_id
WHERE cr.card_id IS NULL;

-- Q15. Customers having multiple accounts
SELECT c.customer_id,
       c.customer_name,
       COUNT(a.account_id) AS account_count
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(a.account_id) > 1;

-- Q16. Above-average balance customers
SELECT c.customer_id,
       c.customer_name,
       a.account_id,
       a.balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
WHERE a.balance > (
    SELECT AVG(balance)
    FROM accounts
);

-- Q17. Second-highest balance
SELECT MAX(balance) AS second_highest_balance
FROM accounts
WHERE balance < (
    SELECT MAX(balance)
    FROM accounts
);

-- Q18. Customers above their branch average
SELECT c.customer_name,
       a.account_id,
       a.branch_id,
       a.balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
WHERE a.balance > (
    SELECT AVG(a2.balance)
    FROM accounts a2
    WHERE a2.branch_id = a.branch_id
);

-- Q19. Highest transaction customer
SELECT c.customer_id,
       c.customer_name,
       SUM(t.transaction_amount) AS total_transaction
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_transaction DESC
LIMIT 1;

-- Q20. Branch with highest total balance
SELECT b.branch_id,
       b.branch_name,
       SUM(a.balance) AS total_balance
FROM branches b
JOIN accounts a
ON b.branch_id = a.branch_id
GROUP BY b.branch_id, b.branch_name
ORDER BY total_balance DESC
LIMIT 1;

-- Q21. Customer-wise total balance
SELECT c.customer_id,
       c.customer_name,
       SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name;

-- Q22. Customer-wise transaction volume
SELECT c.customer_id,
       c.customer_name,
       COUNT(t.transaction_id) AS transaction_volume
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY c.customer_id, c.customer_name;

-- Q23. Branch-wise average balance
SELECT b.branch_id,
       b.branch_name,
       AVG(a.balance) AS average_balance
FROM branches b
JOIN accounts a
ON b.branch_id = a.branch_id
GROUP BY b.branch_id, b.branch_name;

-- Q24. Above-average customers
SELECT c.customer_id,
       c.customer_name,
       SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(a.balance) > (
    SELECT AVG(total_balance)
    FROM (
        SELECT SUM(balance) AS total_balance
        FROM accounts
        GROUP BY customer_id
    ) AS customer_balances
);

-- Q25. Top customer per branch
SELECT customer_id,
       customer_name,
       branch_id,
       total_balance
FROM (
    SELECT c.customer_id,
           c.customer_name,
           a.branch_id,
           SUM(a.balance) AS total_balance,
           ROW_NUMBER() OVER (
               PARTITION BY a.branch_id
               ORDER BY SUM(a.balance) DESC
           ) AS customer_rank
    FROM customers c
    JOIN accounts a
    ON c.customer_id = a.customer_id
    GROUP BY c.customer_id,
             c.customer_name,
             a.branch_id
) AS ranked_customers
WHERE customer_rank = 1;

-- Q26. Rank customers by balance
SELECT c.customer_id,
       c.customer_name,
       SUM(a.balance) AS total_balance,
       RANK() OVER (
           ORDER BY SUM(a.balance) DESC
       ) AS balance_rank
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.customer_name;

-- Q27. Top 3 customers per branch
SELECT customer_id,
       customer_name,
       branch_id,
       total_balance
FROM (
    SELECT c.customer_id,
           c.customer_name,
           a.branch_id,
           SUM(a.balance) AS total_balance,
           ROW_NUMBER() OVER (
               PARTITION BY a.branch_id
               ORDER BY SUM(a.balance) DESC
           ) AS customer_rank
    FROM customers c
    JOIN accounts a
    ON c.customer_id = a.customer_id
    GROUP BY c.customer_id,
             c.customer_name,
             a.branch_id
) AS branch_ranked_customers
WHERE customer_rank <= 3;

-- Q28. Rank transactions per customer
SELECT c.customer_id,
       c.customer_name,
       t.transaction_id,
       t.transaction_amount,
       t.transaction_mode,
       RANK() OVER (
           PARTITION BY c.customer_id
           ORDER BY t.transaction_amount DESC
       ) AS transaction_rank
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id;
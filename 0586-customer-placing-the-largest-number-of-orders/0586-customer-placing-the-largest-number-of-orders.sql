# Write your MySQL query statement below
-- select customer_number from Orders group by order_number having order_number = max(order_number)

-- SELECT customer_number
-- FROM Orders
-- WHERE order_number = (SELECT MAX(order_number) FROM Orders)
-- LIMIT 1;


SELECT customer_number
FROM Orders
ORDER BY order_number DESC
LIMIT 1;


-- # Wri
-- select s.name from Orders o 
-- left join SalesPerson s 
-- on s.sales_id=o.sales_id 
-- where o.com_id not in
-- (select com_id from Company where name="RED")

SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

-- SELECT s.name
-- FROM Orders o
-- LEFT JOIN SalesPerson s ON s.sales_id = o.sales_id
-- WHERE o.com_id NOT IN (
--     SELECT c.com_id
--     FROM Company c
--     WHERE c.name = 'RED'
-- );



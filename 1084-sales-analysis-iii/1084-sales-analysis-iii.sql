# Write your MySQL quep.product_idry statement below
-- select p.product_id, p.product_name 
-- from Sales s left join Product p 
-- on p.product_id = s.product_id 
-- where s.sale_date between 2018-12-31 and 2019-04-01;

# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product p
INNER JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= "2019-01-01" 
AND MAX(s.sale_date) <= "2019-03-31";
# Write your MySQL query statement below

 with cte as (select d.name as Department, e.name as Employee,salary,
 max(salary) over(partition by d.name ) as Salary_max
 from employee e join department d on e.departmentId = d.id)

 select Department, Employee, Salary_max as Salary from cte 
 where salary = Salary_max;

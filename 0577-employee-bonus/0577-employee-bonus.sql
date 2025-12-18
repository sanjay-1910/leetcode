# Write your MySQL query statement below
# Write your MySQL query statement below
select e.name,b.bonus
from employee as e
left join Bonus as b on e.EmpId=b.EmpId
where bonus <1000 or bonus is null;
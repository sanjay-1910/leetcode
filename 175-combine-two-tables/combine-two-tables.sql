# Write your MySQL query statement below
-- select firstName,lastName,city,state from Person join Address on Person.personId = Address.personId;
# Write your MySQL query statement below
select firstName,lastName,city,state from Person left join Address on Person.personId=Address.personId;
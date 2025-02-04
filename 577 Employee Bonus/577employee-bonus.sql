# Write your MySQL query statement below
select name , bonus 
from Employee left Join Bonus ON Employee.empId = Bonus.empId
where bonus < 1000 or bonus is Null 
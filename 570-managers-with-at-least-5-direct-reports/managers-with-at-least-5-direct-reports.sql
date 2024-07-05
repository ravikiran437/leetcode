# Write your MySQL query statement below
select e1.name 
from employee e1
join (
    select managerid,count(managerid) as cnt from employee
    group by managerid
    having managerid is not null and cnt >= 5
) as report
on report.managerid = e1.id
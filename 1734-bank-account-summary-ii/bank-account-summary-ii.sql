# Write your MySQL query statement below
select u.name,tb.amount as balance
from users u 
join (
    select t.account,sum(t.amount) as amount
    from transactions t 
    group by t.account
) as tb 
on tb.account = u.account
having tb.amount > 10000
# Write your MySQL query statement below
select u.name,COALESCE(rk.distance, 0) as travelled_distance
from users u 
left join (
    select r.user_id,sum(r.distance) as distance
    from rides r 
    group by r.user_id
) as rk
on rk.user_id = u.id
order by travelled_distance desc,u.name
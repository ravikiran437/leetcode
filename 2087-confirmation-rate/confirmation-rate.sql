# Write your MySQL query statement below
select s.user_id,ifnull(round(cnt.user/cnt1.total,2),0) as confirmation_rate from signups s
left join (
    select user_id,count(user_id) as user from confirmations
    where action = "confirmed"
    group by user_id
) as cnt 
on cnt.user_id = s.user_id 
left join (
    select user_id,count(user_id) as total from confirmations
    group by user_id
) as cnt1
on cnt1.user_id = s.user_id
order by confirmation_rate
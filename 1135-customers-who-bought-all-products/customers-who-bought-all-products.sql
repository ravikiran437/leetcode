select c.customer_id from customer c 
group by customer_id
having count(distinct c.product_key) = (
    select count(p.product_key) from product p 
)
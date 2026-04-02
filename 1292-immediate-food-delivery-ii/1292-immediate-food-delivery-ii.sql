# Write your MySQL query statement below

select 

round(count(case when type = "immediate" then 1 else NULL end)
/
count(*)
*
100.00, 2)

as immediate_percentage from (

select *,
(case when order_date = customer_pref_delivery_date
then "immediate"
else "scheduled"
end) as type
from (
select *,
row_number() over (partition by customer_id order by order_date asc) as rnk
from Delivery) as rnk_table where rnk = 1

) as s 


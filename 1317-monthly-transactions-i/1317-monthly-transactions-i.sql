# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month, country, count(*) as trans_count, 
count(case 
    when state = 'approved' then amount 
    else NULL
end) AS approved_count 
,sum(amount) as trans_total_amount,
sum(case 
    when state = 'approved' then amount 
    else 0 
end) AS approved_total_amount 
from transactions
group by month, country
-- (
--    select DATE_FORMAT(trans_date, '%Y-%m') as month, country, sum(amount), state from transactions group by month, country having state = "approved"
-- ) as approved_count, 



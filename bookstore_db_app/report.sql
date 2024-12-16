--Create a report query that will show sales stats to the customer by genre, month, and the previous month.
with sales_by_category_month as (
select
p.category,
extract(year from order_date) as order_year,
date_trunc('month', order_date) as order_month,
sum(price * quantity) as total_sales
from
orders o
inner join product p on o.product_id = p.id
group by
category, order_year, order_month
)
select
category,
order_month,
total_sales as current_month_sales,
lag(total_sales) over (partition by category order by order_year, order_month) as previous_month_sales
from
sales_by_category_month
order by category, order_year, order_month
;


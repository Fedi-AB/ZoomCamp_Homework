SELECT 
    pickup_zone
FROM 
    prod_marts.monthly_revenue_per_location
WHERE revenue_monthly_total_amount = (
    SELECT MAX(revenue_monthly_total_amount)
    FROM prod_marts.monthly_revenue_per_location
    WHERE service_type = 'green'
      AND EXTRACT(YEAR FROM revenue_month) = 2020
)
AND service_type = 'green'
AND EXTRACT(YEAR FROM revenue_month) = 2020;
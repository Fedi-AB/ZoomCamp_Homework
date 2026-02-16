SELECT 
    SUM(total_monthly_trips) AS total_octobre_trip

FROM 
    prod_marts.monthly_revenue_per_location
WHERE
    STRFTIME('%Y-%m', revenue_month) = '2019-10'
    AND 
        service_type = 'green';

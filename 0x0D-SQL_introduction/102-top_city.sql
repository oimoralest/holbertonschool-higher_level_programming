-- This script displays the top 3 temperatures of cities
SELECT
    city,
    AVG(value) as `avg_temp`
    FROM temperatures
    WHERE month=7 or month=8
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;

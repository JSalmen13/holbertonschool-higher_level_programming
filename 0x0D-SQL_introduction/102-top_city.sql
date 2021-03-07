-- top 3 avg summer
SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC limit 3;
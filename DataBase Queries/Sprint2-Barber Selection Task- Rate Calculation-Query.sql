
-- this is our first query
use tahlil_project;
SET SQL_SAFE_UPDATES=0;
UPDATE barber_barber
JOIN (
    SELECT barber_rate.barbershop_id, AVG(barber_rate.stars) AS avg_stars
    FROM barber_rate
    GROUP BY barber_rate.barbershop_id
) AS subquery
ON barber_barber.id = subquery.barbershop_id
SET barber_barber.rate = ROUND(FORMAT(subquery.avg_stars,2));
SET SQL_SAFE_UPDATES=1;
select * from barber_barber



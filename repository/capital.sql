-- CREATE table

CREATE TABLE IF NOT EXISTS capitals
(
    id    SERIAL PRIMARY KEY,
    month INTEGER CHECK (1 <= month AND month <= 12),
    city  VARCHAR(50),
    sold  INTEGER
);

-- Data insertion
INSERT INTO capitals (month, city, sold)
VALUES (1, 'Rome', 200),
       (2, 'Paris', 500),
       (1, 'London', 100),
       (1, 'Paris', 300),
       (2, 'Rome', 300),
       (2, 'London', 400),
       (3, 'Rome', 400);


-- MEDIAN

SELECT percentile_cont(0.5) WITHIN GROUP ( ORDER BY sold ) AS median
FROM capitals;

WITH temp_counter AS (SELECT *,
                             row_number() over (ORDER BY sold) AS rn,
                             COUNT(*) over ()                  AS rc
                      FROM capitals)

SELECT sold
FROM temp_counter
WHERE rn IN (
             (rc + 1) / 2, (rc + 2) / 2
    );


WITH sum_by_city AS (SELECT city, SUM(sold) AS summ
                     FROM capitals

                     GROUP BY city)

SELECT capitals.city, sold, summ
FROM capitals

         JOIN sum_by_city s on capitals.city = s.city

ORDER BY city, month;

--

SELECT capitals.city,
       sold,
       capitals.month,
--        SUM(sold) over city_      summ,
--        SUM(sold) over city_month summ_,
--        AVG(sold) over city_month avg,
       sold - LAG(sold, 1, 0) over city_month lag_
--        LEAD(sold, 1, 0) over city_month lead_

FROM capitals
WINDOW city_ AS (
        PARTITION BY city
        ),
       city_month AS (
               PARTITION BY city
               ORDER BY month
               );


-- billing task

SELECT * FROM billing

ORDER BY currency, billing_date;


CREATE TABLE Groups_1 (
    id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE Groups_2 (
    id INT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

DO $$
BEGIN
    FOR cnt IN 1..10 LOOP
        RAISE NOTICE 'cnt: %', cnt;
    END LOOP;
END; $$
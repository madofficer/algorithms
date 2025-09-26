CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT * FROM crosstab(
$$select * from(values
  ('a', 'b', 'c'),
  ('a', 'b', 'e'),
  ('b', 'b', 'c'),
  ('b', 'b', 'd')
) as t (c1, c2, c3) $$) as t1(Column_name text, Cat1 text, Cat2 text, Cat3 text)

--
SELECT column_name
FROM
    information_schema.columns
WHERE table_schema = 'public' AND table_name = 'clients';

select *
from crosstab(
 'select *
  from ('
|| ( select string_agg(sql, '') as sql_string
 from (
  select case when row_number() OVER () = 1 then '' else ' union all ' end
  || 'select '''
  || column_name || ''' as column_name, ''cat'' as category, '
  || '100.0 * (count(*) - count('
    ||column_name||  '))/coalesce(count(*),1) as val from '
  || table_schema
  || '.'
  || table_name as sql
  from information_schema.columns
  where table_schema = 'public' and table_name = 'clients') as sql_query
   )
  || ') as column_counts ')
as ct(row_name text, cat_1 numeric )
order by cat_1 desc, row_name;
-- fetch first 1 rows with ties;

WITH result_1 AS (
SELECT *
FROM table_ASD -- this is a comment 
), 
result_2 as (select * from table_b where a=2)
select a+b as c,
a,
f,c
from result_1 inner join result_2 on result_1.a=result_2.a

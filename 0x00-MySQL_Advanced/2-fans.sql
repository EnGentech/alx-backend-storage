-- Query database with data grouped by the sum of fans

select origin, sum(fans) as nb_fans group by origin
order by nb_fans desc;
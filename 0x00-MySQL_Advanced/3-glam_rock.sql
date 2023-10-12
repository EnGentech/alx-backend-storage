-- select * from metal_bands;

select band_name, 
ifnull(split, 2022) - ifnull(formed, 0) as lifespan
from metal_bands where style like "%Glam rock%";
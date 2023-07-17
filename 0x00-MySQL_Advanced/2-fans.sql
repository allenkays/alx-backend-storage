-- SQL script that ranks country origins of bands
-- Column names must be: origin and nb_fans

SELECT DISTINCT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

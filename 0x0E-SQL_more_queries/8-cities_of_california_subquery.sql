-- Lists all the cities of California that can be found in  hbtn_0d_usa.
-- The states table contains only one record where name = California 

SELECT id, name FROM cities
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name = 'california'
)
ORDER BY id ASC;

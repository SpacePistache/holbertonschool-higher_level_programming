-- A script listing all the cities stored in the Yeehaw database
SELECT cities.id, cities.name, states.name 
FROM cities, states 
WHERE cities.state_id = states.id 
ORDER BY cities.id;

-- A scripti listing all the cities in california found in Yank database
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1) 
ORDER BY id;
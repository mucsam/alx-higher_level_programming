-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM states s
JOIN cities c 
ON s.id = c.state_id
ORDER BY c.id ASC;
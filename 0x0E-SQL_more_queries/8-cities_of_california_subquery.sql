-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT cities.name, cities.id
FROM states, cities
WHERE states.name = 'California';
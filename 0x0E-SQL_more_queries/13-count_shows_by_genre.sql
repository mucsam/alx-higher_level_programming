-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tg.name AS genre, COUNT(ts.id) AS number_of_shows
FROM tv_genres tg 
JOIN tv_show_genres tsg 
ON tg.id = tsg.genre_id
JOIN tv_shows ts
ON tsg.show_id = ts.id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
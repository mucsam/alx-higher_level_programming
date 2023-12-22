-- uses the hbtn_0d_tvshows database to list all 
-- genres of the show Dexter
SELECT tg.name
FROM tv_shows ts
JOIN tv_show_genres tsg
ON tsg.show_id = (
    SELECT id FROM tv_shows WHERE title = 'Dexter'
)
JOIN tv_genres tg 
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY tg.name ASC;
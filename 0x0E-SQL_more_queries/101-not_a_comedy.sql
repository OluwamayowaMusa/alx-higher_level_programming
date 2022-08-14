-- List all movies not under genre comedy
SELECT tv_shows.title
 FROM tv_shows
 LEFT OUTER JOIN
 (SELECT tv_shows.title
	   FROM tv_shows
	   INNER JOIN tv_show_genres
	   ON tv_shows.id = tv_show_genres.show_id
	   INNER JOIN tv_genres
	   ON tv_genres.id = tv_show_genres.genre_id
	   WHERE tv_genres.name = "Comedy") AS table_1
 USING (title)
 WHERE table_1.title is NULL
 ORDER BY tv_shows.title ASC;

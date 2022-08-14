-- List all movies under genre Comedy
SELECT tv_shows.title
 FROM tv_show_genres
 INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
 INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
 WHERE tv_genres.name = "Comedy"
 ORDER BY tv_shows.title ASC;

-- List all genre of the show Dexter
SELECT tv_genres.name
 FROM tv_show_genres
 INNER JOIN tv_shows
 ON tv_shows.title = "Dexter" AND tv_show_genres.show_id = 8
 INNER JOIN tv_genres
 ON tv_genres.id = tv_show_genres.genre_id
 ORDER BY tv_genres.name ASC;

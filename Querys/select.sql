-- Artistic technic
--               All artistic technics
SELECT id_at,title FROM artistic_technic;
--              Artistic technic id with name
SELECT id_at FROM artistic_technic WHERE title = 'Escultura';

-- Artist
--              All artist
SELECT id_artist, (lastname_artist||', '||name_artist) AS artist FROM artist;
--              Artist id with name
SELECT id_artist FROM artist WHERE name_artist='Sandro Javier' AND lastname_artist = 'Bolaños Castro';


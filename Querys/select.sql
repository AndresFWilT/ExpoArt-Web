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
-- Artist by id 
SELECT id_artist, (name_artist||' '||lastname_artist), email_artist, phone FROM artist WHERE id_artist = 1;

-- Galery creation
SELECT art.title_artwork, art.id_artwork, art.image, at.title, ar.name_artist||' '||ar.lastname_artist
FROM Artwork art, artwork_technic aatt, Artistic_Technic at, artwork_artist aart, Artist ar
WHERE art.id_artwork = aatt.id_artwork_fk AND aatt.id_at_fk = at.id_at AND art.id_artwork = aart.id_artwork_fk AND aart.id_artist_fk = ar.id_artist;

-- selected artwork
SELECT art.title_artwork, art.id_artwork, art.image, art.descriptrion_artwork, art.date_published, at.title, ar.name_artist||' '||ar.lastname_artist
FROM Artwork art, artwork_technic aatt, Artistic_Technic at, artwork_artist aart, Artist ar
WHERE art.id_artwork = 24 AND art.id_artwork = aatt.id_artwork_fk AND aatt.id_at_fk = at.id_at AND art.id_artwork = aart.id_artwork_fk AND aart.id_artist_fk = ar.id_artist;

-- Delete from artistic_technic
DELETE FROM artistic_technic WHERE id_at = 2;

-- Delete from artist
DELETE FROM artist WHERE id_artist = 1;

-- Delete from
DELETE FROM artwork_artist WHERE id_artwork_fk = 1;
DELETE FROM artwork_technic WHERE id_artwork_fk = 1;
DELETE FROM artwork WHERE id_artwork = 1;
-- Insert into Artistic Technic

UPDATE artistic_technic SET title = 'title',description = 'desc' WHERE id_at = 1;

-- Insert into Artist
UPDATE artist SET name_artist = 'title', lastname_artist = '', email_artist = '', phone = 456465465 WHERE id_artist = 1;

-- Insert into Artwork (also inserts to artwork-artist, artwork-artistictechnic)
UPDATE artwork SET title_artwork = '', descriptrion_artwork = '', date_published = {to_date('{__date}','YYYY/MM/DD')}


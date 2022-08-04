-- Insert into Artistic Technic

INSERT INTO artistic_technic (title,description) VALUES ('title','desc');

-- Insert into Artist
INSERT INTO artist (name_artist,lastname_artist,email_artist,phone) VALUES ('Sandro','Castro','sandrocorreo@udistrital.edu.co',6668744);

-- Insert into Artwork (also inserts to artwork-artist, artwork-artistictechnic)
INSERT INTO artwork (title_artwork, descriptrion_artwork,date_published,image) VALUES ('','',NOW(),'link');
INSERT INTO artwork_artist (id_artist_fk,id_artwork_fk) VALUES (1,1);
INSERT INTO artwork_technic (id_at_fk,id_artwork_fk) VALUES (1,1);



-- Insert into Artistic Technic

INSERT INTO artistic_technic (title,description) VALUES ('title','desc');

-- Insert into Artist
INSERT INTO artist (name_artist,lastname_artist,email_artist,phone) VALUES ('Sandro','Castro','sandrocorreo@udistrital.edu.co',6668744);

-- Insert into Artwork (also inserts to artwork-artist, artwork-artistictechnic, doctype)
INSERT INTO artwork (title_artwork, descriptrion_artwork,date_published,image) VALUES ('','',NOW(),'link');
INSERT INTO artwork_artist (id_artist_fk,id_artwork_fk) VALUES (1,1);
INSERT INTO artwork_technic (id_at_fk,id_artwork_fk) VALUES (1,1);
INSERT INTO doctype(id_doc, type_doc) VALUES (900, 'Cedula de Ciudadania');
INSERT INTO doctype(id_doc, type_doc) VALUES (901, 'Tarjeta de Identidad');
INSERT INTO doctype(id_doc, type_doc) VALUES (902, 'Cedula de Extranjeria');
INSERT INTO doctype(id_doc, type_doc) VALUES (903, 'NIT');
INSERT INTO category(id_category, cat_name) VALUES (1, 'Pintura');
INSERT INTO category(id_category, cat_name) VALUES (2, 'Dibujo');
INSERT INTO category(id_category, cat_name) VALUES (3, 'Muestra Externa');
INSERT INTO public.ideas(id_ideas, id_category_idfk, id_user_idfk, ideas_title, ideas_desc, is_public) VALUES (1, 1, 1111, 'El sol saliente', 'Esta obra tiene como objetivo recrear las sesaciones que generan cada mañana en los bogotanos los dias soleados', false);


DROP TABLE IF EXISTS movies.tag;
CREATE TABLE movies.tag (
  tag_id INT NOT NULL,
  tag_name varchar(50) DEFAULT NULL,
  CONSTRAINT pk_tag PRIMARY KEY (tag_id)
);

INSERT INTO movies.tag (tag_id, tag_name) VALUES
(12,'Adventure'),
(14,'Fantasy'),
(16,'Animation'),
(18,'Drama'),
(27,'Horror'),
(28,'Action'),
(35,'Comedy'),
(36,'History'),
(37,'Western'),
(48,'Mystery'),
(49,'Romance'),
(51,'Family'),
(52,'War'),
(53,'Thriller'),
(69,'Foreign'),
(70,'TV Movie'),
(78,'Science Fiction'),
(80,'Crime'),
(82,'Music'),
(99,'Documentary'),
/*Genrelist ends, Keyword list begins*/
(100,'HDTGM'),
(101,'Holiday'),
(102,'Cheesy'),
(103,'Nic Cage'),
(104,'Anime'),
(105,'Mecha'),
(106,'Show Dash');

DROP TABLE IF EXISTS movies.watchlist;
CREATE TABLE movies.watchlist (
  movie_id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) DEFAULT NULL,
  runtime INT DEFAULT NULL,
  movie_status VARCHAR(50) DEFAULT NULL,
  imdb_id INT DEFAULT NULL,
  req VARCHAR(50) DEFAULT NULL,
  CONSTRAINT pk_watchlist PRIMARY KEY (movie_id)
);

INSERT INTO movies.watchlist (movie_id, title, runtime, movie_status, imdb_id, req)
VALUES
(1,'The Room',null,'Watched',null,'Dash'),
(2,'Fateful Findings',null,'Downloaded',null,'Dash'),
(3,'Miami Connection',null,'Downloaded',null,'Dash'),
(4,'Voyage of the Rock Aliens',null,'Downloaded',null,'Dash'),
(5,'The Visitor',null,'Downloaded',null,'Dash'),
(6,'Hello Mary Lou: Prom Night II',null,'Downloaded',null,'Dash'),
(7,'Ninja III: The Domination',null,'Downloaded',null,'Dash'),
(8,'Drop Dead Fred',null,null,null,'Dash'),
(9,'Hercules',null,null,null,'Dash'),
(10,'Death Spa',null,'Downloaded',null,'Dash'),
(11,'Maximum Overdrive',null,'Watched',null,'Dash'),
(12,'Zardoz',null,'Downloaded',null,'Dash'),
(13,'Gymkata',null,'Downloaded',null,'Dash'),
(14,'Nothing But Trouble',null,'Downloaded',null,'Dash'),
(15,'Birdemic',null,'Downloaded',null,'Dash'),
(16,'Exit Humanity',null,null,null,null),
(17,'Ninja Terminator',null,'Downloaded',null,'Dash'),
(18,'Hurricane Heist/Geostorm',null,null,null,'Dash'),
(19,'Govenor Gabbi',null,null,null,'Dash'),
(20,'VelociPastor',null,null,null,'Dash'),
(21,'The Peanut Butter Solution',null,null,null,'Dash'),
(22,'The Great Wall',null,'Downloaded',null,'Dash'),
(23,'Double Dragon',null,null,null,'Dash'),
(24,'Whats Up, Tiger Lily?',null,null,null,null),
(25,'The Neighbors',null,null,null,null),
(26,'The Truman Show (1998)',null,'Downloaded',null,'Dash'),
(27,'They Live',null,'Downloaded',null,'Hen'),
(28,'The Adventures of Buckaroo Banzai Across the 8th Dimension (1984)',null,null,86856,'Hen'),
(29,'Invasion USA',null,null,null,'Hen'),
(30,'The Thing (1982)',null,'Downloaded',null,'Hen'),
(31,'Red Dawn',null,null,null,'Hen'),
(32,'Heavy Metal',null,null,null,'Hen'),
(33,'Outland (1981)',null,null,null,'Hen'),
(34,'Kamakazi (1989)',null,null,null,'Hen'),
(35,'Behind the Mask: The Rise of Leslie Vernon',null,'Downloaded',null,'Hen'),
(36,'The Warriors',null,'Downloaded',null,'Spencer'),
(37,'Broken Arrow',null,'Downloaded',null,'Dash'),
(38,'Tango and Cash (1989)',null,'Downloaded',null,'Dash'),
(39,'Combat Mecha Xabungle (1982)',null,null,null,'Hen'),
(40,'The Evil Dead (I-IV)',null,'Downloaded',null,'Dash'),
(41,'Fatman',null,'Downloaded',null,'Dash'),
(42,'Christmas Evil',null,'DVD',null,'Dash'),
(43,'RRR (2022)',null,'Downloaded',null,'Spencer'),
(44,'Kung Pow Enter the Fist (2002)',null,'Downloaded',null,'Adam'),
(45,'Den of Theives (2018)',null,'Downloaded',null,'Dash'),
(46,'The Rock',null,'Downloaded',null,'Dash'),
(47,'Snatch',null,'Downloaded',null,'Dash'),
(48,'Legend (2015)',null,'Downloaded',null,'Dash'),
(49,'The Witch',null,'Downloaded',null,'Spencer'),
(50,'The Running Man (1987)',null,'Downloaded',null,'Dash');

DROP TABLE IF EXISTS movies.watchlist_tags;
CREATE TABLE movies.watchlist_tags (
  movie_id INT DEFAULT NULL,
  tag_id INT DEFAULT NULL,
  CONSTRAINT fk_mt_tag FOREIGN KEY (tag_id) REFERENCES movies.tag (tag_id),
  CONSTRAINT fk_mt_movie FOREIGN KEY (movie_id) REFERENCES movies.watchlist (movie_id)
);

INSERT INTO movies.watchlist_tags (movie_id, tag_id) VALUES
(39,104);

COMMIT;
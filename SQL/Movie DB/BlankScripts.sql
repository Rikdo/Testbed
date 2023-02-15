delete from tag where tag_id = 109;

delete from watchlist where movie_id in (52, 53);
delete from watchlist_tags order by tag_id desc limit 1;

SELECT Movie_Id, title FROM Watchlist WHERE Title like "the g%";

SELECT Movie_Id, title, movie_status FROM Watchlist WHERE req = "Spencer";

alter table watchlist_tags add constraint uc_mt_combo unique (movie_id, tag_id);

call list_by_tag("");

update watchlist set movie_status = "Watched" where movie_id = 73;
update watchlist set movie_status = "Hold" where movie_id in (8,19,21,20,25,24,27);

insert into watchlist_tags(movie_id, tag_id) values (83, 104);
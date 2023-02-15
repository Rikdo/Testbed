call add_to_watchlist("Farcry", "Uwe Boll", "Hen");

select movie_id, title as "Last Five" from watchlist
order by movie_id desc
limit 5;

select tag_name as "Last Five", tag_id from tag
order by tag_id desc
limit 5;

select * from watchlist_tags
order by movie_id desc
limit 5;
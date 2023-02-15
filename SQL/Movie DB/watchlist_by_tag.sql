select 
	watchlist.title,
	group_concat(tag.tag_name) as tags
from watchlist 
left join watchlist_tags on watchlist.movie_id = watchlist_tags.movie_id
left join tag on watchlist_tags.tag_id = tag.tag_id
where not movie_status in ("Watched", "Hold")
and tag.tag_name = "Seagal"
group by watchlist.title
order by watchlist.movie_id asc
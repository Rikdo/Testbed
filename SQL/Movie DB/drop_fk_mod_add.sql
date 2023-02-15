Alter Table watchlist_tags drop foreign key fk_mt_tag;

ALTER TABLE tag MODIFY COLUMN tag_id INT NOT NULL AUTO_INCREMENT;

Alter Table watchlist_tags add CONSTRAINT fk_mt_tag FOREIGN KEY (tag_id) REFERENCES movies.tag (tag_id);
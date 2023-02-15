DELIMITER $$
CREATE PROCEDURE add_to_watchlist(
	MovieName NVARCHAR(50),
	TagName NVARCHAR(50))
BEGIN
	DECLARE MovieId INT;
	DECLARE TagId INT;

	SELECT MovieId = Movie_Id FROM Watchlist WHERE Title = MovieName;
	SELECT TagId = Tag_Id FROM Tag WHERE Tag_Name = TagName;

	IF MovieId IS NULL THEN
		INSERT INTO Watchlist VALUES(MovieName);
		SELECT MovieId = SCOPE_IDENTITY();
	END IF;

	IF TagId IS NULL THEN
		INSERT INTO Tag VALUES(TagName);
		SELECT TagId = SCOPE_IDENTITY();
	END IF;

	INSERT INTO Watchlist_Tags VALUES(MovieId, TagId);
END$$
DELIMITER ;
SELECT * FROM Book;
SELECT *  FROM USER;

SELECT * FROM BookInUserCollection;

-- INSERT INTO Awards(`Level`, Required_XP)
-- VALUES (0, 0);

INSERT INTO User(email, `Name`, XP, AwardProfile) 
VALUES ("a@gmail.com", "a", 0, 0);

UPDATE User 
SET XP = 450, AwardProfile = 3
WHERE Email = "a@gmail.com";

INSERT INTO Book(APIid, Title, Genre, Pages)
VALUES("000000000", "The Candle and the Flame", 
		"Fantasy", 416);

INSERT INTO Book(APIid,  Title, Genre, Pages)
VALUES("000000001", "The Selection", 
		"Dystopian", 336);

INSERT INTO Book(APIid, Title, Genre, Pages)
VALUES("000000002", "The Elite", 
		"Dystopian", 336);

INSERT INTO Book(APIid,  Title, Genre, Pages)
VALUES("000000003",  "The One", 
		"Dystopian", 336);

DELETE FROM BookInUserCollection WHERE ISBN = "000000003";

INSERT INTO Book(APIid, Title, Genre, Pages)
VALUES("000000004", "The Heir", 
		"Dystopian", 336);
                

INSERT INTO Book(APIid, Title, Genre, Pages)
VALUES("000000005", "The Crown", 
		"Dystopian", 336);

INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2023-03-07", "2023-03-04", 136, "000000000", 
		"a@gmail.com");

INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2023-03-05", "2023-03-02", 10, "000000001", 
		"a@gmail.com");
        
-- INSERT INTO BookInUserCollection(NewestReadingStartDate, 
-- 			NewestReadingEndDate, PagesRead, ISBN, email)
-- VALUES ("2023-03-02", "2023-03-03", 100, "000000000", 
-- 		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2023-03-01", "2023-03-08", 100, "000000002", 
		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2021-03-01", "2021-03-08", 50, "000000004", 
		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2021-03-01", "2021-03-08", 50, "000000005", 
		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, NumberOfTimesReread, PagesRead, ISBN, email)
VALUES ("2023-04-01", "2023-04-19", 5, 50, "000000003", 
		"a@gmail.com");
        
-- SELECT NewestReadingStartDate, NewestReadingEndDate, PagesRead 
-- 	FROM BookInUserCollection WHERE email = "a@gmail.com";
    
   --  INSERT INTO BookInUserCollection(UserRating, NewestReadingStartDate, 
-- 									NewestReadingEndDate, NumberOfTimesReread, 
--                                     PagesRead, ISBN, Email, ShelfName, CollectionID) 
-- 	VALUES()
    
-- SELECT C.NewestReadingEndDate, B.Genre 
-- FROM BookInUserCollection AS C, Book AS B 
-- WHERE C.email = "a@gmail.com"
-- AND B.ISBN = C.ISBN;

-- SELECT B.Title, C.NumberOfTimesReread
-- FROM BookInUserCollection AS C, Book AS B 
-- WHERE C.email = "a@gmail.com" 
-- AND B.ISBN = C.ISBN
-- AND C.NumberOfTimesReread > 1;


SELECT * FROM `User`;
SELECT * FROM auth_user; 
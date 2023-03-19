SELECT * FROM Book;
SELECT *  FROM USER;
SELECT * FROM Statistics;

SELECT * FROM BookInUserCollection;

-- INSERT INTO Awards(`Level`, Required_XP)
-- VALUES (0, 0);

INSERT INTO User(email, `Name`, XP, AwardProfile) 
VALUES ("a@gmail.com", "a", 0, 0);

UPDATE User 
SET XP = 450, AwardProfile = 3
WHERE Email = "a@gmail.com";

INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000000", "ebook", "The Candle and the Flame", 
		"Fantasy", 416);

INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000001", "Hardcover", "The Selection", 
		"Dystopian", 336);

INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000002", "Hardcover", "The Elite", 
		"Dystopian", 336);

INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000003", "Hardcover", "The One", 
		"Dystopian", 336);
        
INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000004", "Hardcover", "The Heir", 
		"Dystopian", 336);
                

INSERT INTO Book(ISBN, `Type`, Title, Genre, Pages)
VALUES("000000005", "Hardcover", "The Crown", 
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
        
SELECT NewestReadingStartDate, NewestReadingEndDate, PagesRead 
	FROM BookInUserCollection WHERE email = "a@gmail.com";
    
-- SELECT C.NewestReadingEndDate, B.Genre 
-- FROM BookInUserCollection AS C, Book AS B 
-- WHERE C.email = "a@gmail.com"
-- AND B.ISBN = C.ISBN;

-- SELECT B.Title, C.NumberOfTimesReread
-- FROM BookInUserCollection AS C, Book AS B 
-- WHERE C.email = "a@gmail.com" 
-- AND B.ISBN = C.ISBN
-- AND C.NumberOfTimesReread > 1;
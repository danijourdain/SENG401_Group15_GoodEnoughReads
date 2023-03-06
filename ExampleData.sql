SELECT * FROM Book;
SELECT * FROM USER;
SELECT * FROM Statistics;

SELECT * FROM BookInUserCollection;

INSERT INTO User(email, `Name`, `Password`) 
VALUES ("a@gmail.com", "a", "b");

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
VALUES ("2023-03-01", "2023-03-01", 100, "000000002", 
		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2021-03-01", "2021-03-01", 50, "000000004", 
		"a@gmail.com");
        
INSERT INTO BookInUserCollection(NewestReadingStartDate, 
			NewestReadingEndDate, PagesRead, ISBN, email)
VALUES ("2021-03-01", "2021-03-01", 50, "000000005", 
		"a@gmail.com");
        
SELECT NewestReadingStartDate, NewestReadingEndDate, PagesRead 
	FROM BookInUserCollection WHERE email = "a@gmail.com";
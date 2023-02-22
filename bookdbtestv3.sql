-- Good Enough Reads :)
DROP TABLE IF EXISTS `BookInUserCollection`;
DROP TABLE IF EXISTS `IsAPartOf`;
DROP TABLE IF EXISTS `Collection`;
DROP TABLE IF EXISTS `Shelf`;
DROP TABLE IF EXISTS `BookCase`;
DROP TABLE IF EXISTS `Statistics`;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `Awards`;
DROP TABLE IF EXISTS `WrittenBy`;
DROP TABLE IF EXISTS `Author`;
DROP TABLE IF EXISTS `Book`;


CREATE TABLE Awards (
  `Level` INT NOT NULL,
  `Image` VARCHAR(255),
  Required_XP INT NOT NULL,
  PRIMARY KEY (Level)
);


CREATE TABLE User (
  Email VARCHAR(255) BINARY,
  `Name` VARCHAR(255),
  ProfilePictureURL VARCHAR(255),
  `Password` VARCHAR(255),
  XP INT NOT NULL,
  AwardProfile INT NOT NULL,
  FOREIGN KEY (AwardProfile) REFERENCES Awards(`Level`),
  PRIMARY KEY (Email)
);


CREATE TABLE Author (
  `Name` VARCHAR(255),
  Genre VARCHAR(255),
  A_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (A_ID)
);


CREATE TABLE Book (
  ISBN VARCHAR(255),
  ImageURL VARCHAR(255),
  `Type` VARCHAR(255),
  Title VARCHAR(255),
  Genre VARCHAR(255),
  Pages INT NOT NULL,
  Rating INT,
  PRIMARY KEY (ISBN)
);


CREATE TABLE WrittenBy (
  BookISBN VARCHAR(255),
  AuthorID INT UNSIGNED NOT NULL,
  FOREIGN KEY (AuthorID) REFERENCES Author(A_ID),
  FOREIGN KEY (BookISBN) REFERENCES Book(ISBN),
  PRIMARY KEY (AuthorID, BookISBN)
);


CREATE TABLE BookCase (
  ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Colour VARCHAR(255),
  Email VARCHAR(255) BINARY,
  FOREIGN KEY (Email) REFERENCES User(Email),
  PRIMARY KEY (ID)
);


#Was previously called Bookshelf
CREATE TABLE Shelf (
  `Name` VARCHAR(255) BINARY,
  Colour VARCHAR(255) BINARY,
  Visibility VARCHAR(255) BINARY,
  PinnedShelfPosition INT UNSIGNED,
  Email VARCHAR(255) BINARY,
  BookCaseID INT UNSIGNED,
  FOREIGN KEY (Email) REFERENCES User(Email),
  FOREIGN KEY (BookCaseID) REFERENCES BookCase(ID),
  PRIMARY KEY (Name, Email, BookCaseID)
);


CREATE TABLE IsAPartOf (
  Position VARCHAR(255),
  BookISBN VARCHAR(255),
  ShelfName VARCHAR(255) BINARY,
  FOREIGN KEY (BookISBN) REFERENCES Book(ISBN),
  FOREIGN KEY (ShelfName) REFERENCES Shelf(`Name`),
  PRIMARY KEY (BookISBN, ShelfName)
);


CREATE TABLE Statistics (
  ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Email VARCHAR(255) BINARY,
  TotalPagesRead INT UNSIGNED,
  FOREIGN KEY (Email) REFERENCES User(Email),
  PRIMARY KEY (ID, Email)
);


CREATE TABLE Collection (
  ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(255) BINARY, 
  StatsID INT UNSIGNED NOT NULL,
  Email VARCHAR(255) BINARY,
  ShelfName VARCHAR(255) BINARY,
  FOREIGN KEY (StatsID) REFERENCES Statistics(ID),
  FOREIGN KEY (Email) REFERENCES User (Email),
  FOREIGN KEY (ShelfName, Email) REFERENCES Shelf (Name, Email),
  PRIMARY KEY (ID, Shelfname)
  
  ##From previous version of Collection
  #DateCreated DATE,
  #`Description` VARCHAR(255) BINARY,
  #FOREIGN KEY (BookshelfName, Email) REFERENCES Bookshelf (Name, Email),
);


CREATE TABLE BookInUserCollection (
  UserRating INT,
  #Format, unsure of variable type here
  NewestReadingStartDate DATE,
  NewestReadingEndDate DATE,
  NumberOfTimesReread INT UNSIGNED,
  PagesRead INT UNSIGNED, #Needs to be in ERD
  ISBN VARCHAR(255),
  Email VARCHAR(255) BINARY,
  
  ShelfName VARCHAR(255) BINARY,
  CollectionID INT UNSIGNED,
  
  FOREIGN KEY (ISBN) REFERENCES Book (ISBN),
  #FOREIGN KEY (ShelfName, Email) REFERENCES Shelf (Name, Email),
  FOREIGN KEY (CollectionID, ShelfName) REFERENCES Collection(ID, Shelfname),
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (ISBN, ShelfName, Email)
);
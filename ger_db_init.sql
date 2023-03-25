-- Good Enough Reads :)

DROP DATABASE IF EXISTS GER_DB;
CREATE DATABASE GER_DB;
USE GER_DB;

DROP USER 'ger'@'localhost';
FLUSH PRIVILEGES;
CREATE USER 'ger'@'localhost' IDENTIFIED BY 'seng';
GRANT ALL PRIVILEGES ON GER_DB.* TO 'ger'@'localhost';

DROP TABLE IF EXISTS `Awards`;
CREATE TABLE Awards (
  `Level` INT NOT NULL,
  Required_XP INT NOT NULL,
  PRIMARY KEY (Level)
);

DROP TABLE IF EXISTS `User`;
CREATE TABLE User (
  Email VARCHAR(255) BINARY,
  `Name` VARCHAR(255),
  XP INT NOT NULL,
  AwardProfile INT NOT NULL,
  FOREIGN KEY (AwardProfile) REFERENCES Awards(`Level`),
  PRIMARY KEY (Email)
);

DROP TABLE IF EXISTS `Collection`;
CREATE TABLE Collection (
  `Name` VARCHAR(255) BINARY, 
  Email VARCHAR(255) BINARY,
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (`Name`)
);

DROP TABLE IF EXISTS `Author`;
CREATE TABLE Author (
  `Name` VARCHAR(255),
  Genre VARCHAR(255),
  A_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (A_ID)
);

DROP TABLE IF EXISTS `Book`;
CREATE TABLE Book (
  APIid VARCHAR(255),
  ImageURL VARCHAR(255),
  Title VARCHAR(255),
  Genre VARCHAR(255),
  Pages INT NOT NULL,
  Rating FLOAT,
  PRIMARY KEY (APIid)
);

DROP TABLE IF EXISTS `WrittenBy`;
CREATE TABLE WrittenBy (
  BookISBN VARCHAR(255),
  AuthorID INT UNSIGNED NOT NULL,
  FOREIGN KEY (AuthorID) REFERENCES Author(A_ID),
  FOREIGN KEY (BookISBN) REFERENCES Book(APIid),
  PRIMARY KEY (AuthorID, BookISBN)
);

DROP TABLE IF EXISTS `BookInUserCollection`;
CREATE TABLE BookInUserCollection (
  UserRating INT,
  NewestReadingStartDate DATE,
  NewestReadingEndDate DATE,
  NumberOfTimesReread INT UNSIGNED,
  PagesRead INT UNSIGNED, -- Needs to be in ERD
  ISBN VARCHAR(255),
  shelfName VARCHAR(255) BINARY,
  Email VARCHAR(255) BINARY,
  CollectionID INT UNSIGNED,
  FOREIGN KEY (ISBN) REFERENCES Book(APIid),
  FOREIGN KEY (shelfName) REFERENCES Collection(`Name`),
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (ISBN, Email)
);

INSERT INTO `Awards` VALUES (0,0),(1,1000),(2,2000),(3,5000),(4,10000),(5,20000),(6,35000);
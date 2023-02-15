-- Good Enough Reads :)

CREATE TABLE User (
  Email VARCHAR(255) BINARY PRIMARY KEY,
  'Name' VARCHAR(255),
  ProfilePictureURL VARCHAR(255),
  'Password' VARCHAR(255),
  XP INT NOT NULL,
  AwardProfile INT NOT NULL,
  FOREIGN KEY (AwardProfile) REFERENCES Awards('Level')
);

CREATE TABLE Awards (
  'Level' INT NOT NULL,
  'Image' VARCHAR(255),
  Email VARCHAR(255) BINARY,
  Required_XP INT NOT NULL,
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (Level, Email)
);

CREATE TABLE Author (
  'Name' VARCHAR(255),
  Genre VARCHAR(255),
  A_ID INT NOT NULL AUTO_INCREMENT UNSIGNED PRIMARY KEY,
  PRIMARY KEY (A_ID)
);

CREATE TABLE Book (
  ISBN VARCHAR(255) PRIMARY KEY,
  ImageURL VARCHAR(255),
  Genre VARCHAR(255),
  'Type' VARCHAR(255),
  Pages INT NOT NULL,
  Title VARCHAR(255),
);

CREATE TABLE WrittenBy (
  BookISBN VARCHAR(255),
  AuthorID INT NOT NULL UNSIGNED,
  FOREIGN KEY (AuthorID) REFERENCES Author(A_ID),
  FOREIGN KEY (BookISBN) REFERENCES Book(ISBN),
  PRIMARY KEY (AuthorID, BookISBN)
);

CREATE TABLE IsAPartOf (
  Position VARCHAR(255),
  BookISBN VARCHAR(255),
  ShelfName VARCHAR(255),
  FOREIGN KEY (BookISBN) REFERENCES Book (ISBN),
  FOREIGN KEY (ShelfName) REFERENCES Shelf (Name),
  PRIMARY KEY (BookISBN, ShelfName)
);

CREATE TABLE BookCase (
  ID INT NOT NULL AUTO_INCREMENT UNSIGNED PRIMARY KEY,
  Colour VARCHAR(255),
  Email VARCHAR(255) BINARY,
  FOREIGN KEY (Email) REFERENCES User (Email)
);

CREATE TABLE Bookshelf (
  'Name' VARCHAR(255) BINARY,
  Visibility VARCHAR(255) BINARY,
  Colour VARCHAR(255) BINARY,
  PinnedShelfPosition INT UNSIGNED,
  Email VARCHAR(255) BINARY,
  BookCaseID INT UNSIGNED,
  FOREIGN KEY (BookCaseID) REFERENCES BookCase (ID),
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (Name, Email, BookCaseID)
);

CREATE TABLE Collection (
  'Name' VARCHAR(255) BINARY,
  DateCreated DATE,
  'Description' VARCHAR(255) BINARY,
  Email VARCHAR(255) BINARY,
  BookshelfName VARCHAR(255) BINARY,
  FOREIGN KEY (Email) REFERENCES User (Email),
  FOREIGN KEY (BookshelfName, Email) REFERENCES Bookshelf (Name, Email),
  PRIMARY KEY (Name, Email)
);

CREATE TABLE Statistics (
  ID INT UNSIGNED,
  'Name' VARCHAR(255) BINARY,
  Email VARCHAR(255) BINARY,
  TotalPagesRead INT UNSIGNED,
  FOREIGN KEY (Name, Email) REFERENCES Collection (Name, Email),
  PRIMARY KEY (ID, Name, Email)
);

CREATE TABLE BookInUserCollection (
  ISBN VARCHAR(255),
  BookshelfName VARCHAR(255) BINARY,
  Email VARCHAR(255) BINARY,
  UserRating INT,
  NewestReadingStartDate DATE,
  NewestReadingEndDate DATE,
  NumberOfTimesReread INT UNSIGNED,
  PagesRead INT UNSIGNED,
  FOREIGN KEY (ISBN) REFERENCES Book (ISBN),
  FOREIGN KEY (BookshelfName, Email) REFERENCES Bookshelf (Name, Email),
  FOREIGN KEY (Email) REFERENCES User (Email),
  PRIMARY KEY (ISBN, BookshelfName, Email)
);

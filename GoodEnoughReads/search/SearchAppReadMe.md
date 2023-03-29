# Search App/Service
This app/ service is created for the purpose of searching for a specific book, displaying that book, and submitting user related information related to that book. As such the search app deals with not only book information itself, but collections information since each book can be related to a user collection. Through this app a user may search for a book using the Google Books API, view the information for a specifically chosen book, add that book to a collection they wish after submitting the required information.

Classes/files: 
- BookModel: Preforms all database operations such as queries to retrive information, check tables, and deletes/inserts into the database specificially the Book and BookInUserCollection table. 
- viewsSearch.py: Is the controller of the app. Renders templates based on the specific function called by the template 
- urls.py: Controls what template is connected to what function so that the view knows what to do with the template information

Templates:
- bookDisplay.html: This html page renders the information for a specific book that the user has chosen after searching for a book. Information such as the title, author, publisher, and description are all displayed
- bookInfo: This html page is related to when a user wants to specifically add a book into their collection by clicking the 'add/edit shelf' button that is accessible through the bookDisplay page.
- search.js: This file takes user input and calls on the Google Books API to do a search related to the text input. As a result, multiple books are presented to the user which they can select from. 

**Note: This app is dependent on the collections app due because book deals with user specific collections in addition to individual books.**
 


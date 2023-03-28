# Collections App/Service
A collection entails a group of books that are related to some catagory. 

There are 4 types of specific collections:
1. Read: All books that a user has finished reading
2. ToRead: All books a user wishes to read but has not technically completed
3. Currently Reading: Books that a user is reading, but has not finished
4. DNF - Did Not Finish: Books that a user has attempted to read but has not finished and ended up dropping due to a variety of reasons. 

5. Collections-All: This is an additional shelf that holds all the books that the user has ever added across all 4 collections. 

This app/ service is created for the purpose of creating munipulating the collections shelves. Through this app a user may remove a book from a collection, update the status of a specific book and view additional information for that book that is not included in collections.


Classes/files: 
- CollectionModel: Preforms all database operations such as queries to retrive information, check tables, and deletes from the database
- Views.py: Is the controller of the app. Renders templates based on the specific function called by the template 
- urls.py: Controls what template is connected to what function so that the view knows what to do with the template information

Templates:
- There is a template (HTML) page for every collection that is required in additonal to an all books collection 
- toRead.js: This file takes the bookID (an APIid that which is the primary key of the googleBooksAPI) and does an API call specifically related to this key. This javascript file was created to purposely render a book display page that is not reliant on a user searching a book. This template will only be accessed through clcking the 'view book information' button that is found under every book in each collection page. 

**Note: This app is dependent on the search app due because collections deals with user specific collections in addition to individual books.**
 


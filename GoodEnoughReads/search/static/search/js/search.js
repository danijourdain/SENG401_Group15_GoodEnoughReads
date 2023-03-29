/**
 * This file was made by Ryan Mailhiot for Good Enough Reads. 
 * Date of final edit by Ryan was: March 28, 2023
 */

// Defining variables 
const search_box = document.querySelector("#search-box"); // This is the reference to the search box id tag in the HTML
var bookIndex = 0; // used for API index
var previousSearch = ""; // Used for resetting searches


function bookSearch(){
    // This function uses the google books API to search for books. What we have found is this information tends to be extremely unreliable
    // There is alot of fun and interesting things we need to do when it comes to dealing with this information.
    var search = search_box.value; // grabs the value at the search bar
    var cardResults = document.getElementById("results"); // grabs the results div
    var placeHldr = document.getElementById("placeholder").src; // Placeholder image
    var parsed = search.replace(" ", "-"); // removes spaces in the query
    // This block resets on a new search
    if (previousSearch != search){
        previousSearch = search;
        bookIndex = 0;
        cardResults.innerHTML = "";
    }
    console.log(parsed); 
    console.log(bookIndex);
    console.log(placeHldr);
    cardResults.innerHTML = cardResults.innerHTML + ""; 
    // This pings the google books api for search queries
    // Uses the parsed search data as well as the book index
    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=" + parsed + "&printType=books&maxResults=20&startIndex=" + bookIndex, 
        dataType: "json",
        type: 'get',
        success: function(data){
          console.log(data);  
          for(i = 0; i < data.items.length; i++){
                item = data.items[i];
                title1 = item.volumeInfo.title;
                author1 = item.volumeInfo.authors;
                publisher1 = item.volumeInfo.publisher;
                pageCount1 = item.volumeInfo.pageCount;
                bookID = item.id;
                desc = item.volumeInfo.description;
                rating = item.volumeInfo.averageRating;

                if (pageCount1 === undefined || pageCount1 === 0) { // Removes all 0 book queries
                    continue;
                }
                if (rating === undefined){ // changes ratings so it doesnt break in python later
                    rating = "unavailable";
                }

                
                bookImg1 = (item.volumeInfo.imageLinks) ? item.volumeInfo.imageLinks.thumbnail : placeHldr ;
                // Formats the output into a card that can be added
                cardResults.innerHTML += '<div class="row mt-4">' +
                                        formatOutput(bookImg1, title1, author1, publisher1, pageCount1, desc, rating, bookID) +
                                        '</div>';

            }
        },
        type: 'GET'
    });
    bookIndex += 20;
}

// Search buttons
document.getElementById("search-button").addEventListener('click', bookSearch, false)

// This is an intersection check to see if a hidden element is visible to auto reload
// There is a known bug that will auto run the googlebooksAPI call on page load. This is
// known but is considered an extremely low priority as it affects basically noone. 
// The functionality will be the same on the first user submission regardless.
const observer = new IntersectionObserver(entries => {
    const bottomReload = entries[0]
    if (!bottomReload.isIntersecting) {
        return
    }
    bookSearch()
}, {})

// This is the observe command
observer.observe(document.querySelector('.bottom-reload'))

// This is the format card that makes the search cards show up. 
function formatOutput(bookImg, title, author, publisher, pageCount, desc, rating, bookID) {
    // console.log(title + ""+ author +" "+ publisher +" "+ bookLink+" "+ bookImg)
    var htmlCard = `
  
        <div class="col-md-3">
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="row no-gutters">
              <div class="col-sm-4">
                <img src="${bookImg}" class="card-img" alt="${title}" width="120" height="240"></img>
              </div>
              <div class="col-sm-8">
                <div class="card-body">
                  <form action="/bookDisplay/" method="post">
                    <input type="text" name="title" value="${title}" hidden>
                    <input type="text" name="author" value="${author}" hidden>
                    <input type="text" name="publisher" value="${publisher}" hidden>
                    <input type="text" name="bookImg" value="${bookImg}" hidden>
                    <input type="text" name="pageCount" value="${pageCount}" hidden>
                    <input type="text" name="desc" value="${desc}" hidden>
                    <input type="text" name="rating" value="${rating}" hidden>
                    <input type="text" name="bookID" value="${bookID}" hidden>
                    <h5 class="card-title">${title}</h5>
                    <p class="card-text">Author: ${author}</p>
                    <p class="card-text">Publisher: ${publisher}</p>
                    <p class="card-text">Page Count: ${pageCount}</p>
                    <button type="submit" class="btn btn-primary">View Book</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3">
        </div>

    
    `
    return htmlCard;
}







// This will literally run the moment it is loaded, which is something we want. 
// This file will basically search for the hidden tag called "BookID" and then it will run a search based on that book alone.
// This way if we want any new information it can be separate from the search results. 

var volumeID = document.getElementById("bookID").getAttribute("value"); // Grabs the book id
console.log(volumeID);
var cardResults = document.getElementById("bookRead"); // This is the place where the html gets placed
var placeHldr = "{% static 'gersiteapp/img/placeholder.png' %}"; // Placeholder image
cardResults.innerHTML = "";
$.ajax({
    url: "https://www.googleapis.com/books/v1/volumes/" + volumeID, 
    dataType: "json",
    type: 'get',
    success: function(data){
        console.log(data);  
        title1 = data.volumeInfo.title;
        author1 = data.volumeInfo.authors;
        publisher1 = data.volumeInfo.publisher;
        pageCount1 = data.volumeInfo.pageCount;
        bookImg1 = (data.volumeInfo.imageLinks) ? data.volumeInfo.imageLinks.thumbnail : placeHldr ;
        desc = data.volumeInfo.description;
        rating = data.volumeInfo.averageRating;
        if (rating === undefined){ // changes ratings so it doesnt break it
          rating = "unavailable";
        }

        cardResults.innerHTML += formatOutput(bookImg1, title1, author1, publisher1, pageCount1, desc);

    },
    type: 'GET'
});

// This is the formatted HTML from before that now includes the information for the book
// Currently incomplete but working on that part
function formatOutput(bookImg, title, author, publisher, pageCount, desc) {
    // console.log(title + ""+ author +" "+ publisher +" "+ bookLink+" "+ bookImg)
    var htmlCard = `
    <div class="media">
        <img class= "align-self-start mr-3" src="${ bookImg }" style= "width: 30%; height: 100%; border-style: solid; 
              border-color: #004643; border-radius: 10px; border-width: 5px; margin: 5px 5px 5px 5px;">
      <div class="media-body" style="background-color: #84A98C; color:#004643; border-radius: 10px;
          border-style: solid; border-color:#004643; 
            border-radius: 10px; border-width: 5px; margin: 5px 5px 5px 5px; padding-bottom: 5px;">
            <div class="container">
              <div class="row" style="padding-left: 10px">
                <div class="col">
                  <h2>${ title }</h2>
                </div>
                <div class="col">
                  <h2>Rating: ${ rating }</h2>
              </div>
              </div>
              <div class="row" style="padding-left: 10px">
                <div class="col">
                  <h5>Author: ${ author }</h5>
                </div>
                <div class="col">
                  <h5>Publisher: ${ publisher }</h5>
                </div>
                <div class="col">
                  <h5>Pages: ${ pageCount }</h5>
                </div>
              </div>
              <div class="row" style="padding-left: 10px">
                Summary: ${ desc }
              </div>
          </div>
      </div>
    </div>
    `
    return htmlCard;
}


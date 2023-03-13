const search_box = document.querySelector("#search-box"); // This is the reference to the search box id tag in the HTML

function bookSearch(){
    var search = search_box.value;
    var cardResults = document.getElementById("results");
    var placeHldr = "{% static 'gersiteapp/img/placeholder.png' %}"; // Placeholder image
    search = search.replaceAll("/\s", "_");
    console.log(search);
    cardResults.innerHTML = "";
    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=-collection+intitle:" + search + "&printType=books&maxResults=20", 
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
                console.log(pageCount1);
                // bookLink1 = item.volumeInfo.previewLink;
                // bookIsbn = item.volumeInfo.industryIdentifiers[1].identifier
                bookImg1 = (item.volumeInfo.imageLinks) ? item.volumeInfo.imageLinks.thumbnail : placeHldr ;

                cardResults.innerHTML += '<div class="row mt-4">' +
                                        formatOutput(bookImg1, title1, author1, publisher1, pageCount1) +
                                        '</div>';

            }
        },
        type: 'GET'
    });
}

document.getElementById("search-button").addEventListener('click', bookSearch, false)
// document.addEventListener('keypress', function(e){
//   if (e.key === 'Enter')
//   {


    // 

//     <form action="bookDisplay" method="post">

//     bookSearch()

// </form>
//   }
// });


function formatOutput(bookImg, title, author, publisher, pageCount) {
    // console.log(title + ""+ author +" "+ publisher +" "+ bookLink+" "+ bookImg)
    var htmlCard = `
  
        <div class="col-md-3">
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="row no-gutters">
              <div class="col-sm-4">
                <img src="${bookImg}" class="card-img" alt="${title}" width="120" height="200"></img>
              </div>
              <div class="col-sm-8">
                <div class="card-body">
                  <form action="/bookDisplay/" method="post">
                    <input type="text" name="title" value="${title}" hidden>
                    <input type="text" name="author" value="${author}" hidden>
                    <input type="text" name="publisher" value="${publisher}" hidden>
                    <input type="text" name="bookImg" value="${bookImg}" hidden>
                    <input type="text" name="pageCount" value="${pageCount}" hidden>
                    <h5 class="card-title">${title}</h5>
                    <p class="card-text">Author: ${author}</p>
                    <p class="card-text">Publisher: ${publisher}</p>
                    <p class="card-text">Page Count: ${pageCount}</p>
                    <input type="submit" value="View Book">
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






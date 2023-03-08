const search_box = document.querySelector("#search-box"); // This is the reference to the search box id tag in the HTML

function bookSearch(){
    var search = search_box.value;
    var cardResults = document.getElementById("results");
    console.log(search);
    cardResults.innerHTML = "";
    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=" + search, 
        dataType: "json",
        type: 'get',
        success: function(data){
          console.log(data);  
          for(i = 0; i < data.items.length; i++){
                item = data.items[i];
                title1 = item.volumeInfo.title;
                author1 = item.volumeInfo.authors;
                publisher1 = item.volumeInfo.publisher;
                bookLink1 = item.volumeInfo.previewLink;
                bookIsbn = item.volumeInfo.industryIdentifiers[1].identifier
                bookImg1 = (item.volumeInfo.imageLinks) ? item.volumeInfo.imageLinks.thumbnail : placeHldr ;

                cardResults.innerHTML += '<div class="row mt-4">' +
                                        formatOutput(bookImg1, title1, author1, publisher1, bookLink1, bookIsbn) +
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
//     bookSearch()
//   }
// });


function formatOutput(bookImg, title, author, publisher, bookLink, bookIsbn) {
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
              <h5 class="card-title">${title}</h5>
              <p class="card-text">Author: ${author}</p>
              <p class="card-text">Publisher: ${publisher}</p>
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
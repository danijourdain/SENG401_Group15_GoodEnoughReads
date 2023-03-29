import unittest
from gersiteapp.views import get_book_genre
from gersiteapp.views import get_similar_books

class TestRecommendation(unittest.TestCase):

    #Tests the get_book_genre function when given a book title along with a known existing genre for the book to see if it returns correctly.
    def test_genre(self):
        genres = get_book_genre("The Ballad of Songbirds and Snakes")
        self.assertIn('Science fiction', genres)
    
    
    #Tests the get_book_genre function to properly return nothing when given gibberish search information.
    def test_invalid_title(self):
        genres = get_book_genre("hngwlibnqlijgkuwehgnla.sljngo;ilwsjgo;wie")
        self.assertEqual(genres, [])
    

    #Tests the get_similar_books function to make sure it properly returns 4 recommended book values when given valid information.
    def test_valid_input(self):
        genres = ['Science fiction']
        published_after = 2010
        similar_books = get_similar_books(genres, published_after)
        self.assertEqual(len(similar_books), 4)

if __name__ == '__main__':
    unittest.main()
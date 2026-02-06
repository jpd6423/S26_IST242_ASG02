"""
Testing library
""" 
import unittest
from unittest.mock import patch
from io import StringIO
#import our user made function for testing
from personal_library import(
    add_book,
    remove_book,
    list_book,
    search_book
)
#test class 
class TestPersonallibrary(unittest.TestCase):
    #test case for add book function
    def test_add_book_normal_case(self):
        library =[]
        with patch("builtins.input",return_value ="Dune"):
           add_book(library)
        
        self.assertEqual(library, ["Dune"])
    #test case for multiple books
    def test_list_more_than_one_book(self):
        library= ["Dune","Dune Messiah"]
        with patch("sys.stdout",new=StringIO()) as out:
            list_book(library)
            output = out.getvalue()
        self.assertIn("Dune", output)
        self.assertIn("Dune Messiah", output)
    #test remove book
    def test_remove_book(self):
        library =["book"]
        with patch("builtins.input", return_value="book"):
            remove_book(library)
        self.assertEqual(library,[])
    #test search function
    def test_search_book(self):
        library =["book"]
        with patch("builtins.input", return_value="book"):
            with patch("sys.stdout", new=StringIO()) as out:
                search_book(library)
            output = out.getvalue()
        self.assertIn("book",output)

      

    

#call the test class main method

if __name__ == "__main__":
    unittest.main()
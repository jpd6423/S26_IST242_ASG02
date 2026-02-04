"""
Author: Steve
"""

import unittest
from unittest.mock import patch
from io import StringIO

# Import our user-made functions for testing
from personal_library import ( 
    addBook,
    removeBook,
    listBooks,
    searchBooks
)

# Test class
class TestPersonalLibrary(unittest.TestCase):
    # Test case for addBook function
    def test_addBook_normalCase(self):
        library = []
        with patch("builtins.input", return_value='Dune'): # Pass a value to the system input
            addBook(library)
        self.assertEqual(library, ['Dune'])

    def test_listBook_listsMoreThanOneBook(self):
        library = ['Dune',"Dune Messiah"]
        with patch("sys.stdout", new=StringIO()) as out:
            listBooks(library)
            output = out.getvalue()
        self.assertIn('Dune', output)
        self.assertIn("Dune Messiah", output)

# Call the test class main method
if __name__ == "__main__":
    unittest.main()
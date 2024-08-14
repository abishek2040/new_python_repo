# A unit test verifies that one specific aspect of a function's behavior is correct;
# While a test case is a set of unit tests that verifies that a specific aspect of a function's behaviour is correct.

# Here's a test case with one function that verifies that the function, get_name() works correctly when given a first
# and a last name.

import unittest # First we import the unitest module which has all the tools to test a code.
from name_function import get_name

class NamesTestCase(unittest.TestCase):
    """Tests for the name_function.py"""

    def test_first_last(self):
        """Do names like janis joplin work? """
        formatted_name = get_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_middle(self):
        """"Do names like Gopal Prasad Phuyal work?"""""
        formatted_name = get_name('Gopal', 'Phuyal', 'Prasad')
        self.assertEqual(formatted_name, 'Gopal Prasad Phuyal')

if __name__ == '__main__':
    unittest.main()

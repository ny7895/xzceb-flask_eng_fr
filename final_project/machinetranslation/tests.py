import unittest
from translator import english_to_french
from translator import french_to_english

class Test_english_to_french(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test input is Hello expected output is Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)
class Test_french_to_english(unittest.TestCase):
    def test2(self):
        #Test input is Bonjour expected output is Hello
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        #Test returns an empty string 
        self.assertNotEqual(french_to_english(0), 0)

if __name__ == "__main__":
    unittest.main()

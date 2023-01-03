import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):
   
    def test_null_english_to_french(self):
        with self.assertRaises(Exception):
            english_to_french(None)

    def test_null_french_to_english(self):
        with self.assertRaises(Exception):
            french_to_english(None)

    def test_dog_english_to_french(self):
        self.assertEqual(english_to_french("dog"), "chien")
        self.assertNotEqual(english_to_french("dog"), "chien")

    def test_chien_french_to_english(self):
        self.assertEqual(french_to_english("chien"), "dog")
        self.assertNotEqual(french_to_english("chien"), "dog"

if __name__=="__main__":
    unittest.main()
    print('Passed All Tests')

import unittest
from homework_week3 import generate_phrase

# TESTS

class TestLengthCharacters(unittest.TestCase):


    #  Check it returns False if the characters list is shorter than phrase
    def test_short_characters_list(self):
        result = generate_phrase("cbacba", "aabbccc")
        self.assertFalse(result)

    #  Check it returns True if the characters list is longer than phrase
    def test_long_characters_list(self):
        result = generate_phrase("cbacbagfc", "aabbccc")
        self.assertTrue(result)

class TestSpecialCharacters(unittest.TestCase):

    #  Check it works with spaces -> returns True
    def test_space_characters_list(self):
        result = generate_phrase("ccba cba", "aabbccc")
        self.assertTrue(result)

    #  Check it works with capital letter -> returns False
    def test_capital_letters_characters_list(self):
        result = generate_phrase("ccba cba", "aabbCCc ")
        self.assertFalse(result)

    #  Check it works with symbols -> returns True
    def test_symbols_characters_list(self):
        result = generate_phrase("cCba Cba%", "a%abbCCc ")
        self.assertTrue(result)

    #  Check it works with numbers -> returns False
    def test_numbers_characters_list(self):
        result = generate_phrase("cC33ba Cba%", "a%a33bbCCc ")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

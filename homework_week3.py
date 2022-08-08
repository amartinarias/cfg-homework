"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
import itertools


def generate_phrase(characters, phrase):
    """
    The function checks if the characters from parameter "characters" could form the same as parameter phrase

    param characters: Str, any number of random characters, accepts, numbers, letters, symbols, spaces
    param phrase: Str, any number of  characters
    return: True/False
    """
    for permutation in itertools.permutations(characters):
        word = ''.join(permutation)
        short_word = word[0: len(phrase)]
        if short_word == phrase:
            return True
    else:
        return False


# Case 1, result = True
characters = "cbacbagfc"
phrase = "aabbccc"
print(generate_phrase(characters, phrase))

# Case 2, result = False
characters = "cbacba"
phrase = "aabbccc"
print(generate_phrase(characters, phrase))

# Case 3, result = True
characters = "ccba cba"
phrase = "aabbccc "
print(generate_phrase(characters, phrase))

# Case 4, result = False
characters = "ccba cba"
phrase = "aabbCCc "
print(generate_phrase(characters, phrase))

# Case 5, result = True
characters = "cCba Cba%"
phrase = "a%abbCCc "
print(generate_phrase(characters, phrase))

# Case 6, result = True
characters = "cC33ba Cba%"
phrase = "a%a33bbCCc "
print(generate_phrase(characters, phrase))


if __name__ == '__main__':
    generate_phrase(characters, phrase)

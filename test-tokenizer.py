import unittest
from collections import Counter
from tokenizer import *

class TestTokenizer(unittest.TestCase):

    text = "Processing text is weird, Weird -- weird!"
    list_of_words = ["a", "a", "b", "a", "b", "a"]
    list_of_some_nonwords = ["a", "'a'", ";", "!", "." "A!", "#a"]

    def testGetWords(self):
        """ Check that your get_words function works """

        self.assertEqual(get_tokens(self.text), ['Processing', 'text', 'is', 'weird,', 'Weird', '--', 'weird!'])
        self.assertEqual(get_tokens(self.text, do_lower=True), ['processing', 'text', 'is', 'weird,', 'weird', '--', 'weird!'])

    def testCountWords(self):
        """ Check that your count_words function works."""

        expected = Counter({'a': 4, 'b': 2})
        self.assertEqual(count_tokens(self.list_of_words), expected)

    def testWordsByFreq(self):
        """ Check that your words_by_frequency function works."""

        self.assertEqual(tokens_by_frequency(self.list_of_words), [('a', 4), ('b', 2)])
        self.assertEqual(tokens_by_frequency(self.list_of_words, n=1), [('a', 4)])

    def testTokenize(self):
        """ Check that your tokenize function works."""

        self.assertEqual(tokenize(self.text), ['Processing', 'text', 'is', 'weird', ',', 'Weird', '-', '-', 'weird', '!'])
        self.assertEqual(tokenize(self.text, do_lower=True), ['processing', 'text', 'is', 'weird', ',', 'weird', '-', '-', 'weird', '!'])

    def testFilterNonwords(self):
        """ Check that your filter_nonwords function works."""

        self.assertEqual(filter_nonwords(self.list_of_words), self.list_of_words)
        self.assertEqual(filter_nonwords(self.list_of_some_nonwords), ['a'])

if __name__ == '__main__':
    unittest.main()

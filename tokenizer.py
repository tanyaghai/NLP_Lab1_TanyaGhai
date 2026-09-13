#!/usr/bin/env python3

from collections import Counter
import os
import re 

def get_tokens(s, do_lower=False):
    if do_lower:
        s = s.lower()
    return s.split(' ')

def count_tokens(list_of_tokens):
    return Counter(list_of_tokens)

def tokens_by_frequency(list_of_tokens, n=None):
    counts = count_tokens(list_of_tokens)
    return counts.most_common(n)

def tokenize(s, do_lower=False):
    if do_lower:
        s = s.lower()

    s_adj = re.split(r'(\W)', s)
    tokens = []

    for token in s_adj:
        if token != '' and not token.isspace():
            tokens.append(token)
    return tokens

def filter_nonwords(list_of_tokens):
    words = []
    for token in list_of_tokens:
        if token.isalpha():
            words.append(token)
    return words

def main():
    """ All of your testing code should go in here. This code
    is only run if your program is run as an executable. If it
    is imported into another file, then this code will not run."""

    directory = '/courses/cs159/data/gutenberg/'
    files = os.listdir(directory)

    for file in files:
        if file.endswith('.txt'):
            infile = open(os.path.join(directory, file), 'r', encoding='latin1')
            text = infile.read()

            tokens = tokenize(text, do_lower=False)
            words = filter_nonwords(tokens)

            print(file, tokens_by_frequency(words, 5))


if __name__ == '__main__':
    main()

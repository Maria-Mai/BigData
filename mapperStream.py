#!/usr/bin/python

# example usage w/o hadoop: cat harryPotter.txt | python.exe mapperStream.py | sort | python.exe reducerStream.py
# example usage w hadoop: cat harryPotter.txt | python.exe mapperStream.py | python.exe reducerStream.py

from itertools import combinations
import sys
import re

# split text in input file into sentences
def read_input(file):
    file = re.sub(r'mr\.|mrs\.|ms\.', '', file.read())
    for sentence in re.split(r"[.?!]\s*", file):
        yield sentence

def main():
    data = read_input(sys.stdin)
    # return all possible combinations of keywords from the keyword.txt file
    keywords = list(combinations(open("keywords.txt", mode="r").read().split(), 2))
    for sentence in data:
        for keyword_pair in keywords:
            if ( (keyword_pair[0] in sentence) and (keyword_pair[1] in sentence) ):
                print '%s %s %s' % (keyword_pair[0], keyword_pair[1], 1)

if __name__ == "__main__":
    main()

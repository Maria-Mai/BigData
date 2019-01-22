# example usage w/o hadoop: cat harryPotter.txt | python.exe mapperStream.py | sort | python.exe reducerStream.py
# example usage w hadoop: cat harryPotter.txt | python.exe mapperStream.py | python.exe reducerStream.py


from itertools import combinations
import sys
import re

# split text in input file into sentences
def read_input(file):
    for sentence in re.split(r"[.?!]\s*", file.read()):
        yield sentence


def read_keywords(file):
    return list(combinations(file.readline().split(), 2))

def main():
    data = read_input(sys.stdin)
    keywords = read_keywords(open("keywords.txt", mode="r", encoding="UTF-8"))
    for sentence in data:
        for keyword_pair in keywords: # gets looped once
            if ( (keyword_pair[0] in sentence) and (keyword_pair[1] in sentence) ):
                print(keyword_pair[0], keyword_pair[1], 1)

if __name__ == "__main__":
    main()

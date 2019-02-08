#!/usr/bin/python

# example usage w/o hadoop: cat harryPotter.txt | python.exe mapperStream.py | sort | python.exe reducerStream.py
# example usage w hadoop: cat harryPotter.txt | python.exe mapperStream.py | python.exe reducerStream.py

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file):
    for line in file:
        yield line.split("\t")

def main():
    data = read_mapper_output(sys.stdin)
    for (keyword_1, keyword_2), group in groupby(data, itemgetter(0, 1)):
        total_count = sum(int(count) for keyword_1, keyword_2, count in group)
        print(keyword_1, keyword_2, total_count, sep="\t")

if __name__ == "__main__":
    main()

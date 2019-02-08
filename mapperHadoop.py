#coding=utf-8
from itertools import combinations
import re
import sys

formattedHarry = ""
for line in sys.stdin:
    uline = line.decode('utf-8')
    formattedHarry = formattedHarry +line

#open the preformatted text
#formattedHarry = open("formattedHarry.txt", mode="r", encoding="UTF-8").read()
#split it for every sentence into an array
formattedHarry = re.split(r'[.?!]\s*', formattedHarry) #7228 sätze

#character list of all characters that you want to look at later
characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge", "Vernon",
                 "Dudley", "Scabbers", "Petunia", "Ollivander", "Percy", "Gregory",
                 "Filch"]

#lowercase all characters
characterList = list(map(lambda x:x.lower(), characterList))
#create a list with all character pairs
character_pair_list = list(combinations(characterList,2))

#for every sentece look which character pairs are in it
for sentence in formattedHarry:
    for character_pair in character_pair_list:
        if((character_pair[0] in sentence) and (character_pair[1] in sentence)):
            print('%s\t%s\t%s' % (character_pair[0], character_pair[1], 1))

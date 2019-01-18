from itertools import combinations
import re

formattedHarry = open("formattedHarry.txt", mode="r", encoding="UTF-8").read()
formattedHarry = re.sub(r'mr\.|mrs\.|ms\.', '', formattedHarry)
formattedHarry = re.split(r'[.?!]\s*', formattedHarry) #7228 sätze

characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge", "Vernon",
                 "Dudley", "Scabbers", "Petunia", "Ollivander", "Percy", "Gregory",
                 "Filch"]

characterList = list(map(lambda x:x.lower(), characterList))

for sentence in formattedHarry:
    for character_pair in combinations(characterList,2):
        if((character_pair[0] in sentence) and (character_pair[1] in sentence)):
            print('%s\t%s\t%s' % (character_pair[0], character_pair[1], 1))
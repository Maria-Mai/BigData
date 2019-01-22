from itertools import combinations
import re

formattedHarry = open("formattedHarry.txt", mode="r", encoding="UTF-8").read()
formattedHarry = re.sub(r'mr\.|mrs\.|ms\.', '', formattedHarry)
formattedHarry = re.split(r'[.?!]\s*', formattedHarry)

characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge", "Vernon",
                 "Dudley", "Scabbers", "Petunia", "Ollivander", "Percy", "Gregory",
                 "Filch"]

characterList = list(map(lambda x: x.lower(), characterList))
allCharacterCombinations = list(combinations(characterList, 2))

# N - Anzahl der Sätze
n = len(formattedHarry)
# g - Anzahl der Gruppen
g = 5  

start = 0
for J in range(g):
    end = (J+1)*int(n/g) + J
    if (end > n):
        end = n-1
    for sentence in formattedHarry[start: end]:
        for characterCombination in allCharacterCombinations:
            if (characterCombination[0] in sentence and characterCombination[1] in sentence):
                print(characterCombination[0], characterCombination[1], 1)
    start = end + 1

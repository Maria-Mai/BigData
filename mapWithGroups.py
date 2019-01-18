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
allCharacterCombinations = list(combinations(characterList,2))

g = 1000
n = len(formattedHarry) # n = anzahl  sätze

#I = int(n/g) #anzahl gruppen (gerade 5)
#J = int(n/g) #anzahl gruppen (gerade 5)

# # keine Ahnung ob das so richtig ist, aber besser bekomm ich es nicht hin

#für alle sätze
#for sentence in formattedHarry:
#     #alle combos von I und J
#     for i in range(I):
#         for j in range(J):
#             #wenn paar in satz, dann ausgeben
#             for k in range(len(allCharacterCombinations)-1):
#                 if((i != j) and (allCharacterCombinations[k][0] in sentence) and (allCharacterCombinations[k][1] in sentence)):
#                     print((i, j), (sentence, allCharacterCombinations[k]))
                    
# Wir teilen unseren Datensatz (Bsp: Harry Potter - Stein der Weisen) mit n Sätzen (6137) in g Gruppen.
g = 5 # Anzahl der zur Verfügung stehenden Rechner

characterDictionary = {}

for characterCombination in allCharacterCombinations:
    characterDictionary[characterCombination] = 0

# print(characterDictionary)
# Laufvariable mit if(): break

"""
for J in range(g):
    for sentence in formattedHarry[ J*(int(n/g)) : (J+1)*int(n/g)-1 ]: # hier nochmal überprüfen
        for characterCombination in allCharacterCombinations:
            if (characterCombination[0] in sentence and characterCombination[1] in sentence):
                characterDictionary[characterCombination] += 1
    print("mapper / group:", J)
    print(characterDictionary)

print(characterDictionary)
"""
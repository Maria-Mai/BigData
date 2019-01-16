from itertools import combinations

formattedHarry = open("formattedHarry.txt", mode="r", encoding="UTF-8").read()
formattedHarry = formattedHarry.split(".") #6137 sätze #TODO  mr. mrs. entfernen und !? hinzufügen

characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville", "Luna",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge"]

characterList = list(map(lambda x:x.lower(), characterList))
allCharacterCombinations = list(combinations(characterList,2))

g = 1000
n = len(formattedHarry) # n = anzahl (6137) sätze

I = int(n/g) #anzahl gruppen (gerade 5)
J = int(n/g) #anzahl gruppen (gerade 5)

# keine Ahnung ob das so richtig ist, aber besser bekomm ich es nicht hin

#für alle sätze
for sentence in formattedHarry:
    #alle combos von I und J
    for i in range(I):
        for j in range(J):
            #wenn paar in satz, dann ausgeben
            for k in range(len(allCharacterCombinations)-1):
                if((i != j) and (allCharacterCombinations[k][0] in sentence) and (allCharacterCombinations[k][1] in sentence)):
                    print((i,j), (sentence, allCharacterCombinations[k]))
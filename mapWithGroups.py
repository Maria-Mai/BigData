from itertools import combinations

formattedHarry = open("formattedHarry.txt", mode="r", encoding="UTF-8").read()
formattedHarry = formattedHarry.split(".")

characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville", "Luna",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge"]

characterList = list(map(lambda x:x.lower(), characterList))

# Schlüsselpaar [i,j] wird ersetzt durch [I,J]. Teile n Charaktere in g Gruppen
# mit je n/g Charakterpaaren.
character_pairs = list(combinations(characterList, 2))

n = len(character_pairs) # 300
g = 5           
print(n/g)  # 60
for I in range(g):  
    for J in range(g):
        if (I is not J):
            print((I, J), (character_pairs[I]))
        else:
            continue




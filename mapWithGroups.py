from itertools import combinations

formattedHarry = open("formattedHarry.txt", "r").read()
formattedHarry = formattedHarry.split(".")

characterList = ["Harry", "Ron", "Hermione", "Ginny", "Neville", "Luna",
                 "James", "Lily", "Malfoy", "Hagrid", "Dumbledore", "Voldemort",
                 "Sirius", "Remus", "Bellatrix", "Snape", "McGonagall", "Fred", "George",
                 "Arthur", "Molly", "Bill", "Fleur", "Horace", "Umbridge"]

characterList = list(map(lambda x:x.lower(), characterList))

for sentence in formattedHarry:
    for character_pair in combinations(characterList,2):
        if((character_pair[0] in sentence) and (character_pair[1] in sentence)):
            print('%s\t%s\t%s' % (character_pair[0], character_pair[1], 1))


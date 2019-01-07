harryPotterBook = open("harryPotter.txt", "r")

newHarry = ""
for line in harryPotterBook:
    line = line.lower()
    line = line.strip()
    if("chapter" in line):
        pass
    else:
        newHarry = newHarry + line

#print(newHarry)
output = open("formattedHarry.txt", "w")
output.write(newHarry)
output.close()
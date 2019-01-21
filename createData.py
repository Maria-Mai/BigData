#import regular expressions
import re

#open the first harry potter book
harryPotterBook = open("harryPotter.txt", "r")

newHarry = ""
for line in harryPotterBook:
    #make the whole text lower case
    line = line.lower()
    #delete unnecessary characters
    line = line.strip()
    #delete mr. mrs. ms because of later split by "."
    line = re.sub(r'mr\.|mrs\.|ms\.', '', line)

    #delete all chapter names
    if("chapter" in line):
        pass
    else:
        #write everything into a new variable
        newHarry = newHarry + line

#save it to a file
output = open("formattedHarry.txt", "w")
output.write(newHarry)
output.close()
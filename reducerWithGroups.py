import sys

current_character_pair = ("","")
current_count = 0

# parse mapperWithGroups.py output
for line in sys.stdin:
    character1, character2, count = line.split()
    character_pair = (character1, character2)
    count = int(count)

    # after group by key, which is done by hadoop
    if(current_character_pair == character_pair):
        current_count += count
    else:
        if(current_character_pair):
            print(current_character_pair[0], current_character_pair[1], current_count)
        current_count = count
        current_character_pair = character_pair
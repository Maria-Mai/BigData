import sys

current_character_pair = None
current_count = 0
character_pair = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    character1, character2, count = line.split()

    try:
        #make a tuple of to characters
        character_pair = (character1,character2)
    except ValueError:
        continue

    try:
        count = int(count)
    except ValueError:
        continue

    # after group by key
    if(current_character_pair == character_pair):
        current_count += count
    else:
        #print the character pair and its number of occurence in the book
        if(current_character_pair):
            print('%s\t%s\t%d' % (current_character_pair[0], current_character_pair[1], current_count))
        current_count = count
        current_character_pair = character_pair

# do not forget to output the last character_pair if needed!
if(current_character_pair == character_pair):
    print('%s\t%s\t%d' % (current_character_pair[0], current_character_pair[1], current_count))
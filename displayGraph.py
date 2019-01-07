import networkx as nx
import matplotlib.pyplot as plot

outputData = open("outputData.txt", "r")

charList = []
countList = []

for line in outputData:
    character1, character2, count = line.split()

    try:
        character_pair = (character1,character2)
    except ValueError:
        continue

    try:
        count = int(count)
    except ValueError:
        continue

    if(count > 0):
        charList.append(character_pair)
        countList.append(count)

aGraph = nx.Graph()
aGraph.add_edges_from(charList)

nx.draw(aGraph,
        width=[(weight / 2) ** 0.5 for weight in countList],
        with_labels=True, edge_color="green",
        node_color="lightgrey",
        node_shape="o",
        font_size=10,
        font_color="black",
        alpha=0.9)

plot.show()
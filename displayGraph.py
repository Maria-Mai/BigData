import networkx as nx
import matplotlib.pyplot as plot

outputData = open("outputData.txt", "r")

characterWeightDict = {}

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
        characterWeightDict[character_pair] = count

aGraph = nx.Graph()

for characterWeight in characterWeightDict:
    print(characterWeightDict[characterWeight])
    aGraph.add_edge(characterWeight[0], characterWeight[1], color='green', weight=characterWeightDict[characterWeight]/20)

edges = aGraph.edges()
weights = [aGraph[u][v]['weight'] for u,v in edges]

pos = nx.circular_layout(aGraph)
nx.draw(aGraph, pos,
        width= weights,
        with_labels=True,
        node_color="lightgrey",
        node_shape="o",
        font_size=10,
        font_color="black",
        alpha=0.9)

plot.show()

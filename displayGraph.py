import networkx as nx
import matplotlib.pyplot as plot

#read the output data of the reducer
outputData = open("outputData.txt", "r")

#dictionary for the characters and their occurence number
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

#create a graph
aGraph = nx.Graph()

#add the occurence number (weight) and the edges to the graph
for characterWeight in characterWeightDict:
    aGraph.add_edge(characterWeight[0], characterWeight[1], color='green', weight=characterWeightDict[characterWeight]/20)

#get the edges
edges = aGraph.edges()
#get the weights
weights = [aGraph[u][v]['weight'] for u,v in edges]

#create the graph layout
pos = nx.circular_layout(aGraph)
nx.draw(aGraph, pos,
        width= weights,
        with_labels=True,
        node_color="lightgrey",
        node_shape="o",
        font_size=10,
        font_color="black",
        alpha=0.9)

#show the graph
plot.show()

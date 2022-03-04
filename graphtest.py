import networkx as nx
import matplotlib.pyplot as plt
import json
import math

f = open('graph.json')
data = json.load(f)
G = nx.DiGraph()

for i in data:
	for j in data[i]:
		if i!=j: #don't add self-loops
			G.add_edge(i, j)

max = 0
inconsistencies = 0
degreesList = []
clusteringList = []
closenessList = []

for i in data:
	#create data for degree histogram
	try:
		if max < G.degree[i]:
			max = G.degree[i]
		degreesList.append(G.degree[i])
	except KeyError:
		inconsistencies += 1
		print("Attempted to add edge to deleted user")

	#create data for clustering
	try:
		if type(nx.clustering(G,i))==int or type(nx.clustering(G,i))==float:
			clusteringList.append(nx.clustering(G, i))
		else:
			print("Problem with ", i)
	except TypeError:
		print("problem with ", i)

	#create data for Closeness centrality
	try:
		closenessList.append(nx.closeness_centrality(G, i))
	except:
		print("problem")

#Uncomment to see Clustering Coefficient Distribution
#plt.hist(clusteringList, bins = math.floor(len(data)/3))
#plt.title("Clustering Coefficient Histogram\nTotal Clustering Coefficient for G: .061415")
#plt.xlabel("Clustering Coefficient")
#plt.ylabel("Nodes")

#Uncomment to see Closeness Centrality Histogram
#plt.hist(closenessList, bins = math.floor(len(data)/3))
#plt.title("Closeness Centrality Histogram")
#plt.xlabel("Closeness Centrality")
#plt.ylabel("Nodes")

#Uncomment to see Degree Distribution Histogram
plt.hist(degreesList, bins=max)
plt.title("Degree Distribution Histogram")
plt.xlabel("Degree")
plt.ylabel("Nodes")

#Uncomment to see directed graph
#nx.draw(G)

plt.show()

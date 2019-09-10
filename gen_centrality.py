import snap

# Taking input from text file 
G1 = snap.LoadEdgeList(snap.PUNGraph,"/home/vedant/Social_computing/Social_Epinions/soc-Epinions1.txt",0,1)
G2 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Citation_network/Cit-HepPh.txt", 0, 1)
G3 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Enron_email_network/Email-Enron.txt", 0, 1)
G4 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/P2P_gutella_network/p2p-Gnutella04.txt", 0, 1)

#Taking Input of which sub graph to proceed
 
sub_graph_name = raw_input("Enter the name of subgraph ")

#### Task 2

### Task 2.1

# Creating the subgraph 1
# Creating a new list with taking odd edges
list1 = []

for i in G1.Nodes():
	node = i.GetId()
	if(node%2!=0):
		list1.append(node)

# Making it a set
list1 = set(list1)
list1 = list(list1)

v1 = snap.TIntV()

# Defining the snap vector
for i in range(len(list1)):
	v1.Add(list1[i])

# Creating the subgraph
soc_epinions1_subgraph = snap.GetSubGraph(G1,v1)

## Creating the subgraph 2
# Creating a new list with taking even edges
list2 = []

for i in G2.Nodes():
	node = i.GetId()
	if(node%2==0):
		list2.append(node)

# Making it a set
list2 = set(list2)
list2 = list(list2)

v2 = snap.TIntV()

# Defining the snap vector
for i in range(len(list2)):
	v2.Add(list2[i])

# Creating the subgraph
cit_heph_subgraph = snap.GetSubGraph(G2,v2)

## Creating the subgraph 3
# Creating a new list with taking  edges multiple of 3
list3 = []

for i in G3.Nodes():
	node = i.GetId()
	if(node%3==0):
		list3.append(node)

# Making it a set
list3 = set(list3)
list3 = list(list3)

v3 = snap.TIntV()

# Defining the snap vector
for i in range(len(list3)):
	v3.Add(list3[i])

# Creating the subgraph
email_enron_subgraph = snap.GetSubGraph(G3,v3)

## Creating the subgraph 4
list4=[]
for i in G4.Nodes():
	node = i.GetId()
	list4.append(node)

# Making it a set
list4 = set(list4)
list4 = list(list4)

v4 = snap.TIntV()

# Defining the snap vector
for i in range(len(list4)):
	v4.Add(list4[i])

p2p_gnutella04_subgraph = G4


## Calculating Degree centrality
'''
file1 = open("soc-Epinions1-subgraph-degree-centraility.txt","w+") 

file1.write("NodeId CentralityValue")
for j in soc_epinions1_subgraph.Nodes():
	node_id = j.GetId()
	degree=0
	for i in soc_epinions1_subgraph.Edges():
		if((i.GetSrcNId() == node_id) or (i.GetDstNId() == node_id)):
			degree = degree + 1
	file1.write(str(node_id) + " " + str(degree) + "\n")

file2 = open("cit-HepPh-subgraph-degree-centraility.txt","w+") 
count =0
file2.write("NodeId CentralityValue")
for j in cit_heph_subgraph.Nodes():
	node_id = j.GetId()
	degree=0
	count = count +1
	print count
	for i in cit_heph_subgraph.Edges():
		if((i.GetSrcNId() == node_id) or (i.GetDstNId() == node_id)):
			degree = degree + 1
	file2.write(str(node_id) + " " + str(degree) + "\n")

'''
file3 = open("email-Enron-subgraph-degree-centraility.txt","w+") 
count =0
file3.write("NodeId CentralityValue")
for j in email_enron_subgraph.Nodes():
	node_id = j.GetId()
	degree=0
	count = count + 1
	print count
	for i in email_enron_subgraph.Edges():
		if((i.GetSrcNId() == node_id) or (i.GetDstNId() == node_id)):
			degree = degree + 1
	file3.write(str(node_id) + " " + str(degree) + "\n")

file4 = open("p2p-Gnutella04-subgraph-degree-centraility.txt","w+") 
count =0
file4.write("NodeId CentralityValue")
for j in p2p_gnutella04_subgraph.Nodes():
	node_id = j.GetId()
	degree=0
	count = count + 1
	print count
	for i in p2p_gnutella04_subgraph.Edges():
		if((i.GetSrcNId() == node_id) or (i.GetDstNId() == node_id)):
			degree = degree + 1
	file4.write(str(node_id) + " " + str(degree) + "\n")

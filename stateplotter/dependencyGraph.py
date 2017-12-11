import networkx as nx
import matplotlib.pyplot as plt


def initiate_graph():
    return nx.DiGraph()
    

def create_node(graph, task):
    graph.add_node(task) # Add name as attribute?


def connect(graph , src, dest):
    graph.add_edge(src, dest)


G = initiate_graph()
H = initiate_graph()
print(G.number_of_nodes())
print(H.number_of_nodes())
create_node(G,"T1")
create_node(G,"T2")
create_node(G,"T3")
print(G.number_of_nodes())
print(H.number_of_nodes())
connect(G,"T1","T2")
connect(G,"T3","T1")

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

import networkx as nx
import matplotlib.pyplot as plt


def initiate_graph():
    return nx.DiGraph()
    

def create_node(graph, task):
    graph.add_node(task) # Add name as attribute?


def connect(graph , src, dest):
    graph.add_edge(src, dest)


def deadlock_detection(graph):
    L = list(nx.simple_cycles(graph))
    nr = len(L)
    if nr == 0:
       print('apa')
       return False
    return True

def graph_from_state(graph, state):
    sema_holders = {}
    for sema in state.semaphores:
        sema_holders[sema] = []
        for t in state.tasks:
            if sema in t.heldSemaphores:
                sema_holders[sema].append(t)

    for t in state.tasks:
        for sem in t.requestedSemaphores:
            for holder in sema_holders[sem]:
                graph.add_edge(t, holder)
 

# G = initiate_graph()
# H = initiate_graph()
# print(G.number_of_nodes())
# print(H.number_of_nodes())
# create_node(G,"T1")
# create_node(G,"T2")
# create_node(G,"T3")
# print(G.number_of_nodes())
# print(H.number_of_nodes())
# connect(G,"T1","T2")
# connect(G,"T3","T1")

edges = [ (0, 1), (1, 2), (2, 3), (3, 0),(2,4),(4,3),(2,0)]
edges = [ (0, 1), (1, 2), (2, 3), (3, 4),(4,5),(5,0),(2,4)]
edges = [ ('a', 'b'), ('b', 'c'), ('c', 'd')]
G = nx.DiGraph(edges)
L = deadlock_detection(G)
l = list(nx.simple_cycles(G))

# kalle = {'apa': 5}
# kalle['hast'] = []
# kalle['hast'].append('ja')
# print(kalle)

# print(len(L))
# print(len(l))

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

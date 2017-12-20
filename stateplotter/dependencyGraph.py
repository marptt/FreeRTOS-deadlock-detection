import networkx as nx
import matplotlib.pyplot as plt

def check_for_deadlock(state):
    G = nx.DiGraph()
    graph_from_state(G, state)
    return deadlock_detection(G), G

def deadlock_detection(graph):
    L = list(nx.simple_cycles(graph))
    nr = len(L)
    if nr == 0:
       return False
    return True

def graph_from_state(graph, state):
    sema_holders = {}
    sema_ored = []
    
    for sema in state.semaphores:
        sema_holders[sema] = []
        for t in state.tasks:
            if sema in t.heldSemaphores:
                sema_holders[sema].append(t)

    for t in state.tasks:
        for sem in t.requestedSemaphores:
            if len(sema_holders[sem])==1:
                graph.add_edge(t.taskName, sema_holders[sem][0].taskName)
            else:
                orText = 'OR-{}'.format(sem)
                graph.add_edge(t.taskName, orText)
                if sem not in sema_ored:
                    for holder in sema_holders[sem]:
                        graph.add_edge(orText, holder)
                    sema_ored.append(sem)

def show_dependency_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


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

# edges = [ (0, 1), (1, 2), (2, 3), (3, 0),(2,4),(4,3),(2,0)]
# edges = [ (0, 1), (1, 2), (2, 3), (3, 4),(4,5),(5,0),(2,4)]
# edges = [ ('a', 'b'), ('b', 'c'), ('c', 'd')]
# G = nx.DiGraph(edges)
# L = deadlock_detection(G)
# l = list(nx.simple_cycles(G))

# kalle = {'apa': 5}
# kalle['hast'] = []
# kalle['hast'].append('ja')
# print(kalle)

# print(len(L))
# print(len(l))

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


'''
load_graph takes a string name and returns the graph corresponding to the
input network's name
'''
def load_graph(nw_name):
    path = './data/cit-' + nw_name + '/out.cit-' + nw_name
    G = nx.read_edgelist(path, comments='%', create_using=nx.DiGraph())
    return G


'''
gets a list of tuples of node ids and count of neighbors sorted by
neighbor count with highest at the front of the returned list
'''
def degree_top_k(G, k):
    if (k <= 0):
        return 'please use k>0'

    return sorted(G.degree_iter(),key=itemgetter(1),reverse=True)[:k]


'''
gets a list of node ids sorted by neighbor count with nodes
with highest count at the front of the returned lists

Returns a list of integer ids
'''
def degree_top_k_ids(G, k):
    if (k <= 0):
        return 'please use k>0'

    top_tups = degree_top_k(G, k)
    return [int(tup[0]) for tup in top_tups]

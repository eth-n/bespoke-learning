import networkx as nx
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
gets a list of tuples of node ids and count of neighbors sorted hi-lo by
in-degree count
'''
def in_degree_top_k(G, k):
    if (k <= 0):
        print('please use k>0')
        return

    descending = sorted(G.in_degree().items(), key=itemgetter(1), reverse=True)
    k = min(k, len(descending))
    return descending[:k]


'''
gets a list of tuples of node ids and count of neighbors sorted hi-lo by
out-degree
'''
def out_degree_top_k(G, k):
    if (k <= 0):
        print('please use k>0')
        return

    descending = sorted(G.out_degree().items(), key=itemgetter(1), reverse=True)
    k = min(k, len(descending))
    return descending[:k]

'''
gets a list of node ids sorted by neighbor count with nodes
with highest count at the front of the returned lists

Returns a list of integer ids
'''
def in_degree_top_k_ids(G, k):
    if (k <= 0):
        print('please use k>0')
        return

    top_tups = in_degree_top_k(G, k)
    return [int(tup[0]) for tup in top_tups]


'''
gets a list of node ids sorted by neighbor count with nodes
with highest count at the front of the returned lists

Returns a list of integer ids
'''
def out_degree_top_k_ids(G, k):
    if (k <= 0):
        print('please use k>0')
        return

    top_tups = out_degree_top_k(G, k)
    return [int(tup[0]) for tup in top_tups]

import networkx as nx
import matplotlib.pyplot as plt

import shared


'''
cumulative count of distinct nodes that cite the top k most cited papers
in the graph
'''
def distinct_reachable(G, k):
    if (k <= 0):
        return 'please use k>0'

    G_r = nx.DiGraph.reverse(G)
    top_ids = shared.degree_top_k_ids(G, k)

    distinct_nodes = set()
    k_steps = []

    for id in top_ids:
        papers_citing_id = G_r.neighbors(str(id))
        for paper in papers_citing_id:
            distinct_nodes.add(paper)
        k_steps.append(len(distinct_nodes))

    return k_steps


'''
Functions for graphing k high citation papers vs inbound edges from distinct
nodes
'''
def graph_distinct_reachable(G, k=10):
    if isinstance(k, list):
        for k_val in k:
            y = distinct_reachable(G, k_val)
            x = [n for n in range(1, k_val+1)]
            plt.bar(x, y)
            plt.title('Papers Citing any of Top-K Most Cited')
            plt.xlabel('K')
            plt.ylabel('Distinct Citers')
            plt.savefig('reachable_'+str(k_val)+'.png')
    else:
        y = distinct_reachable(G, k)
        x = [n for n in range(1, k+1)]
        plt.bar(x, y)
        plt.title('Papers Citing any of Top-K Most Cited')
        plt.xlabel('K')
        plt.ylabel('Distinct Citers')
        plt.savefig('reachable_'+str(k)+'.png')


def graph_distinct_reachable_fraction(G, k=10):
    num_nodes = G.order()
    if isinstance(k, list):
        for k_val in k:
            y = [count/num_nodes for count in distinct_reachable(G, k_val)]
            x = [n for n in range(1, k_val+1)]
            plt.bar(x, y)
            plt.title('Fraction of Papers Citing any of Top-K Most Cited')
            plt.xlabel('K')
            plt.ylabel('Fraction of Papers')
            plt.savefig('frac_reachable_'+str(k_val)+'.png')
    else:
        y = [count/num_nodes for count in distinct_reachable(G, k_val)]
        x = [n for n in range(1, k+1)]
        plt.bar(x, y)
        plt.title('Fraction of Papers Citing any of Top-K Most Cited')
        plt.xlabel('K')
        plt.ylabel('Fraction of Papers')
        plt.savefig('frac_reachable_'+str(k)+'.png')


G = shared.load_graph('HepPh')
print(nx.info(G))
# print(distinct_reachable(G, 10))
# graph_distinct_reachable_fraction(G, [10, 50, 100, 1000]) #, G.order()])

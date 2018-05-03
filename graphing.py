import networkx as nx
import matplotlib.pyplot as plt

import base
import shared


'''
Functions for graphing k high citation papers vs inbound edges from distinct
nodes
'''
def graph_distinct_citers(G, k=10):
    if isinstance(k, int):
        k = [k]
    for k_val in k:
        y = base.distinct_citers(G, k_val)
        x = [n for n in range(1, k_val+1)]
        plt.bar(x, y)
        plt.title('Distinct Papers Citing any of Top-K Most Cited')
        plt.xlabel('K')
        plt.ylabel('Distinct Citers')
        plt.savefig('citers_'+str(k_val)+'.png')


def graph_distinct_citers_fraction(G, k=10):
    num_nodes = G.order()
    if isinstance(k, int):
        k = [k]
    for k_val in k:
        y = [count/num_nodes for count in base.distinct_citers(G, k_val)]
        x = [n for n in range(1, k_val+1)]
        plt.bar(x, y)
        plt.title('Fraction of Papers Citing any of Top-K Most Cited')
        plt.xlabel('K')
        plt.ylabel('Fraction of Papers')
        plt.savefig('frac_citers_'+str(k_val)+'.png')


def graph_distinct_cited(G, k=10):
    if isinstance(k, int):
        k = [k]
    for k_val in k:
        y = base.distinct_cited(G, k_val)
        x = [n for n in range(1, k_val+1)]
        plt.bar(x, y)
        plt.title('Distinct Papers Cited by any of Top-K Papers with Most References')
        plt.xlabel('K')
        plt.ylabel('Distinct Cited')
        plt.savefig('cited_'+str(k_val)+'.png')


def graph_distinct_cited_fraction(G, k=10):
    num_nodes = G.order()
    if isinstance(k, int):
        k = [k]
    for k_val in k:
        y = [count/num_nodes for count in base.distinct_cited(G, k_val)]
        x = [n for n in range(1, k_val+1)]
        plt.bar(x, y)
        plt.title('Fraction of Papers Papers Cited by any of Top-K Papers with Most Teferences')
        plt.xlabel('K')
        plt.ylabel('Fraction of Cited')
        plt.savefig('frac_cited_'+str(k_val)+'.png')


G = shared.load_graph('HepTh')
print(nx.info(G))

graph_distinct_cited_fraction(G, [10, 50, 100, 1000, G.order()])

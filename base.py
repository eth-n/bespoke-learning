import networkx as nx

import shared


'''
cumulative count of distinct nodes that cite the top k most cited papers
in G
'''
def distinct_citers(G, k):
    top_ids = shared.in_degree_top_k_ids(G, k)

    distinct_nodes = set()
    k_steps = []

    for id in top_ids:
        papers_citing_id = G.predecessors(str(id))
        for paper in papers_citing_id:
            distinct_nodes.add(paper)
        k_steps.append(len(distinct_nodes))

    return k_steps


'''
cumulative count of distinct nodes that are cited by the top k papers with
the most citations in G
'''
def distinct_cited(G, k):
    top_ids = shared.out_degree_top_k_ids(G, k)

    distinct_nodes = set()
    k_steps = []

    for id in top_ids:
        papers_citing_id = G.successors(str(id))
        for paper in papers_citing_id:
            distinct_nodes.add(paper)
        k_steps.append(len(distinct_nodes))

    return k_steps

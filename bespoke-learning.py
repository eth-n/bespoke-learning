import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

import shared


'''
Do all roads lead to Rome? Do wide BestFS runs go to any of the k most cited
papers in any citation network?

In graph G, run BFS from the start node, only enqueuing the top-b nodes by
Katz centrality. Don't enqueue any neighbors of a top-k most cited paper.
Also terminate after 'depth' iterations in case there are centrality loops.

I do not know if these are reasonable assumptions. I really hope they are.
'''
def skinny_bfs(G, start, b, k, depth, centrality_dict):
    top_k_ids = set(shared.degree_top_k_ids(G, k))

    marked = set()
    q = deque()
    q.append(int(start))
    marked.add(int(start))

    for iteration in range(depth):
        if len(q) == 0:
            return marked

        current = q.popleft()

        if current in top_k_ids:
            pass
        else:
            neighbors = [(n, centrality_dict[n])
                         for n in G.neighbors(str(current))]
            best_neighbors = sorted(neighbors,
                                    key=lambda tup: tup[1],
                                    reverse=True)
            best_neighbor_ids = [int(tup[0]) for tup in best_neighbors]

            to_add = min(len(neighbors), b)


            # Always try to add b neighbors with the while loop conditions
            # Might not be the right choice?
            idx = 0

            while idx < len(best_neighbor_ids) and to_add > 0:
                if best_neighbor_ids[idx] not in marked:
                    q.append(best_neighbor_ids[idx])
                    marked.add(best_neighbor_ids[idx])
                    to_add -= 1
                idx += 1

    # marked now contains all the verticies on this skinny BFS/wide DFS
    return marked


'''
Extract the subgraph of all vertices in set V from the original graph G
'''
def build_reading_graph(G, V):
    print(list(V))
    for n in V:
        print(G.has_node(n))
    H = G.subgraph(list(V))
    print(nx.info(H))
    return H


'''
Draw the graph with nx... pretty bad.
'''
def draw_write_graph(G, paper_id):
    limits=plt.axis('off') # turn of axes
    figure = plt.figure()
    plt.title('Bespoke Learning Goal for Paper id'+str(paper_id))
    nx.draw_shell(G)
    figure.savefig(str(paper_id)+'_learning_goal.png')


'''
Write the graph as something Gephi can open
'''
def write_graph_file(G, fname):
    nx.write_graphml(G, fname+'.graphml')


G = shared.load_graph('HepPh')
print(nx.info(G))

# print(G.neighbors('100'))
#
# centrality = nx.katz_centrality(G)
# print('centralities computed')
#
# marked_vertex_ids = skinny_bfs(G,
#                              start='100',
#                              b=5,
#                              k=50,
#                              depth=10,
#                              centrality_dict=centrality)
# print(marked_vertex_ids)
# print(len(marked_vertex_ids))
#
# marked_vertices = [str(id) for id in marked_vertex_ids]
#
# print(nx.info(G))
# H = build_reading_graph(G, marked_vertices)
# print(nx.info(H))
# draw_write_graph(H, 100)
# write_graph_file(H, '100')

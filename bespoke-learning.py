import networkx as nx
from collections import deque
import matplotlib.pyplot as plt
from collections import Counter
import time
import random

import shared


'''
Do all roads lead to Rome? Do wide BestFS runs go to any of the k most cited
papers in any citation network?

In graph G, run BFS from the start node, only enqueuing the top-b nodes by
Katz centrality. Don't enqueue any neighbors of a top-k most cited paper.
Also terminate after 'depth' iterations in case there are centrality loops.

I do not know if these are reasonable assumptions. I really hope they are.
'''
def skinny_bfs(G, start, b, k, centrality_dict):
    top_k_ids = set(shared.degree_top_k_ids(G, k))

    marked = set()
    q = deque()
    q.append(int(start))
    marked.add(int(start))

    # for iteration in range(depth):
    while len(q):
        # if len(q) == 0:
        #     return marked

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
    marked -= top_k_ids
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

# centrality = nx.katz_centrality(G)
centrality = nx.eigenvector_centrality_numpy(G)
print('centralities computed')

random_ids = [4165, 18338, 25568, 1315, 328, 27062, 19402, 12068, 22210, 4132,
              6720, 17937, 7801, 7535, 26318, 22904, 16031, 8597, 11193, 4358]

dag_sizes = []

start_time = time.time()

random.seed(42)

total_count = 1000

for node_id in range(1, total_count+1):
    marked_vertex_ids = skinny_bfs(G,
                             start=str(random.randint(1, G.order())),
                             b=3,
                             k=50,
                             centrality_dict=centrality)
    # print(marked_vertex_ids)
    # print(len(marked_vertex_ids))
    dag_sizes.append(len(marked_vertex_ids))

c = Counter(dag_sizes)

max_dag_size = max(dag_sizes)

# y = [c[n] for n in range(200)]
# x = [n for n in range(200)]
# plt.bar(x, y)
# plt.title('DAG Size Distribution')
# plt.xlabel('DAG Size (excl. base nodes)')
# plt.ylabel('Occurences')
# plt.savefig('dag-sizes.png')
#
# plt.clf()

y = []
x = [n for n in range(120+1)]

sum = 0
target = 0.05

for n in range(120+1):
    sum += c[n]
    y.append(sum/total_count)
    if sum/total_count >= target:
        print(n, target)
        target += 0.05
        while sum/total_count > target:
            target += 0.05

print(sum)

plt.bar(x, y)
plt.minorticks_on()
plt.grid(b=True, which='both', axis='both')
plt.title('Cumulative Fraction of DAG Size Distribution for hep-ph')
plt.xlabel('Largest DAG size included in cumulative sum')
plt.ylabel('Fraction of papers')
plt.savefig('ph-cmltv-dag-sizes.png')

print(c)
print(time.time() - start_time)

# marked_vertices = [str(id) for id in marked_vertex_ids]
#
# print(nx.info(G))
# H = build_reading_graph(G, marked_vertices)
# print(nx.info(H))
# draw_write_graph(H, 100)
# write_graph_file(H, '100')

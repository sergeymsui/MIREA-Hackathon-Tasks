
from collections import defaultdict

# (u, v, weight)
graph = [
    [1, 2, 7],
    [1, 3, 9],
    [1, 6, 14],
    [2, 4, 15],
    [2, 3, 10],
    [3, 4, 11],
    [3, 6, 2],
    [5, 6, 9],
    [4, 5, 6],
]

def dijkstra_path():
    n = len(graph)

    mdict = defaultdict(list)
    for (u, v, w) in graph:
        mdict[u].append((v, w))
        mdict[v].append((u, w))

    visited = set()
    node_weight = [float('inf')] * (n+1)

    start_pos = 1
    end_pos = 5

    outer_pos = set([start_pos])
    node_weight[start_pos] = 0

    while end_pos not in visited:
        for outer in list(outer_pos):
            if outer in visited:
                continue
            
            links = mdict[outer]
            for u, w in links:
                node_weight[u] = min(node_weight[u], node_weight[outer] + w)
                outer_pos.add(u)
            visited.add(outer)
    
    return node_weight[end_pos]

if __name__ == "__main__":
    w = dijkstra_path()
    print(f"w = {w}")
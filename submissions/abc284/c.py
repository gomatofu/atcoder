import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1 

csr = csr_matrix(graph)
n, labels = connected_components(csr)

print(n)

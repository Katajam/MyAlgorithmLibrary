# Dijkstra's algorithm
# - an algorithm for finding the shortest paths 
# 	between nodes in a graph

from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(G, start, end):
	heap, visited = [(0, start, ())], set()
	while heap:
		(cost, v1, path) = heappop(heap)
		if v1 not in visited:
			visited.add(v1)
			path = (v1, path)
			if v1 == end:
				return (cost, path)
			for v2 in G[v1].keys():
				if v2 not in visited:
					heappush(heap, (cost + G[v1][v2], v2, path))
	return 'inf'

graph = {1: {2: 24, 3: 3, 4: 20}, 2: {1: 24}, 3: {1: 3, 4: 12}, 4: {1: 20, 3: 12}}
print(dijkstra(graph, 1, 4)) # (15, (4, (3, (1, ()))))

# it worths putting here because it's so special
'''
works fine for https://www.hackerrank.com/challenges/dijkstrashortreach

input
1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1

output
24 3 15
'''

'''
lessons to learn:
1. http://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu
	'sys.stdin.readline' is faster than 'input' in this case, 
	and I stuck here and never know this would be a problem.
2. currently both the heapq and queue version work well

Anyways, many thanks to andreimaximov, and his code:
https://github.com/andreimaximov/algorithms/blob/master/algorithms/graph-theory/dijkstra-shortest-reach-2/dijkstra-shortest-reach-2.py
'''

from collections import defaultdict
from heapq import heappush, heappop
# import queue
import sys

def dijkstra(G, start, nodes):
	heap, visited = [(0, start)], set()
	# visited = set()
	# q = queue.PriorityQueue()
	# q.put((0, start))
	# too lazy to move index, make it one larger
	dist, dist[start] = ['-1']*(nodes+1), 0
	while heap:
	# while not q.empty():
		(cost, v1) = heappop(heap)
		# (cost, v1) = q.get()
		if v1 not in visited:
			visited.add(v1)
			if dist[v1] == '-1':
				dist[v1] = str(cost)
			for v2 in G[v1].keys():
				if v2 not in visited:
					heappush(heap, (cost + G[v1][v2], v2))
					# q.put((cost + G[v1][v2], v2))
	return ' '.join([i for i in dist[1:] if i != 0])

cases = int(sys.stdin.readline())
for case in range(cases):
	graph = defaultdict(dict)
	nodes, m_edges = [int(i) for i in sys.stdin.readline().split()]
	for edge in range(m_edges):
		u, v, w = [int(i) for i in sys.stdin.readline().split()]
		if v in graph[u].keys():
			graph[u][v] = graph[v][u] = min(graph[u][v], w)
		else:
			graph[u][v] = graph[v][u] = w
	start = int(sys.stdin.readline())
	print(dijkstra(graph, start, nodes))


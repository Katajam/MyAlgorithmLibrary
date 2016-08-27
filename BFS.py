# Breadth-first search (BFS)
# explores the neighbor nodes first, 
# before moving to the next level neighbors.

# from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# changed some names because my sublime shows weird colors
# also we need deque to speed up!
from collections import deque

def BFS(G, start):
	visited, queue = set(), deque([start])
	while queue:
		current = queue.popleft()
		if current not in visited:
			visited.add(current)
			queue.extend(graph[current] - visited)
	return visited

graph = {1: {2, 3}, 2: {1}, 3: {1}, 4: {}}
print(BFS(graph, 1)) # set([1, 2, 3])

def BFS_path(G, start, end):
	queue = deque([(start, [start])])
	while queue:
		(current, path) = queue.popleft()
		for another in graph[current] - set(path):
			if another == end:
				return path + [another]
			else:
				queue.append((another, path + [another]))

print(BFS_path(graph, 1, 3)) # [1, 3]
print(BFS_path(graph, 1, 4)) # None
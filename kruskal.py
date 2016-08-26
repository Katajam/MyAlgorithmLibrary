# kruskal algorithm
# - a minimum-spanning-tree algorithm which 
#   finds an edge of the least possible weight 
#   that connects any two trees in the forest. 
# - a greedy algorithm in graph theory as it 
#   finds a minimum spanning tree for a connected 
#   weighted graph adding increasing cost arcs at each step.

'''pseudocode
Kruskal(V, E):
	A = empty set
	for v in V:
		disjoint-set(v)
	sort E by increasing weight
	for v1, v2 in E:
		if find(v1) != find(v2):
			A += {(v1, v2)}
			union(v1, v2)
	return A
A is the set of all paths for the minimum spanning tree
'''

# - use disjoint-set
# - adjust find to return the root, not the number
# - also adjust some greater than zero to greater and
#		equal to zero

def union(self, x, y):
	while self.tree[x] >= 0:
		x = self.tree[x]
	while self.tree[y] >= 0:
		y = self.tree[y]
	if x == y:   # same root
		return
	if -self.tree[x] >= -self.tree[y]:
		self.tree[x] += self.tree[y]
		self.tree[y] = x
	else:
		self.tree[y] += self.tree[x]
		self.tree[x] = y

def find(self, x):
	while self.tree[x] >= 0:
		x = self.tree[x]
	return x

def init(self, x):
	self.tree = [-1] * x

Disjoint = type('Disjoint', (), {
	'tree' : [],
	'init' : init,
	'union' : union,
	'find' : find
	})

def kruskal(v, e):
	d = Disjoint()
	d.init(v)
	e.sort(key = lambda x:x[2])
	A = set([])
	for v1, v2, w in edges:
		if d.find(v1) != d.find(v2):
			A.add((v1, v2, w))
			d.union(v1, v2)
	return A

vertices = 4 # vertices are 0 1 2 3
edges = [(0, 1, 5), (0, 2, 3), (3, 0, 6), (1, 3, 7), (2, 1, 4), (2, 3, 5)]
print(kruskal(vertices, edges)) # set([(0, 2, 3), (2, 1, 4), (2, 3, 5)])

# disjoint-set: union-find data structure
# Wikipedia said it's used for:
#  1. Incremental Connected Components functionality
#  2. Kruskal's algorithm (to find the minimum spanning tree)


# 1. union
def union(self, x, y):
	while self.tree[x] > 0:
		x = self.tree[x]
	while self.tree[y] > 0:
		y = self.tree[y]
	if x == y:   # same root
		return
	if -self.tree[x] >= -self.tree[y]:
		self.tree[x] += self.tree[y]
		self.tree[y] = x
	else:
		self.tree[y] += self.tree[x]
		self.tree[x] = y

# 2. find
def find(self, x):
	while self.tree[x] > 0:
		x = self.tree[x]
	return -self.tree[x]

# 3. print
def show(self):
	return self.tree

def init(self, x):
	self.tree = [-1] * x

# build a disjoint-set
# imagine you are building a tree
# when you do union, you connect the root of
#	the smaller tree to the root of the larger
#	tree so that the height of your tree can be
#	less, and store the number in the root
# when you do find, you search until you find
#	its root, at most the height of the tree, 
#	since we only need the number
# the amazing thing is that we will do all of
# 	this in an array, just an array
Disjoint = type('Disjoint', (), {
	'tree' : [],
	'init' : init,
	'union' : union,
	'find' : find,
	'show' : show
	})


d = Disjoint()
d.init(10)
print(d.show())  # [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
print(d.find(2))  # 1
d.union(2, 3)
d.union(0, 2)
d.union(7, 8)
print(d.show())  # [2, -1, -3, 2, -1, -1, -1, -2, 7, -1]
print(d.find(2))  # 3
d.union(2, 7)
print(d.show())  # [2, -1, -5, 2, -1, -1, -1, 2, 7, -1]
print(d.find(2))  # 5

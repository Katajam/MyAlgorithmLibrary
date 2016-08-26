# python 3 
'''
works fine for https://www.hackerrank.com/challenges/merging-communities

input
3 6
Q 1
M 1 2
Q 2
M 2 3
Q 3
Q 2

output
1
2
3
3
'''

P, Q = [int(i) for i in input().split()]

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

def find(self, x):
	while self.tree[x] > 0:
		x = self.tree[x]
	return -self.tree[x]

def init(self, x):
	self.tree = [-1] * x

Disjoint = type('Disjoint', (), {
	'tree' : [],
	'init' : init,
	'union' : union,
	'find' : find
	})


d = Disjoint()
d.init(P+1)  # too lazy to move index, just make it one larger

for q in range(Q):
	get = input().split()
	if get[0] == 'Q':
		print(d.find(int(get[1])))
	elif get[0] == 'M':
		d.union(int(get[1]), int(get[2]))


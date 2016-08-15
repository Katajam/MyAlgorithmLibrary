# python 3
# trie with count
# simply make the count as a key named '-'
'''
works fine for https://www.hackerrank.com/challenges/contacts

input
4
add hack
add hackerrank
find hac
find hak

output
2
0
'''

def add(self, item):
	root = self.tree
	for piece in item:
		root = root.setdefault(piece, {'-': 0})
		root['-'] += 1
	return root

def find(self, item):
	root = self.tree
	for piece in item:
		if piece in root:
			root = root[piece]
		else:
			return 0
	else:
		return root['-']

Trie = type('Trie', (), { 
	'tree' : {},
	'add' : add,
	'find' : find
	})

OPS = int(input())
t = Trie()
for one in range(OPS):
	op, string = input().split()
	if op == 'add': 
		t.add(string)
	elif op == 'find':
		print(t.find(string))


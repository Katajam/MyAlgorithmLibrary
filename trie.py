# python 3
# trie - a cute prefix tree


# 1. add
def add(self, item):
	root = self.tree
	for piece in item:
		root = root.setdefault(piece, {})

# 2. find
def find(self, item):
	root = self.tree
	for piece in item:
		if piece in root:
			root = root[piece]
		else:
			return False
	return True

# 3. print
def show(self):
	print(self.tree)

# build a trie
Trie = type('Trie', (), { 
	'tree' : {},
	'add' : add,
	'find' : find,
	'show' : show
	})


# test some data
t = Trie()
t.add('hello')
t.add('hi')
t.show()  # {'h': {'i': {}, 'e': {'l': {'l': {'o': {}}}}}}
print(t.find('hi'))  # True
print(t.find('ho'))  # False


# python 3
# trie with end sign
# simply add '_' after each adding
'''
works fine for https://www.hackerrank.com/challenges/no-prefix-set

input
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

output
BAD SET
aabcde
'''

def add(self, item):
	root = self.tree
	for piece in item:
		root = root.setdefault(piece, {})
	root['_'] = '_'

def find(self, item):
	root = self.tree
	for index, piece in enumerate(item):
		if piece in root:
			root = root[piece]
		elif index > 0 and root.get('_'):
			return True
		else:
			return False
	return True

Trie = type('Trie', (), { 
	'tree' : {},
	'add' : add,
	'find' : find
	})

def solve():
	OPS = int(input())
	t = Trie()
	for one in range(OPS):
		string = input()
		if t.find(string):
			return 'BAD SET\n' + string
		else:
			t.add(string)
	return 'GOOD SET'

print(solve())
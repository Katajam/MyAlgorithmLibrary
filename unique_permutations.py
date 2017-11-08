x = 'bba'


x = ''.join(sorted(x))
sol = [i for i in x]
used = [False for i in x]
ans = []
def solve(x, n, N):

	if n == N:
		ans.append(''.join(sol))

	last_ele = None
	for i in range(N):
		if used[i]: continue 
		if x[i] == last_ele: continue # avoid repetition

		last_ele = sol[n] = x[i]
		used[i] = True

		solve(x, n + 1, N)

		used[i] = False


solve(x, 0, len(x))
assert(ans == ['abb', 'bab', 'bba'])


from collections import Counter

x = ''.join(sorted(x))
sol = [i for i in x]
c = Counter(x)
keys = sorted(c.keys())
ans = []

# at highly repetitive situation
def solve_2(x, n, N):
	
	if n == N:
		ans.append(''.join(sol))
	
	for i in keys:
		if c[i] > 0:
			c[i] -= 1
			sol[n] = i
			solve_2(x, n + 1, N)
			c[i] += 1	

solve_2(x, 0, len(x))
assert(ans == ['abb', 'bab', 'bba'])

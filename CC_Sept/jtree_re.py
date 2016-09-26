
import math
inf = 10**14

class node:

	def __init__(self, a, b):

		self.length = a
		self.cost = b


def dfs(start, p, d):

	lca[0][start] = p
	depth[start] = d
	for i in graph[start]:
		dfs(i, start, d+1)

def compute(start):

	for i in graph[start]:
		to = i
		small[0][to] = minimise[lca[0][to]]
		to = lca[0][i]
		height = long(math.log(depth[i], 2))
		for j in xrange(1, height+1):
			if (to == -1):
				break

			small[j][i] = min(small[j-1][i], small[j-1][to])
			to = lca[j][i]

		for l in vertex[i]:
			if l.length >= depth[i]:
				minimise[i] = min(minimise[i], l.cost)

			else:
				to = i
				val = inf
				for k in xrange(height+1):
					if (to == -1):
						break

					if (l.length & (1<<k)):
						val = min(val, small[k][to])
						to = lca[k][to]

				minimise[i] = min(minimise[i], l.cost + val)				
	    
     		compute(i)

n, m = map(long, raw_input().split())
graph = [[] for i in range(n+1)]
for i in xrange(n-1):
	a, b = map(long, raw_input().split())
	graph[b].append(a)

depth = [0]*(n+1)
lca = [[-1 for _ in range(n+1)] for i in xrange(18)]
vertex = [[] for i in range(n+1)]
dfs(1, -1, 0)
for i in xrange(1, 19):
	for j in xrange(1, n+1):
		if lca[i-1][j] != -1:
			lca[i][j] = lca[i-1][lca[i-1][j]]

for i in xrange(m):
	v, k, w = map(long, raw_input().split())
	temp = node(k, w)
	vertex[v].append(temp)

minimise = [inf for i in range(n+1)]
small = [[inf for _ in range(n+1)] for i in xrange(18)]
minimise[1] = 0
compute(1)
q = long(raw_input())
query = []
for i in xrange(q):
	print minimise[(long(raw_input()))]


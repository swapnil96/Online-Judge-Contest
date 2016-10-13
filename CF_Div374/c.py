'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

def topo(graph, start):
    
    visited[start] = 1
    for node in graph[start]:   
    	if visited[node] != 1:
    	    topo(graph, node)

    final.insert(0, start)

n, m, t = map(int, raw_input().split())
graph = {}
graph1 = {}
visited = [0]*n
final = []
for i in xrange(n):
	graph[i] = {}
	graph1[i] = {}

for i in xrange(m):
	u, v, w = map(int, raw_input().split())
	graph1[v-1][u-1] = w
	graph[u-1][v-1] = w

for i in xrange(n):
	if visited[i] == 0:
		topo(graph, i)

print graph
print final
print graph1

def find(graph1, start1, to1, val, count, fin):

	visited1[start1] = 1
	for node1 in graph1[start1]:
		val += graph1[start1][node1]
		print val, start1, to1, node1, fin
		if node1 == to1 and val <= t:
			return (1, count)

		elif node1 == to1 and val > t:
			return (0, count)

		if val > t:
			print 'asdf', start1
			return (0, count)

		if visited1[node1] == 0:
			count += 1
			z, y = find(graph1, node1, to1, val, count, fin)
			if z == 1:
				fin = max(fin, y)

	return 	

visited1 = [0]*n
find(graph1, n-1, 0, 0, 0, 0)
print fin
			
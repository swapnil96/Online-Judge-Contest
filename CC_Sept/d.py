
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def bipartite(g, v, src, visited):

	color = [-1]*v
	color[src] = 1
	visited[src] = 1
	que = Queue()
	que.enqueue(src)

	while que.isEmpty() == False:
		t = que.dequeue()
		visited[t] = 1

		for x in xrange(v):
			
			if t == x:
				continue

			if g[t][x] == 1 and color[x] == -1:
				color[x] = 1 - color[t]
				que.enqueue(x)
				visited[x] = 1

			elif g[t][x] == 1 and color[x] == color[t]:
				#print g, color, t, x
				return False	

	#print g, color			
	return True			 	
				


tt = int(raw_input())
for i in xrange(tt):
	n, m = map(int, raw_input().split())
	graph = [[1 for _ in range(n)] for l in range(n)]
	visited = [0]*n
	
	for j in xrange(m):
		x, y = map(int, raw_input().split())
		graph[x - 1][y - 1] = 0
		graph[y - 1][x - 1] = 0	

	for j in xrange(n):	
		if visited[j] == 0:
			if bipartite(graph, n, j, visited):
				ans = "YES"

			else:
				ans = "NO"
				break

			visited[j] = 1	

	print ans		


import sys

# Each element is a list of two elements (priority, element)
PRIORITY = 0
ID = 1

# Data structure. Start by describing the priority queue as storing 
# identifiers (drawn from set [0, n - 1]) and an associated integer priority
# where lower values imply greater importance

class BHeap:

	def __init__(self, size):
		'''Initialize Binary Heap to given number of elements'''

		self.size = size
		self.n = 0
		self.elements = [[0, None] for i in xrange(size + 1)]
		self.positions = [0 for i in xrange(size + 1)]

	def isEmpty(self):
		'''Determine whether Binary Heap is empty'''

		return self.n == 0

	def smallest(self):
		'''Extract and return smallest element in heap - Min Heap'''

		id = self.elements[1][ID]

		# Heap will have one less entry, so place final one appropriately
		last = self.elements[self.n]
		self.n -= 1
		self.elements[1] = last
		pIdx = 1
		child = pIdx * 2
		while child <= self.n:
			# Select smaller of two children
			sm = self.elements[child]
			if child < self.n:
				if sm[PRIORITY] > self.elements[child + 1][PRIORITY]:
					child += 1
					sm = self.elements[child]

			if last[PRIORITY] <= sm[PRIORITY]:
				break

			self.elements[pIdx] = sm
			self.positions[sm[ID]] = pIdx
			pIdx = child
			child = 2 * pIdx

		self.elements[pIdx] = last
		self.positions[last[ID]] = pIdx
		return id				

	def insert(self, id, priority):
		'''Insert item into heap with given priority'''

		self.n += 1
		i = self.n
		while i > 1:
			pIdx = int(i / 2)
			p = self.elements[pIdx]
			if priority > p[PRIORITY]:
				break

			self.elements[i] = list(p)
			self.positions[p[ID]] = i
			i = pIdx

		self.elements[i][ID] = id
		self.elements[i][PRIORITY] = priority
		self.positions[id] = i

	def decreaseKey(self, id, newPriority):
		'''Reduce the priority for the given item'''

		size = self.n
		self.n = self.positions[id] - 1
		self.insert(id, newPriority)
		self.n = size

def singleSourceShortestPath(graph, s, ver):
	''' Compute and return (dist, pred) matrices of computation'''

	pq = BHeap(ver)
	dist = {}
	for v in xrange(0, ver):
		dist[v] = sys.maxint

	dist[s] = 0
	for v in xrange(0, ver):
		pq.insert(v, dist[v])

	while not pq.isEmpty():
		u = pq.smallest()
		for v in graph[u]:
			wt = graph[u][v]
			newlen = dist[u] + wt
			try:
				if newlen < dist[v]:
					pq.decreaseKey(v, newlen)
					dist[v] = newlen
			except:
				#print v, u			
				pass
	return dist

n, m = map(int, raw_input().split())
to = [-1]*(n)
graph = {}
for i in xrange(n-1):
	a, b = map(int, raw_input().split())
	to[a - 1] = b - 1
	graph[i] = {}

graph[n-1] = {}
#till = [0]*(n)
#print to
#graph = [[-1 for _ in range(n)] for p in range(n)]
for i in xrange(m):
	v, k, w = map(int, raw_input().split())
	#if k > till[v - 1] or w < cos[v - 1]:	
	temp = k
	y = v - 1
	'''
	while temp != 0:
		try:
			if graph[to[y]][v - 1] > w or graph[to[y]][v - 1] == -1:
				graph[to[y]][v - 1] = w
				#print to[y], v-1, 'asdf'

			y = to[y]	
			temp -= 1

		except:
			pass
			#print to[y], v-1	
	#till[v - 1] = k
	'''
	while temp != 0 and to[y] != -1: 
		try:
			if graph[to[y]][v - 1] > w:
				graph[to[y]][v - 1] = w

		except:
			if graph[to[y]] == {}:
				graph[to[y]] = {v - 1: w}

			else:
				graph[to[y]][v - 1] = w	
		
		y = to[y]
		temp -= 1
		
#print graph
ans = singleSourceShortestPath(graph, 0, n)
q = int(raw_input())
query = []
for i in xrange(q):
	#query.append(int(raw_input()))
	print ans[int(raw_input()) - 1]
'''
for i in xrange(q):
	print ans[query[i] - 1]
'''	
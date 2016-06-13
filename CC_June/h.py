
class Graph:

	def __init__(self):
		'''Creater an empty graph'''

		self.edges = {}

	def addVertex(self, ver):
		'''Add vertex to the graph if not already present'''

		if ver not in self.edges:
			self.edges[ver] = []

	def addEdge(self, from_ver, to_ver):
		'''Creates a road between given vertices'''

		if from_ver not in self.edges:
			self.edges[from_ver] = []

		if to_ver not in self.edges:
			self.edges[to_ver] = []

		if from_ver not in self.edges[to_ver]:
			self.edges[to_ver].append(from_ver)

		if to_ver not in self.edges[from_ver]:
			self.edges[from_ver].append(to_ver)

	def isedge(self, from_ver, to_ver):
		'''Determines whether edge exists'''

		if to_ver not in self.edges:
			return False

		if from_ver not in self.edges:
			return False

		return to_ver in self.edges[from_ver]

def loadgraph(edges):
	'''Create a graph instance'''

	g = Graph()
	for v in edges:
		g.addVertex(v)
		#for neighbour in edges[v]:
		g.addEdge(v, edges[v])

	return g	

tt = map(int, raw_input().split())
a = map(int, raw_input().split())
dic = {}
for i in xrange(tt[1]):
	b = map(int, raw_input().split())
	dic[b[0]] = b[1]

gra = loadgraph(dic)
print gra.edges

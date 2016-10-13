
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''


import math

class segmentTree:


	def __init__(self, n):
		self.length = 2*(2**(int(math.log(n, 2)) + 1)) - 1
		self.tree1 = [0]*(self.length)

	def build(self, start, end, main, node = 0):

		if start == end:
			self.tree1[node] = main[start]

		else:
			mid = (start + end) / 2	
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			self.tree1[node] = self.tree1[2*node + 1] + self.tree1[2*node + 2]

	def update1(self, start, end, l, node = 0):

		if (start > end) or (start > l) or (end < l):
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return

		if start == end:
			self.tree1[node] = -1
			#print self.tree[node], start, end, l, r, node, 'qwre'
			return
		
		mid = (start + end ) / 2	

		if l <= mid:
			self.update1(start, mid, l, 2*node + 1)

		else:
			self.update1(mid + 1, end, l, 2*node + 2)
			
		self.tree1[node] = max(self.tree1[2*node + 1], self.tree1[2*node + 2])
		

n = int(raw_input())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
g = segmentTree(n)
g.build(0, n-1, a)
ans = []
print g.tree1
for i in xrange(n):
	g.update1(0, n-1, b[i]-1)
	print g.tree1
	ans.append(g.tree1[0])

for i in xrange(n):
	print ans[i]

import math

primes = [2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,

 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,

 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,

 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,

 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,

 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,

 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

def lpd(t):
	for i in primes:
		if t % i == 0:
			return i
		
	return t

def do(lpds):
	for i in xrange(2, 10**6 + 1):
		lpds.append(lpd(i))

class segmentTree:


	def __init__(self, n):
		self.length = 2*(2**(int(math.log(n, 2)) + 1)) - 1
		self.tree = [0]*(self.length)
		self.lazy = [0]*(self.length)

	def build(self, start, end, main, node = 0):

		if start == end:
			
			self.tree[node] = lpds[main[start] - 1]

		else:
			mid = (start + end) / 2	
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])
	
	def update(self, start, end, l, r, main, node = 0):

		if (start > end) or (start > r) or (end < l):
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return

		if start == end:
			self.tree[node] = lpds[main[start]/(lpds[main[start] - 1]) - 1]
			main[start] = main[start]/(lpds[main[start] - 1])
			#print self.tree[node], start, end, l, r, node, 'qwre'
			return
		
		if self.tree[node] == 1:
			return 

		mid = (start + end ) / 2	
		self.update(start, mid, l, r, main, 2*node + 1)
		self.update(mid + 1, end, l, r, main, 2*node + 2)
		self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])			
		#print self.tree[node], start, end, l, r, node, 'fuck'	

	def get(self, start, end, l, r, main, node = 0):
		
		if r < start or end < l:
			#print self.tree[node], start, end, l, r, node, 'qewr'
			return 0

		if l <= start and end <= r:
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return self.tree[node]

		if self.tree[node] == 1:
			return 1

		mid = (start + end) / 2
		p1 = self.get(start, mid, l, r, main, 2*node+1)
		p2 = self.get(mid + 1, end, l, r, main, 2*node+2)
		#print self.tree[node], start, end, l, r, node, 'bill'
		return max(p1, p2)

tt = int(raw_input())
lpds = [1]
for i in xrange(tt):
	n, m = map(int, raw_input().split())
	a = map(int, raw_input().split())
	if i == 0:
		do(lpds)

	g = segmentTree(n)	
	g.build(0, n-1, a)
	query = []
	for j in xrange(m):
		query.append(map(int, raw_input().split()))

	temp = []	
	for j in xrange(m):
		if query[j][0] == 0:
			g.update(0, n-1, query[j][1]-1, query[j][2]-1, a)
			#g.aupdate(query[j][1] - 1, query[j][2] -1 , a)
			#print g.tree

		else:
			temp.append(g.get(0, n-1, query[j][1]-1, query[j][2]-1, a))
			#print g.tree

	print ' '.join(map(str, temp))	
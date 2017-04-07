
import math

def func(num):

    max_a = int(math.sqrt(num))
    min_a = int(math.sqrt(num/4))
    got = 0
    for a in xrange(min_a, max_a+1):

        temp = num - a**2
        max_b = int(math.sqrt(temp))
        min_b = int(math.sqrt(temp/3))

        for b in xrange(min_b, max_b+1):

            temp1 = temp - b**2
            max_c = int(math.sqrt(temp1))
            min_c = int(math.sqrt(temp1/2))

            for c in xrange(min_c, max_c + 1):

                temp2 = temp1 - c**2
                root = int(math.sqrt(temp2))
                if root**2 == temp2:
                    got = 1
                    d = root
                    break

            if got == 1:
                break

        if got == 1:
            break

    return [a, b, c, d]

def shift_bit_length(x):
    return 1<<(x-1).bit_length()

class segmentTree:


	def __init__(self, n, p):
		self.p = p
		self.length = 2*(shift_bit_length(n)) - 1
		self.tree = [1]*(self.length)

	def build(self, start, end, main, node = 0):

		if start == end:
			self.tree[node] = main[start] % self.p

		else:
			mid = (start + end) / 2
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			self.tree[node] = (self.tree[2*node + 1] * self.tree[2*node + 2])%self.p
			# print self.tree[2*node + 1] * self.tree[2*node + 2]

	def update(self, start, end, idx, val, main, node = 0):

		if start == end:
			main[start] = val
			self.tree[node] = val % self.p
			# print self.tree[node], start, end, idx, node, 'qkhkk', main, val
			return

		mid = (start + end ) / 2
		if start <= idx and idx <= mid:
			self.update(start, mid, idx, val, main, 2*node + 1)

		else:
			self.update(mid + 1, end, idx, val, main, 2*node + 2)

		self.tree[node] = (self.tree[2*node + 1] * self.tree[2*node + 2]) % self.p

	def get(self, start, end, l, r, main, node = 0):

		if r < start or end < l:
			#print self.tree[node], start, end, l, r, node, 'qewr'
			return 1

		if l <= start and end <= r:
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return self.tree[node]

		mid = (start + end) / 2
		p1 = self.get(start, mid, l, r, main, 2*node+1)
		p2 = self.get(mid + 1, end, l, r, main, 2*node+2)
		#print self.tree[node], start, end, l, r, node, 'bill'
		return (p1 * p2)%self.p

tt = long(raw_input())
temp = []
length = 0
half = []
for i in xrange(10**4 + 1):
    half.append(func(i))

print half
for i in xrange(tt):
	n, q, p = map(long, raw_input().split())
	a = map(long, raw_input().split())
	g = segmentTree(n, p)
	g.build(0, n-1, a)
	for j in xrange(q):
		query = map(long, raw_input().split())
		if query[0] == 2:
			val = g.get(0, n-1, query[1]-1, query[2]-1, a)
			val = val % p

			ans = func(val)
			temp.append(ans)
			length += 1

		elif query[0] == 1:
			g.update(0, n-1, query[1]-1, query[2], a)

for i in xrange(length):

	print ' '.join(map(str, temp[i]))

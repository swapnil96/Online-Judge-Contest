def shift_bit_length(x):
    return 1<<(x-1).bit_length()
 
class segmentTree:
	def __init__(self, n):
		self.length = 2*(shift_bit_length(n)) - 1
		self.tree = [0]*(self.length)
		self.tree2 = [-1]*(self.length)
 
	def build(self, start, end, main, node = 0):
		if start == end:
			self.tree[node] = main[start]
			self.tree2[node] = start
 
		else:
			mid = (start + end) / 2	
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			if self.tree[2*node + 1] >= self.tree[2*node + 2]:
				self.tree2[node] = self.tree2[2*node+1]
			
			else:
				self.tree2[node] = self.tree2[2*node+2]
 
			self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])
	
	def update(self, start, end, idx, node = 0):
 
		if start == end:
			lec[idx] -= 1
			if lec[idx] == 0:
                		self.tree[node] = 0
				self.tree2[node] = -1
			return 
 
        	else:
		    	mid = (start + end) / 2	
            		if start <= idx and idx <= mid:
                		self.update(start, mid, idx, 2*node + 1)
 
            		else:
		        	self.update(mid + 1, end, idx, 2*node + 2)
        
			if self.tree[2*node + 1] >= self.tree[2*node + 2]:
				self.tree2[node] = self.tree2[2*node+1]
			
			else:
				self.tree2[node] = self.tree2[2*node+2]
	    		
			self.tree[node] = max(self.tree[2*node + 1], self.tree[2*node + 2])
 
 
	def get(self, start, end, l, r, node = 0):
		
		if r < start or end < l:
			return [0, -1]
 
		if l <= start and end <= r:
            		return [self.tree[node], self.tree2[node]]
 
		mid = (start + end) / 2
		p1 = self.get(start, mid, l, r, 2*node+1)
		p2 = self.get(mid + 1, end, l, r, 2*node+2)
		if p1[0] >= p2[0]:
			return p1
		
		else:
			return p2
 
tt = int(raw_input())
for i in xrange(tt):
    n, d = map(int, raw_input().split())
    day = [0]*n
    lec = [0]*n
    sad = [0]*n
    done = [0]*d
    total = 0
    for j in xrange(n):
        day[j], lec[j], sad[j] = map(int, raw_input().split())
        total += lec[j] * sad[j]
    
    temp = zip(day, sad, lec)
    temp = sorted(temp)
    j = 0
    for x, y, z in temp:
        day[j], sad[j], lec[j] = x, y, z
        j += 1
    
    day_idx = [-1]*d
    for j in xrange(n):
        day_idx[day[j]-1] = j
 
    curr = -1
    for j in xrange(d):
        if day_idx[j] != -1:
            curr = day_idx[j]
 
        day_idx[j] = curr
 
    g = segmentTree(n)
    g.build(0, n-1, sad)
    tot = 0
    for j in xrange(d):
	if day_idx[j] != -1:
	    temp = g.get(0, n-1, 0, day_idx[j])
            if temp[0] != 0:
                g.update(0, n-1, temp[1])
        
            tot += temp[0]
    
 
    print total - tot
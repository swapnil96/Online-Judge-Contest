
def hcf(x, y):
   
   while(y):
       x, y = y, x % y

   return x

def find(v):

	a = v[0]
	b = v[1]
	c = v[2]
	d = v[3]
	if a == b:
		return 0 

	more = abs(a - b)
	get = hcf(c,d)
	t = more % get
	return min((t), get - t )

tt = int(raw_input())
sol = []
for i in xrange(tt):
	v = map(int, raw_input().split())
	sol.append(find(v))

for i in xrange(tt):
	print sol[i]


def find(no, strength, start):

	keys = list(range(1, no+1))
	values = list(range(1, no+1))
	dic = {}
	for i in xrange(1, no+1):

		values.remove(i)
		dic[i] = values
		print dic
		values.append(i)
		values.sort()
	
	print dic







tt = int(raw_input())
sol = []
for i in xrange(0, tt):

	a = raw_input()
	b = map(int, a.split())
	no = b[0]
	s = b[1]
	j = raw_input()
	strength = map(int, j.split())
	start = b[2]
	sol.append(find(no, strength, start))

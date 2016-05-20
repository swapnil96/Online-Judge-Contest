
def cut(law, req, que):

	got = 0
	#print law, req, que
	i = 1

	while True:
		
		got = 0
		for j in xrange(0, len(que)):

			que[j][0] += que[j][1]

			if que[j][0] >= law:

				got += que[j][0]

		#print que
		if got >= req:
			return i

		i += 1			


a = raw_input()
b = a.split()
no = int(b[0])
req = int(b[1])
law = int(b[2])
que = []
for i in xrange(0, no):

	q = raw_input()
	que.append(map(int, q.split()))
print cut(law, req, que)
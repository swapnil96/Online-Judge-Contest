
def find(no, ori, que):

	pts = 0

	for i in que:

		if i[0] == 'C':

			if i[8] == 'W':

				rank = int(i[12:])
				if rank > 20:
					pts += 300

				else:	
					pts += 300 + (20 - rank)

			else:

				pts += 50

		elif i[0] == 'B':
		
			sev = int(i[10:])
			pts += sev

		else:
			
			pts += 300

	if ori == 1:

		mon = pts/200

	else:
		
		mon = pts/400


	return mon		

tt = int(raw_input())
sol = []
for i in xrange(0, tt):

	a = raw_input()
	b = a.split()
	no = int(b[0])
	
	if b[1] == 'INDIAN':

		ori = 1

	else:

		ori = 0
	que = []
	for j in xrange(0, no):

		que.append(raw_input())

	sol.append(find(no, ori, que)			)

for i in xrange(tt):

	print sol[i]
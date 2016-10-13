'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

n, k = map(int, raw_input().split())
temp = []
for i in xrange(n):
	a = raw_input()
	temp.append(a)

corr = raw_input()
length = sorted(temp, key=len)	
to = len(corr)
tot = 0
penal = 0
for i in xrange(n):
	now = len(length[i])
	#print now, penal, length[i]
	if penal == k:
		tot += 5
		penal = 0

	if now < to:
		tot += 1
		penal += 1

	elif now == to:
		loop = 0
		for j in xrange(i, n):
			now1 = len(length[j])
			if now1 > to:
				break

			loop += 1	

		#print tot, loop		
		mini = tot + 1
		maxi = tot + 5*((loop-1)/k) + loop
		break


print mini, maxi				


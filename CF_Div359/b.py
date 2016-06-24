
import sys

'''
tt = int(raw_input().split())
a = map(int, raw_input().split())
a = map(int, (' '.join(n for n in raw_input())).split())
for i in xrange(tt):
'''

tt = int(raw_input())
a = map(int, raw_input().split())
while True:
	fin = -1
	ini = -1
	for i in xrange(0, tt-1):
		if a[i] > a[i + 1]:
			ini = i
			break

	if ini == -1:
		sys.exit()		

	for i in xrange(ini + 2, tt - 1, 2):
		if a[i] > a[i + 1]:
			fin = i + 1

	if fin == -1:
		fin = ini + 1		

	if (fin - ini + 1) & 1 != 0:
		fin -= 2

	if fin == ini:
		fin += 1

	for j in xrange(ini, fin, 2):
		a[j], a[j+1] = a[j+1], a[j]

	print ini+1, fin+1 #, a

	got = 0
	for j in xrange(tt - 1):
		if a[j] > a[j+1]:
			got = 1

	if got == 0:
		break			

	#print got
	#sys.exit()			

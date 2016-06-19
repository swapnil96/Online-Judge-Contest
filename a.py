
from random import *
import sys
'''1010001111'''
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)]
real = {}
to_print = ''.join(map(str, randBinList(10)))
'''
for i in xrange(100):
	for v in real.keys():
		if real[v] != to_print[v]:
			to_print = to_print[:v] + to_print[v].replace(to_print[v], real[v]) + to_print[v+1:]

	print to_print
	sys.stdout.flush()
	rep = int(raw_input())
	if to_print[rep - 1] == '1':
		real[rep - 1] = '0'
		if rep == 2:
			if to_print[0] == '0':
				real[0] = '1'

			else:
				real[0] = '0'	

	else:
		real[rep - 1] = '1'	
		if rep == 2:
			if to_print[0] == '0':
				real[0] = '1'

			else:
				real[0] = '0'

sys.exit()
'''

def binary_search(to_print):
	
	for i in xrange(3):	
		print to_print
		sys.stdout.flush()
		rep = int(raw_input())
		if to_print[rep - 1] == '1':
			to_print = to_print[:rep-1] + to_print[rep].replace(to_print[rep], '0') + to_print[rep:]

		else:
			to_print = to_print[:rep-1] + to_print[rep].replace(to_print[rep], '1') + to_print[rep:]

		

binary_search(to_print)


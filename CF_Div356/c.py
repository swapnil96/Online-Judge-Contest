'''
import sys
lis = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
count = 2

for i in xrange(10, 1, -1):
	print i
	sys.stdout.flush()
	a = raw_input()
	if a == 'yes':
		count += 1
		
		print 25
		sys.stdout.flush()
		a = raw_input()
		if a == 'yes':
			print 'composite'
			sys.stdout.flush()
			sys.exit()

		else:
			print 49
			sys.stdout.flush()
			a = raw_input()
			if a == 'yes':
				print 'composite'
				sys.stdout.flush()
				sys.exit()
		
		for j in xrange(i-1, 1, -1):
			print j
			sys.stdout.flush()
			a = raw_input()
			if a == 'yes':
				print 'composite'
				sys.stdout.flush()
				sys.exit()

		count -= 1		
							
	if count > 2:
		print 'composite'
		sys.stdout.flush()
		sys.exit()

print 'prime'
sys.stdout.flush()
sys.exit()
'''
'''Solution'''
from sys import stdout

PRIMES = [x for x in range(2,100) if 0 not in [x%i for i in range(2,x)]]

NORMAL = PRIMES[:15]
SQUARES = [x*x for x in PRIMES[:4]]

for ele in SQUARES:
    print(ele)
    stdout.flush()
    x = raw_input()
    if x == "yes":
        print("composite")
        exit(0)

yes = 0
for ele in NORMAL:
    print(ele)
    stdout.flush()
    x =raw_input()
    if x == "yes":
        yes += 1

print("prime" if yes < 2 else "composite")
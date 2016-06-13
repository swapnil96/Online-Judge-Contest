aol = []
import time
import timeit
for i in xrange(1000):
	aol.append([j for j in xrange(1, 1001)])

query = []

for i in xrange(1,51):
	query.append([i,i])

def func():
	j = 0
	for i in xrange(10**7):
		j += 1	

now = time.time()
func()
print time.time() - now, 'adf'
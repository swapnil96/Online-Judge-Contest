import random
#a = [int(1000*random.random()) for i in xrange(-10000, 10000)]
a = []
for x in range (0, 100000):
    a.append(random.randint(-10**9, 10**9))

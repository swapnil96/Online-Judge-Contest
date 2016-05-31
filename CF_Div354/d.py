import math

def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y):
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] 
    for count in range(rows): 
        row = []
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
        
    return result

a = raw_input()
b = map(int, a.split())
i = 1
time = b[1]
finish = 0
got = 0
a = pascals_triangle(b[0])
for row in a:
	div = 2**(len(row) - 1)
	for num in row:
		a[a.index(row)][row.index(num)] *= 1.0/div

c = [[0]*11 for _ in range(11)]
for x in xrange(1, time):
	
	for i in xrange(x):
		for j in xrange(i+1):
			if c[i][j] == 1:
				continue

			else:	
				c[i][j] += a[i][j] 

		if i == b[0] - 1:
			i = 0		

print c
'''http://codeforces.com/contest/676/problem/B'''
a=[[0]*11 for _ in range(11)]
n,a[0][0]=map(int,raw_input().split())
z=0
a[0][0]*=1024
for r in range(n):
  for c in range(r+1):
    d=a[r][c]-1024
    if d>=0:
      z+=1
      a[r+1][c]+=d/2
      a[r+1][c+1]+=d/2
print z
'''
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
	div = 1.0/(2**(len(row) - 1))
	print row, div, 'asdf'
	if len(row) % 2 == 0:
		gmid = len(row)/2
		row = row[gmid:]
		for num in row:
			pour = time*num*div
			print pour, row
			if pour >= 1:
				time -= 2
				got += 2
			
			if time <= 0:
				finish = 1
				break

	else:
		gmid = len(row)/2 	
 		row = row[gmid:]
		for num in row:
			pour = time*num*div
			print pour, row
			if pour >= 1:
				if row.index(num) == 0:
					print 'qwr'
					time -= 1
					got += 1
				
				else:	
					time -= 2
					got += 2

			if time <= 0:
				finish = 1
				break

	if finish == 1:
		break

print got	

'''
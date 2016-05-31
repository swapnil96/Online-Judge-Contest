


def adsf(array, size):

	sum1 = 0
	overall = max1 = -10**9 - 1

	for j in xrange(size):
		sum1 += array[j]
		if sum1 > max1:
			max1 = sum1
		if sum1 < 0:
			sum1 = 0

	compare = max1
	for i in xrange(size):
		if array[i] > 0:
			continue

		else:
			sum1 = 0
			max1 = -10**9 - 1
			for j in xrange(size):
				if j == i:
					continue

				sum1 += array[j]
				if sum1 > max1:
					max1 = sum1

				if sum1 < 0:
					sum1 = 0

			if max1 > overall:
				overall = max1
		
	return max(compare, overall)											

class result:

	def __init__(self, sum1, except1, left, right):

		self.sum1 = sum1
		self.except1 = except1
		self.left = left
		self.right = right

def last(array, n):
	
	re = result(sum(array), -1, 1, 1)
	for i in xrange(n):
		l = sum(array[:i])
		r = sum(array[i+1:])
		print l, r, i, re.sum1
		if ((i > 0 and i < n - 1) and (l + r > re.sum1)):
			re.sum1 = l + r
			re.except1 = i
			re.left = 1
			re.right = 1
			if re.sum1 < re.sum1 + array[i]:
				re.sum1 += array[i]	

		if ((i > 0) and (l > re.sum1)):	
			re.sum1 = l
			re.except1 = i
			re.left = 1
			re.right = 0
			if re.sum1 < re.sum1 + array[i]:
				re.sum1 += array[i]	

		if (i < n -1) and (r > re.sum1):
			re.sum1 = r
			re.except1 = i
			re.left = 0
			re.right = 1
			if re.sum1 < re.sum1 + array[i]:
				re.sum1 += array[i]	

	#print re.right, re.left			
	return re.sum1 + min(re.right, re.left)			

tt = int(raw_input())
sol = []
for i in xrange(tt):
	length = int(raw_input())
	array = map(int, raw_input().split())
	sol.append(last(array, length))
	#sub = maxSubArraySum(array, length)
	#print sub

for i in xrange(tt):
	print sol[i]

'''Problem name - MMSUM'''
'''Correct Solution'''
def R(): return map(int, raw_input().split())
 
T = R()[0]
for i in range(T):
    N = R()[0]
    A = R()
 
    all_negative = True
    max_element = None
    max_so_far = 0
    max_ending_left = 0     # maximum subsequence ending at prev position
    max_skipped_one = 0     # maximum subsequence ending at curr position where one element was skipped
    for x in A:
        max_element = max(max_element, x)
        all_negative = all_negative and x < 0
 	
        max_ending_left, max_skipped_one  = max(0, max_ending_left + x), max(0, max_ending_left, max_skipped_one + x)
        #print x, max_ending_left, max_skipped_one
        max_so_far = max(max_so_far, max_skipped_one, max_ending_left)
 
    print max_element if all_negative else max_so_far
 
class result:

	def __init__(self, sum1, except1, left, right):

		self.sum1 = sum1
		self.except1 = except1
		self.left = left
		self.right = right
'''
def last(array, size):

	re = result(sum(array), -1, 1, 1)
	for i in xrange(size):
		l = sum(array[:i-1])
		r = sum(array[i+1:])

		if (((i > 0) and (i < n - 1)) and ((l + r ) > re.sum1)):
        	re.sum1 = l + r
        	re.except1 = i
            re.left = 1
            re.right = 1
        
      	#Only left is considered. No else if, because of the case
        #when the right is negative and smaller than the left
        if ((i > 0) and (l > re.sum1)):
            re.sum1 = l
            re.except1 = i
            re.left = 1
            re.right = 0
        
        #Only right is considered. No else if, because of the case
        #when the left is negative and smaller than the right
        if ((i < n - 1) and (r > re.sum1)):
            re.sum1 = r
            re.except1 = i
            re.left = 0
            re.right = 1
       
    return re.sum1
'''
def last(array, n):
	
	re = result(sum(array), -1, 1, 1)
	for i in xrange(n):
		l = sum(array[:i-1])
		r = sum(array[i+1:])
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


	return re.sum1 + min(re.right, re.left)		

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

''' 	
def find(array, size):

	temp = -10**9
	k = -1
	o = -1
	l = maxSubArraySu(array, size) 
	mi = min(array)
	print mi, 'adsf'
	for i in xrange(size):
		
		if array[i] < 0:
			if i == 0:
				su = array[1]
				if su > temp:
					temp = su
					k = i
		
			elif i == (size - 1):
				su = array[i - 1]
				if su > temp:
					temp = su
					k = i
		
			else:
				su = array[i - 1] + array[i + 1]
				if su > temp:
					temp = su
					k = i

	temp = -10**9				
	for i in xrange(size):
		
		if array[i] == mi:
			if i == 0:
				su = array[1]
				if su > temp:
					temp = su
					o = i
		
			elif i == (size - 1):
				su = array[i - 1]
				if su > temp:
					temp = su
					o = i
		
			else:
				su = array[i - 1] + array[i + 1]
				if su > temp:
					temp = su
					o = i
				
	#print k				
	#print array
	tot2 = tot1 = 0
	if o >= 0:
		qwe = array[o]
		array.pop(o)
		tot1 = max(maxSubArraySu(array, size - 1), l)
		array.insert(o, qwe)

	if k >= 0:
		qwe = array[k]
		array.pop(k)
		tot2 = max(maxSubArraySu(array, size - 1), l)
		array.insert(k, qwe)

	return max(tot2, tot1, l)	
'''


'''
def maxSubArraySum(a,size):
     
    max_so_far = 0
    max_ending_here = 0
    j = 0 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            j = i
            max_ending_here = 0
         
        if (max_so_far < max_ending_here):
            k = i
            l = j
            max_so_far = max_ending_here
             
    return max_so_far
'''

'''

	for i in xrange(0, size):

		if a[i] < 0:
			temp = i
			continue

		max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
         
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here	
			
'''
def mind(a,size):
     
    max_so_far = 0
    max_ending_here = 0
     
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here >= 0 and a[i] < 0:
        	#print max_ending_here, a[i], max_so_far
        	#if max_ending_here - a[i] >= max_so_far:
        	max_ending_here = max_ending_here - a[i]
        if max_ending_here < 0:
            max_ending_here = 0
         
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
             
    return max_so_far


def maxSubArraySu(a,size):
     
    max_so_far = a[0]
    curr_max = a[0]
    for i in range(1,size):
	
      	curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
        	
    return max_so_far

def find(array, size):

	curr_max = []
	max_so_far = array[0]
	curr_max.append(array[0])

	for i in xrange(1, size):

		if array[i] < 0:
			#print curr_max
			temp = curr_max[0]
			#curr_max = map(lambda x: max(array[i], x + array[i]), curr_max)
			curr_max = [max(array[i], x + array[i]) for x in curr_max]
			#for j in xrange(len(curr_max)):
			#	curr_max[j] = max(array[i], array[i] + curr_max[j])
		
			high = max(curr_max)
			max_so_far = max(max_so_far, high)	
			curr_max.append(temp)
			continue

		#curr_max = map(lambda x: max(array[i], x + array[i]), curr_max)
		curr_max = [max(array[i], x + array[i]) for x in curr_max]
		#for j in xrange(len(curr_max)):
		#	curr_max[j] = max(array[i], array[i] + curr_max[j])

		#print curr_max
		high = max(curr_max)
		max_so_far = max(max_so_far, high)

	return max_so_far

def hel(b, size):

	max_so_far = b[0]
	curr_max = b[0]
	max_so_far_temp = -1 - 10**9

	for j in xrange(1, size): 
		
		if b[j] < 0:
			#print curr_max, max_so_far, 'adsf'
			curr_max_temp = curr_max
			max_so_far_temp = max_so_far

			for i in xrange(j + 1, size):

				curr_max_temp = max(b[i], curr_max_temp + b[i])
				max_so_far_temp = max(max_so_far_temp, curr_max_temp)

		if max_so_far_temp > max_so_far:
			max_so_far = max_so_far_temp

		curr_max = max(b[j], curr_max + b[j])
		max_so_far = max(max_so_far, curr_max)
		#print curr_max, max_so_far, 'qwer'

	return max_so_far	
		
def maximum(a,size):
     
    max_so_far = 0
    max_ending_here = 0
    j = k = l = 0

    if bool(all(i < 0 for i in a)) is True:
    	return min(array)

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            j = i + 1
            max_ending_here = 0
         
        if (max_so_far < max_ending_here):
            k = i
            l = j
            max_so_far = max_ending_here
    
    return l, k
    u = min(a[l, k])
    if u < 0:
    	fir = max_so_far - u

    #return max_so_far
'''
def maxSubArraySum(a,size):
     
    max_so_far = a[0]
    curr_max = a[0]
    curr_max1 = a[0]
    temp = 0
    for i in range(1,size):
        
        curr_max1 = max(a[i], curr_max1 + a[i])
        max_so_far1 = max(max_so_far, curr_max1)
        #print curr_max1, 'asdf', i
        if a[i] < 0:
        	if temp == 0:
        		temp = a[i]
        		z = curr_max1
        		continue

        	else:
        		curr_max = z
        		temp = a[i]
        		z = curr_max1
        		continue

        else:			
        	curr_max = max(a[i], curr_max + a[i])
        	max_so_far = max(max_so_far, curr_max)
        	#print curr_max, max_so_far

        z = curr_max1	

    #print max_so_far1, max_so_far    
    return max(max_so_far, max_so_far1)
'''

def find2(array, size):

	got = maxSubArraySu(array, size)
	a = maximum(array, size)
	print a, sum(array[a[0]:a[1]+1])
	print array, 'asdf'
	for i in xrange(size):
		
		if array[i] < 0:
			temp = array[i]
			array.pop(i)
			p = maxSubArraySu(array, size - 1)
			print array, p, maximum(array, size - 1)
			if p >= got:
				got = p

			array.insert(i, temp)	
			
	#print got
	return got

#print maxSubArraySum([1, -2, 3, 5], 4)

import temp
import time
now = time.time()
s = 10
h = temp.a[:10]
#print h
print find2(h, s)
#print hel(h, s)
#print find(h, s)
#print last(h, s)
print time.time() - now
then = time.time()
#print mind(h, s)
#print adsf(h, s)
#print maxSubArraySum(h, s)
#print (time.time() - then)
#print temp.a


'''
tt = int(raw_input())
sol = []
for i in xrange(tt):
	length = int(raw_input())
	array = map(int, raw_input().split())
	sol.append(find2(array, length))
	#sub = maxSubArraySum(array, length)
	#print sub

for i in xrange(tt):
	print sol[i]


#print find2(array, length), 'adsf'	
#print find(array, length)
'''
'''
import temp
print maxSubArraySum(temp.a, 100000)

[-177564821, 930869278, -151328191, -799241514, 47181689, 905536526, -211276920, 292420790, 318929491, 3193378]


'''
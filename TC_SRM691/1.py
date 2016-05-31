
class Undiv:

	def __init__(self, no):

		self.no = no

	def getsum(self, no):
		
		final = []
		sum1 = 0
		for i in xrange(1, no+1):

			a = 1
			got = 0
			while True:
 				
 				if i % a != 0:
 					got += 1

 				if got == 2:
 					sum1 += a
 					break

 				a += 1		

 		#print sum(final)
 		return sum1
 		'''
 		sum1= 0
 		for i in xrange(1, no+1):
 		
 			#now = time.time()
 			if i < 100:
 				a = 1
				got = 0
				while True:
 				
 					if i % a != 0:
 						got += 1

 					if got == 2:
	 					sum1 += a
 						break

 					a += 1	
 				continue	
 			#then = time.time()
 			#print then - now
 			#print i	
 			got = 0
 			check1 = check2 = check3 =  0
 			if no % 2 != 0:
 				got += 1
				check1 = 1 

 			y = str(i)	
 			#print y
 			if 	sum(map(int, y)) % 3 != 0:
 				got += 1
 				check2 = 1
 				if got == 2:
 					sum1 += 3
 					continue

 			if int(y[len(y)-2:]) % 4 != 0:
 				got += 1
 				check3 = 1
 				if got == 2:
 					sum1 += 4
 					continue
			
			if int(y[len(y) - 1]) == 0 or int(y[len(y) - 1]) == 5:
				got += 1
 				if got == 2:
 					sum1 += 5
 					continue

 			if check2 == check1 == 1:
 				got += 1
 				if got == 2:
 					sum1 += 6
 					continue
			
			if  int(y[:len(y) - 1]) - 2*int(y[len(y) - 1]) % 7 != 0:
				got += 1
 				if got == 2:
 					sum1 += 7
 					continue

 			if int(y[len(y) - 3:]) % 8 != 0:
 				got += 1
 				if got == 2:
 					sum1 += 8
 					continue
			
			if sum(map(int, y)) % 9 != 0:
				got += 1
 				if got == 2:
 					sum1 += 9
 					continue
			
			if int(y[len(y)- 1]) != 0:
				got += 1
 				if got == 2:
 					sum1 += 10
 					continue
			
			if int(y[:len(y) - 1]) - int(y[len[y] - 1]) % 11 != 0:	
				got += 1
 				if got == 2:
 					sum1 += 11
 					continue
			
			if check2 == check3 == 1:
				got += 1
 				if got == 2:
 					sum1 += 12
 					continue
			

 		return sum1				
 		'''
 					

t = int(raw_input())
re = Undiv(t)
print re.getsum(t) 		

'''Problem name - Tandem'''

a = raw_input()
length = len(a)
end = length/3
boring = 0
inter = 0
i = 3
while i <= length:
	
	for j in xrange(0, length - i + 1):

		sub = a[j:j+i]
		s_len = i/3
		#print sub[:s_len], sub[s_len:2*s_len], sub[2*s_len:]

		if sub[:s_len] == sub[s_len :2*s_len] and sub[:s_len] == sub[2*s_len:]:

			#print 'sub'
			boring += 1
			#print j,i,  sub[0]

			if j + i >= length:
				
				inter += 1
				continue

			if a[i + j] != sub[0]:

				#print 'int'
				inter += 1			

	i += 3 

print inter, boring - inter	
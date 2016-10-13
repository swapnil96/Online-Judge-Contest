
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
t = int(raw_input())
b = raw_input()
y = int(b[:2])
g = int(b[3:])
#print y, g	
fin = ''
if t == 12:
	if y == 0:
		fin += '01'

	elif y > 12:
		if b[1] == '0':
			fin += '10'

		else:	
			fin += '0' + b[1]

	else:
		fin += b[0] + b[1]

	fin += ':'

	if g >= 60:
		fin += '5' + b[4]				 

	else:
		fin += b[3] + b[4]

else:
	if y > 23:
		fin += '1' + b[1]

	else:
		fin += b[0] + b[1]

	fin += ':'

	if g >= 60:
		fin += '5' + b[4]	

	else:
		fin += b[3] + b[4]	
		
print fin					 
	
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

s = raw_input()
length = len(s)
flag = 0

for i in xrange(length / 2):
    if s[i] == s[length - 1 - i]:
        continue
        
    else:
        flag += 1

if flag == 1:
    print "YES"

else:
    if length == 1:
        print "YES"
    
    elif flag == 0 and length % 2 == 1:
        print "YES"

    else:
        print "NO"



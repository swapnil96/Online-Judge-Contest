import collections

#tt = int(raw_input())
a = map(int, raw_input().split())
dic = collections.Counter(a)
b = sum(a)
#print dic
if max(dic.values()) < 2:
	print b# 'asdf'

elif len(dic) == 1:
	print 2*dic.keys()[0]# 'qwe'

else:
	ans = 10**9		 
	for i in dic.keys():
		if dic[i] < 2:
			continue

		if dic[i] == 2:	
			sum1 = b - i*2

		else:
			sum1 = b - i*3

		if sum1 < ans:
			ans = sum1

	print ans
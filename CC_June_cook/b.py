
import collections

tt = int(raw_input())
for i in xrange(tt):
	a = int(raw_input())
	b = map(int, raw_input().split())
	dic = collections.Counter(b)
	le = -1
	bre = -1
	for i in dic:
		if dic[i] >= 2:
			if dic[i] >= 4 and (i > le or i > bre):
				le = i
				bre = i

			elif i > (min(le, bre)):
				if le > bre:
					bre = i

				else:
					le = i

	if le == -1 or bre == -1:
		print -1

	else:
		print le*bre					
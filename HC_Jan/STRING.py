'''Link - https://www.hackerearth.com/january-circuits-17/algorithm/good-string-3/'''

import collections

a = raw_input()
letters = collections.Counter(a)
count = 0
for i in letters:
    if letters[i] > 1:
        count += letters[i] - 1

print count

'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
t = raw_input()
s = map(str, (' '.join(n for n in t)).split())
length = len(s)
ans = 0
i = 0
done = 0
while (i < length - 1):
    if (i != length - 2):
        if ((s[i] == "V") and (s[i+1] == "K")):
            ans += 1
            i = i + 1

        elif (s[i] == "V" and s[i+1] == "V" and s[i+2] == "V" and done == 0):
            ans += 1
            done = 1
            s[i+1] = "K"
            i = i + 1

        elif (s[i] == "K" and s[i+1] == "K" and done == 0):
            ans += 1
            done = 1
            s[i] = "V"
            i = i + 1

    else:
        if ((s[i] == "V") and (s[i+1] == "K")):
            ans += 1
            i = i + 1

        elif (s[i] == "V" and s[i+1] == "V" and done == 0):
            ans += 1
            done = 1
            s[i+1] = "K"
            i = i + 1

        elif (s[i] == "K" and s[i+1] == "K" and done == 0):
            ans += 1
            done = 1
            s[i] = "V"
            i = i + 1

    i += 1

print ans
# print s
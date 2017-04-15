s = map(str, (' '.join(n for n in raw_input())).split())
length = len(s)
t = []
u = []
i = 0
from_idx = 0
to_idx = 0
while True:

    try:
        comp = t[-1]
    
    except:
        comp = "{"

    min_idx = 0
    # print u, t, from_idx

    for j in xrange(from_idx, length):

        if s[j] < comp:
            comp = s[j]
            min_idx = j

        else:
            t.append(s[j])
        
        if s[j] == 'a':
            break

    u.append(comp)
    # for k in xrange(from_idx, min_idx):
    #     # if j != min_idx:
    #     t.append(s[k])

    # print u, t, from_idx, min_idx, j
    if min_idx == length - 1:
        break

    from_idx = min_idx + 1
    i += 1

t.reverse()
for i in xrange(len(t)):
    u.append(t[i])

print ''.join(u)

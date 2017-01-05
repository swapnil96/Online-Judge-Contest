'''Link - https://www.hackerearth.com/december-circuits-16/algorithm/christmas-string/'''

a = raw_input()
length = len(a)
n = int(raw_input())
names = []
for i in xrange(n):
    names.append(raw_input())

count = 0
changes = [0]*length
for i in xrange(n):

    got = 1
    dis = 0
    for j in xrange(length):

        if names[i][j] != a[j] and a[j] != "*":
            dis += 1
            got = 0
            if dis == 1:
                changes[j] += 1
                temp = j
                # print changes, names[i], j, 'swapnil'

            elif dis > 1:
                changes[temp] -= 1
                # print changes, names[i], j, 'das'
                break

    # print changes, names[i]
    if got == 1:
        count += 1

# print changes
print count + max(changes)

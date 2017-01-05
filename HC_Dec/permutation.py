'''Link - https://www.hackerearth.com/december-circuits-16/approximate/christmas-permutation/'''

n = int(raw_input())
fin = []
acc = [0]*n
acc[0] = 1
index = 1
fin.append(1)
for i in xrange(3, n + 1, 2):
    fin.append(i)
    acc[index] += acc[index - 1] + fin[index]
    index += 1

if index & 1 == 0:
    for i in xrange(n, 1, -2):
        if i != index and i != (index + 2):
            fin.append(i)

else:
    for i in xrange(n-1, 1, -2):
        if i != (index + 1) and i != (index + 3):
            fin.append(i)


print acc, index

print ' '.join(map(str, fin))

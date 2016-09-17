def update(i, a, b):
  for i in xrange(i - 1, n):
    prob[i] = (prob[i] * (a/b))/prob[i-1]

n, q = map(int, raw_input().split())
prob = [1.0]*n  
for i in xrange(n):
  a, b = map(int, raw_input().split())
  if i == 0:
    prob[0] = (a + 0.0)/b

  else:   
    prob[i] = prob[i - 1]*(a + 0.0) / b

print prob
query = []
for i in xrange(q):
  query.append(map(int, raw_input().split()))

for i in xrange(q):
  if query[i][0] == 1:
    update(query[i][1], query[i][2], query[i][3])

  else:
    v = prob[query[i][2] - 1]
    b = prob[query[i][1] - 2]
    if b == v:
      print v

    else:
      print v/b  

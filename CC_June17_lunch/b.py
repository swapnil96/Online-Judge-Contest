tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    c = map(int, raw_input().split())
    w = map(int, raw_input().split())
    dic = {}
    curr = 0
    k = 0
    cur_sum = [0]*n
    cur_sum[0] = w[0]
    ans = 0
    for j in xrange(1, n):
        cur_sum[j] = cur_sum[j-1] + w[j]

    for j in xrange(n):
        while k < n:
            try:
                t = dic[c[k]]
                break

            except:
                dic[c[k]] = 1
                k += 1
        
        diff = k - j
        curr = max(curr, diff)
        if j == 0:
            ans = max(ans, cur_sum[k-1] - 0)

        else:
            ans = max(ans, cur_sum[k-1] - cur_sum[j-1])

        # print j, k
        dic.pop(c[j], None)
    
    # print curr, ans, cur_sum
    print ans
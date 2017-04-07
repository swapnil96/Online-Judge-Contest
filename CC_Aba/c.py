'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''
n, k = map(int, raw_input().split())
dic = {}
for i in xrange(n):
    dic[i] = []

for i in xrange(n-1):
    f1, f2 = map(int, raw_input().split())
    dic[f1-1].append(f2-1)


def rec(i):

    for j in dic[i]:
        curr_max = i
        curr_min = i
        if (abs(j-i) <= k):
            ans += 1

        rec(j)


rec(0)

# for i in xrange(n-1):
#     curr_max = i
#     curr_min =
#     for j in dic[i]:
#         if j > curr_max:
#             curr_max = j
#
#         if j < curr_min:
#             curr_min = j
#
#         if (abs(i - j) <= k):
#             ans += 1


def overlap(min1, max1, min2, max2):
    return max(0, min(max1, max2) - max(min1, min2))

a = map(int, raw_input().split())
ans = overlap(a[0], a[1], a[2], a[3]) + 1
if ans != 0:
	if a[4] >= max(a[0], a[2]) and a[4] <= min(a[1], a[3]):
		ans -= 1

print ans		

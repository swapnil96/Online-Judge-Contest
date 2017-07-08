import math
n, a = map(int, raw_input().split())
angle = ((n-2)*180)/n
v1 = 1
v2 = 1
v3 = 2*math.sin(math.radians(angle/2))
mini = 10**9
for i in xrange(n-2):
    a1 = math.acos((v2*v2 + v3*v3 - v1*v1)/(2*v2*v3))/math.pi * 180
    a2 = math.acos((v3*v3 + v1*v1 - v2*v2)/(2*v3*v1))/math.pi * 180
    a3 = math.acos((v1*v1 + v2*v2 - v3*v3)/(2*v1*v2))/math.pi * 180
    temp = abs(a - a1)
    if temp < mini:
        mini = temp
        ans1 = 1
        ans2 = i + 3
        ans3 = i + 2
    
    temp = abs(a - a2)
    if temp < mini:
        mini = temp
        ans1 = i + 3
        ans2 = 1
        ans3 = i + 2
    
    temp = abs(a - a3)
    if temp < mini:
        mini = temp
        ans1 = i
        ans2 = i + 2
        ans3 = 1
    
    v1 = v3
    v2 = 1
    v3 = math.sqrt(v1*v1 + v2*v2 - 2*v1*v2*math.cos(math.radians(angle - a1)))

print ans1, ans2, ans3
    
    
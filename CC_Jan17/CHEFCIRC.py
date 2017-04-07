'''Link - https://www.codechef.com/JAN17/problems/CHEFCIRC'''

n, m = map(int, raw_input().split())
points = []
for i in xrange(n):
    points.append(map(float, raw_input().split()))

fin = []
ans = 10**9
got = 0
for i in xrange(n):
    x1, y1 = points[i][0], points[i][1]
    for j in xrange(i+1, n):
        x2, y2 = points[j][0], points[j][1]
        dist1 = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
        if got == 1 and dist1 > 2*ans:
            continue

        if x2 == x1:
            m_a = "infi"

        else:
            m_a = (y2 - y1)/(x2 - x1)

        for k in xrange(j+1, n):
            x3, y3 = points[k][0], points[k][1]

            dist2 = ((x2 - x3)**2 + (y2 - y3)**2)**(0.5)
            if got == 1 and dist2 > 2*ans:
                continue

            dist3 = ((x1 - x3)**2 + (y1 - y3)**2)**(0.5)
            if got == 1 and dist3 > 2*ans:
                continue

            if x3 == x2:
                m_b = "infi"

            else:
                m_b = (y3 - y2)/(x3 - x2)

            if m_a == m_b:
            	continue

            if m_a == "infi" and m_b != "infi":
                cen_x = ((y1 - y3)/2.0)*(-1*m_b) + (x2 + x3)/2.0
                cen_y = (y1 + y2)/2.0

            elif m_b == "infi" and m_a != "infi":
                cen_x = ((y3 - y1)/2.0)*(-1*m_a) + (x1 + x2)/2.0
                cen_y = (y2 + y3)/2.0

            elif m_b == "infi" and m_a == "infi":
                continue

            else:
                cen_x = ((m_a*m_b)*(y1 - y3) + m_b*(x1 + x2) - m_a*(x2 + x3))/(2*(m_b - m_a))
                cen_y = -(1.0/m_a)*(cen_x - ((x1 + x2)/2.0)) + (y1 + y2)/2.0

            # print cen_x, cen_y
            rad = ((cen_x - x3)**2 + (cen_y - y3)**2)**(0.5)
            if rad > ans:
                continue

            count = 0
            for l in xrange(n):
                temp_x, temp_y = points[l][0], points[l][1]
                dist = ((cen_x - temp_x)**2 + (cen_y - temp_y)**2)**(0.5)
                if dist <= rad:
                    count += 1

            if count >= m:
                got = 1
                ans = min(ans, rad)
                # fin.append(rad)

print ans

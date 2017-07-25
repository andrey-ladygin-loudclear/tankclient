from math import atan, fabs

def check(points, check_point):
    sum = 0
    px = check_point[0]
    py = check_point[1]

    for k in range(len(points)):
        x1 = points[k][0] - px
        y1 = points[k][1] - py
        print(x1)

        try:
            x2 = points[k + 1][0] - px
            y2 = points[k + 1][1] - py
        except IndexError:
            x2 = points[0][0] - px
            y2 = points[0][1] - py

        s1 = (x1*x1 + y1*y1 - x2*x1 - y2*y1)
        d1 = (x1*y2 - x2*y1) + 0.0000001
        s2 = (x2*x2 + y2*y2 - x2*x1 - y2*y1)
        d2 = (x1*y2 - x2*y1) + 0.0000001
        sum += atan(s1/d1) + atan(s2/d2)

    print('RESILT: ' + str(fabs(sum)))
    return fabs(sum) > 0.01

# print(check([
#     (10, 10),
#     (20, 10),
#     (20, 20),
#     (10, 20),
# ], (20, 20)))
#
# print(check([
#     (10, 10),
#     (20, 10),
#     (20, 20),
#     (10, 20),
# ], (15, 15)))

'''
for point in points:

    x1 = 42 - px
    y1 = 42 - py

    x2 = 42 - px
    y2 = 10 - py

    x3 = 10 - px
    y3 = 10 - py

    x4 = 10 - px
    y4 = 42 - py

    s1 = (x1*x1 + y1*y1 - x2*x1 - y2*y1)
    d1 = (x1*y2 - x2*y1)
    s2 = (x2*x2 + y2*y2 - x2*x1 - y2*y1)
    d2 = (x1*y2 - x2*y1)
    #d1 = max(d1, 1)
    #d2 = max(d2, 1)
    sum += atan(s1/d1) + atan(s2/d2)

    s1 = (x2*x2 + y2*y2 - x3*x2 - y3*y2)
    d1 = (x2*y3 - x3*y2)
    s2 = (x3*x3 + y3*y3 - x3*x2 - y3*y2)
    d2 = (x2*y3 - x3*y2)
    #d1 = max(d1, 1)
    #d2 = max(d2, 1)
    sum += atan(s1/d1) + atan(s2/d2)

    s1 = (x3*x3 + y3*y3 - x4*x3 - y4*y3)
    d1 = (x3*y4 - x4*y3)
    s2 = (x4*x4 + y4*y4 - x4*x3 - y4*y3)
    d2 = (x3*y4 - x4*y3)
    #d1 = max(d1, 1)
    #d2 = max(d2, 1)
    sum += atan(s1/d1) + atan(s2/d2)

    s1 = (x4*x4 + y4*y4 - x1*x4 - y1*y4)
    d1 = (x4*y1 - x1*y4)
    s2 = (x1*x1 + y1*y1 - x1*x4 - y1*y4)
    d2 = (x4*y1 - x1*y4)
    #d1 = max(d1, 1)
    #d2 = max(d2, 1)
    sum += atan(s1/d1) + atan(s2/d2)
    print(fabs(sum) > 0.01)
    '''



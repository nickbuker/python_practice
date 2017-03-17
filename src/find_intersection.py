from __future__ import division


def inter(xa1, xa2, ya1, ya2, xb1, xb2, yb1, yb2):
    # If both segments are vertical
    if vert(xa1, xa2) and vert(xb1, xb2):
        if between(ya1, ya2, yb1):
            return xb1, yb1
        if between(ya1, ya2, yb2):
            return xb2, yb2
        else:
            return "No Intercept"
    # If the first segment is vertical
    if vert(xa1, xa2):
        mb, bb = slope_int(xb1, xb2, yb1, yb2)
        i_y = mb * xa1 + bb
        if between(xb1, xb2, xa1) and between(yb1, yb2, i_y) and between(ya1, ya2, i_y):
            return xa1, i_y
        else:
            return "No Intercept"
    # If the second segment is vertical
    if vert(xb1, xb2):
        ma, ba = slope_int(xa1, xa2, ya1, ya2)
        i_y = ma * xb1 + ba
        if between(xa1, xa2, xb1) and between(ya1, ya2, i_y) and between(yb1, yb2, i_y):
            return xb1, i_y
        else:
            return "No Intercept"
    # Find slope and y-intercepts for both linear equations
    ma, ba = slope_int(xa1, xa2, ya1, ya2)
    mb, bb = slope_int(xb1, xb2, yb1, yb2)
    # If segments are parallel
    if ma == mb and ba != bb:
        return "No Intercept"
    if ma == mb and ba == bb:
        if between(xa1, xa2, xb1):
            return xb1, yb1
        if between(xa1, xa2, xb2):
            return xb2, yb2
        else:
            return "No Intercept"
    # Find theoretical intersection point
    i_x = (bb - ba) / (ma - mb)
    i_y = ma * i_x + ba
    # Determine if intersection point is within the segments
    if (between(xa1, xa2, i_x) and between(xb1, xb2, i_x) and
            between(ya1, ya2, i_y) and between(yb1, yb2, i_y)):
        return i_x, i_y
    else:
        return "No Intercept"


def vert(x1, x2):
    if x1 == x2:
        return True


def slope_int(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b


def between(p1, p2, pi):
    if p1 <= pi <= p2 or p2 <= pi <= p1:
        return True
    else:
        return False

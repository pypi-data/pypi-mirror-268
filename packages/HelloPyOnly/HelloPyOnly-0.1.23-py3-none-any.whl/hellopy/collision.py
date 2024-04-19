from hellopy.mouse import mouse
from hellopy.util import *


__all__ = ['CollisionComponent']

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
def cross_product (x1, y1, x2, y2, x3, y3):
    """ 叉乘
    vector 1: x1, y1, x2, y2
    vector 2: x1, y1, x3, y3
    """
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def line_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    """ 判断两条线段是否交叉 """
    # out of the rect
    if min(x1, x2) > max(x3, x4) or max(x1, x2) < min(x3, x4) or \
       min(y1, y2) > max(y3, y4) or max(y1, y2) < min(y3, y4):
        return False

    # same slope rate
    if ((y1 - y2) * (x3 - x4) == (x1 - x2) * (y3 - y4)):
        return False

    if cross_product(x3, y3, x2, y2, x4, y4) * cross_product(x3, y3, x4, y4, x1, y1) < 0 or \
       cross_product(x1, y1, x4, y4, x2, y2) * cross_product(x1, y1, x2, y2, x3, y3) < 0:
        return False

    # get collide point
    b1 = (y2 - y1) * x1 + (x1 - x2) * y1
    b2 = (y4 - y3) * x3 + (x3 - x4) * y3
    D = (x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1)
    D1 = b2 * (x2 - x1) - b1 * (x4 - x3)
    D2 = b2 * (y2 - y1) - b1 * (y4 - y3)

    return Point(D1 / D, D2 / D)

def lines_cross(g1, g2):
    for i in range(0, len(g1.points)):
        x1 = g1.points[i-1][0]
        y1 = g1.points[i-1][1]
        x2 = g1.points[i][0]
        y2 = g1.points[i][1]
        for i in range(0, len(g2.points)):
            x3 = g2.points[i-1][0]
            y3 = g2.points[i-1][1]
            x4 = g2.points[i][0]
            y4 = g2.points[i][1]
            p = line_cross(x1, y1, x2, y2, x3, y3, x4, y4)
            if p: return p

def point_in_points(p, g2):
    x = p[0]
    y = p[1]
    cross_count = 0
    for i in range(0, len(g2.points)):
        x1 = g2.points[i-1][0]
        y1 = g2.points[i-1][1]
        x2 = g2.points[i][0]
        y2 = g2.points[i][1]
        if (x1 < x and x2 < x) or (y1-y)*(y2-y) > 0 or (y1==y2) or (y2==y):
            continue
        cross_x = x1 - (x1-x2)*(y1-y)/(y1-y2)
        if(cross_x >= x):
            cross_count += 1
    return cross_count % 2

def points_in_points(g1, g2):
    for i in range(0, len(g1.points)):
        x = g1.points[i][0]
        y = g1.points[i][1]
        rc = g2.get_rect()

        # outside the collide rect
        if(x < rc[0] or x > (rc[0]+rc[2]) or y < rc[1] or y > (rc[1]+rc[3])):
            continue

        if(point_in_points((x, y), g2)):
            return Point(x, y)
         
    return False

# def shape_clicked(shape):
#     shape.transform.update_points(shape.points)
#     return point_in_points((mouse.x, mouse.y), shape.transform)



class CollisionComponent():
    """ 碰撞图形
    将任意图形转换为多边形进行判断，图形需要拥有points属性

    按照以下步骤进行判断
    1. 如果图形的外接矩形没有碰撞，返回False
    2. 如果图形的点在目标图形内，返回这个点
    3. 如果图形的边和目标图形的边相交，返回相交点
    4. 返回False

    """

    # def update_collision_rect(self):
    #     """ 获取外接矩形 """
    #     self.min_x = min(self.points[::2])
    #     self.max_x = max(self.points[::2])
    #     self.min_y = min(self.points[1::2])
    #     self.max_y = max(self.points[1::2])

    def collide(self, g2):
        """ 判断图形是否碰到了另外一个图形 """
        g1 = self
        
        g1.update_points()
        g2.update_points()

        if not (g1.points and g2.points):
            return False

        # t1 = g1.transform
        # t2 = g2.transform

        

        # t1.update_points(g1.points)
        # t2.update_points(g2.points)

        # # 更新外接矩形
        # t1.update_collision_rect()
        # t2.update_collision_rect()

        # simple collide rect
        r1 = g1.get_rect()
        r2 = g2.get_rect()
        if not (r1[0] < (r2[0]+r2[2]) and (r1[0]+r1[2]) > r2[0] and r1[1] < (r2[1]+r2[3]) and (r1[1]+r1[3]) > r2[1]):
            return False

        return points_in_points(g1, g2) or points_in_points(g2, g1) or lines_cross(g1, g2)

    # def on_press(self, f):
    #     """ 注册on_press函数，当图形被点击时，触发func函数 """
    #     self._press = f

    # def on_click(self, f):
    #     self._press = f

    # def on_right_press(self, f):
    #     self._right_press = f

    # def on_right_click(self, f):
    #     self._right_press = f


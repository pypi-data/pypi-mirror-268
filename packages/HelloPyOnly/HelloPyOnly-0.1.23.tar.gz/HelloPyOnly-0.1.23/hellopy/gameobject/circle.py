import pygame
from hellopy.gameobject.gameobject import GameObject, rotate_point
from hellopy.window import window
from math import sin, cos, pi, sqrt

# 圆形函数
def circle(x=100,y=100,radius=50,color="red"):
    pygame.draw.circle(window.screen,color,(x,y),radius)

# 圆形类
class Circle(GameObject):
    def __init__(self,x=100,y=100,radius=50,color="red"):  
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
        self.points = self.update_points()
        self.angle = 0
        self.scale = 1
        self.line_width = 1
        super().__init__(self.get_rect())
    def update_points(self):
        """ 圆的近似图形：正多边形 """
        n = 72
        d = pi * 2 / n
        x, y, r = self.x, self.y, self.r
        nps = []
        for i in range(n):
            nps.append(((x + r * sin(d * i)), (y + r * cos(d * i))))
        self.points = nps.copy()
    def get_rect(self):
        return (self.x-self.r,self.y-self.r,self.r,self.r)
    def draw(self):
        pygame.draw.circle(window.screen,self.color,(self.x,self.y),self.r)
    def stroke(self):
        pygame.draw.circle(window.screen,self.color,(self.x,self.y),self.r,self.line_width)
    def rotate(self,angle=90,rotate_center=None):
        # 旋转一个角度
        rc = (self.x, self.y)
        if rotate_center != None:
            rc = rotate_center
        nc = rotate_point(rc, (self.x, self.y), angle) 
        self.x = nc[0]
        self.y = nc[1]
        self.angle = (self.angle + angle) % 360
    def rotate_to(self,angle=90,rotate_center=None):
        # 旋转到某个角度       
        a = (angle - self.angle)
        rc = (self.x, self.y)
        if rotate_center != None:
            rc = rotate_center
        nc = rotate_point(rc, (self.x, self.y), a) 
        self.x = nc[0]
        self.y = nc[1]
        self.angle = angle % 360
    def set_scale(self,scale=1):
        self.r = self.r * (scale/self.scale)
        self.scale = scale
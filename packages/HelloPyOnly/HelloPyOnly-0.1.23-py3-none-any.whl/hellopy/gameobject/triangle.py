import pygame
from hellopy.gameobject.polygon import Polygon
from hellopy.window import window

# 三角形函数
def triangle(x1=200, y1=100, x2=150, y2=200, x3=250, y3=200, color="green"):
    pygame.draw.polygon(window.screen,color,[(x1,y1),(x2,y2),(x3,y3)])

# 矩形类
class Triangle(Polygon):
    def __init__(self,x1=200, y1=100, x2=150, y2=200, x3=250, y3=200, color="green"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.points=[(self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)]
        super().__init__(self.points,color)
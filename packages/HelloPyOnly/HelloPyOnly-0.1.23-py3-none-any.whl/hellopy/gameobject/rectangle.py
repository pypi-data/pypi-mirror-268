import pygame
from hellopy.gameobject.polygon import Polygon
from hellopy.window import window

# 矩形函数
def rectangle(x=100, y=100, width=200, height=50, color="blue"):
    pygame.draw.rect(window.screen,color,(x-width/2,y-height/2,width,height))

# 矩形类
class Rectangle(Polygon):
    def __init__(self,x=100, y=100, width=200, height=50, color="blue"):
        
        self.points=[(x-width/2,y-height/2),(x+width/2,y-height/2),(x+width/2,y+height/2),(x-width/2,y+height/2)]
        super().__init__(self.points,color)
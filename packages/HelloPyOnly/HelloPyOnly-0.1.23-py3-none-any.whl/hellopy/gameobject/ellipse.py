import pygame
from hellopy.window import window

# 椭圆形函数
def ellipse(x=300, y=250, xr=150,yr=100,color="pink"):
    pygame.draw.ellipse(window.screen,color,(x-xr,y-yr,xr*2,yr*2))

# TODO：椭圆形类

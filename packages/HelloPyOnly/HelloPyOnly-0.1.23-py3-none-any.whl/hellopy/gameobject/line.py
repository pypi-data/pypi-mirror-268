import pygame
from hellopy.gameobject.gameobject import GameObject, rotate_point
from hellopy.window import window

# 直线函数
def line(x1=200, y1=100, x2=150, y2=200, color="green",line_width=1):
    pygame.draw.line(window.screen, color, (x1,y1),(x2,y2),line_width)
    
# 直线类
class Line(GameObject):
    def __init__(self,x1=100,y1=200,x2=180,y2=300,color="red"):
        self.start_point = (x1,y1)
        self.end_point = (x2,y2)
        super().__init__(self.get_rect())
        self.color = color
        self.scale = 1
        self.line_width = 1
        self.angle = 0
    def get_rect(self):
        x = min(self.start_point[0],self.end_point[0])
        y = min(self.start_point[1],self.end_point[1])
        w = max(self.start_point[0],self.end_point[0]) - min(self.start_point[0],self.end_point[0])
        h = max(self.start_point[1],self.end_point[1]) - min(self.start_point[1],self.end_point[1])
        return (x,y,w,h)
    def draw(self):
        pygame.draw.line(window.screen, self.color, self.start_point,self.end_point,self.line_width)    
    def stroke(self):
        pygame.draw.line(window.screen, self.color, self.start_point,self.end_point,self.line_width)
    def get_center(self):
        return ((self.start_point[0]+self.end_point[0])/2,(self.start_point[1]+self.end_point[1])/2)
    def rotate(self,angle=90,rotate_center=None):
        # 旋转一个角度
        rc = self.get_center()
        if rotate_center != None:
            rc = rotate_center
        self.start_point = rotate_point(rc,self.start_point,angle)
        self.end_point = rotate_point(rc,self.end_point,angle)
        self.angle = (self.angle + angle) % 360
    def rotate_to(self,angle=90,rotate_center=None):
        # 旋转到某个角度
        a = (angle - self.angle)
        rc = self.get_center()
        if rotate_center != None:
            rc = rotate_center
        self.start_point = rotate_point(rc,self.start_point,a)
        self.end_point = rotate_point(rc,self.end_point,a)
        self.angle = angle % 360
    def set_scale(self,scale):
        if self.scale == scale:
            return
        sc = scale/self.scale
        rc = self.get_center()
        self.start_point = (rc[0]+(self.start_point[0]-rc[0])*sc,rc[1]+(self.start_point[1]-rc[1])*sc)
        self.end_point = (rc[0]+(self.end_point[0]-rc[0])*sc,rc[1]+(self.end_point[1]-rc[1])*sc)
        self.scale = scale
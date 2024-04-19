import pygame, math, cv2, random, mediapipe as mp, numpy as np
from hellopy.gameobject.sprite import *
from hellopy.gameobject.circle import circle
from hellopy.gameobject.line import line
from hellopy.window import window
from hellopy.mouse import mouse
from hellopy.sound import Sound
window.set_size(1200,800)

__all__ = ["Finger", 'distance', 'draw_hand', 'Loong', 'get_angle', 'move_to','player', 'cap', 'hands', 'bgm', 'sfx']

# 玩家类
class Player():
    def __init__(self):
        self.controller = mouse
        self.score = 0
        self.mode = 0
        self.finger_nodes = []

# 汤圆
class RiceBall(Sprite):
    def __init__(self):
        self.ox = random.randint(50,window.w-50)
        self.oy = random.randint(100,window.h-50)
        self._src = "https://pic.imgdb.cn/item/65d310a09f345e8d036e25ed.png"
        self.img = pygame.image.load(rss.get(self._src))
        self._w = 40
        self._h = 40
        self.x = self.ox
        self.y = self.oy
        super().__init__(self.x,self.y,self._w,self._h,self._src)
    def draw(self):
        super().draw()
    def reset(self):
        self.x = random.randint(50,window.w-50)
        self.y = random.randint(100,window.h-50)
# 龙
class Loong():
    def __init__(self,body_length=2):
        self.head = Sprite(900,500,90,80,"https://pic.imgdb.cn/item/65d01dad9f345e8d03984642.png")
        self.speed = 20
        self.score = 0
        self._body_length = body_length
        self.head.x_speed = 1
        self.head.y_speed = 0
        self.bodys = [self.head]
        for i in range(self._body_length):
            new_body = Sprite(self.bodys[-1].x-50,self.bodys[-1].y,60,45,"https://pic.imgdb.cn/item/65d01dac9f345e8d03984400.png")
            self.bodys.append(new_body)
        self.tail = Sprite(self.bodys[-1].x-65,self.bodys[-1].y,110,45,"https://pic.imgdb.cn/item/65d19e369f345e8d03507793.png")
        self.bodys.append(self.tail)
        self.foot1 = Sprite(100,100,60,120,"https://pic.imgdb.cn/item/65d5b5569f345e8d035dd171.png")
        self.foot2 = Sprite(100,100,60,120,"https://pic.imgdb.cn/item/65d5b5569f345e8d035dd171.png")
    
    # 绘制龙    
    def draw(self):
        self.head_to(self.head)
        for item in self.bodys[-1::-1]:
            item.draw()
        self.foot1.draw()
        self.foot2.draw()
    
    # 移动龙
    def head_to(self, target):
        if distance(self.head,target) > 40:
            move_to(self.head,target,self.speed)
        for i in range(1,len(self.bodys)-1):
            if distance(self.bodys[i],self.bodys[i-1]) > 50:
                move_to(self.bodys[i],self.bodys[i-1],self.speed)
        if distance(self.bodys[-1],self.bodys[-2])>65:
            move_to(self.bodys[-1],self.bodys[-2],self.speed)
        a = len(self.bodys) // 3 - 1 
        if a < 1:
            a = 1
        self.foot1.x = self.bodys[a].x
        self.foot1.y = self.bodys[a].y
        self.foot1.angle = self.bodys[a].angle
        self.foot1.rotate_to(self.foot1.angle)

        b = len(self.bodys) // 3 * (-1) -1
        self.foot2.x = self.bodys[b].x
        self.foot2.y = self.bodys[b].y
        self.foot2.angle = self.bodys[b].angle
        self.foot2.rotate_to(self.foot2.angle)
    
    #  
    # 增加龙的长度
    @ property
    def body_length(self):
        return self._body_length
    @ body_length.setter
    def body_length(self, n):
        bl = n
        if bl < 2:
            bl = 2
        if self._body_length > bl:
            x = self._body_length - n
            self.bodys[-1].x = self.bodys[-1-x].x
            self.bodys[-1].y = self.bodys[-1-x].y
            self.bodys[-1].angle = self.bodys[-x].angle
            self.bodys = self.bodys[:(-x)] + [self.bodys[-1]]
            self._body_length = bl
            return self._body_length
        while self._body_length < bl:
            self.bodys.insert(-1,Sprite(self.bodys[-1].x,self.bodys[-1].y,60,45,"https://pic.imgdb.cn/item/65d01dac9f345e8d03984400.png"))
            self._body_length += 1
        return self._body_length

# 手指控制器
class FingerPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
# 计算距离
def distance(a,b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)

# 绘制手部形态
def draw_hand(h):
    player.finger_nodes = []
    for i in range(len(h.landmark)):
        x = int(h.landmark[i].x * window.w)
        y = int(h.landmark[i].y * window.h)
        player.finger_nodes.append(FingerPoint(x,y))
    link_dots(player.finger_nodes,[0,1,2,3,4])
    link_dots(player.finger_nodes,[5,6,7,8])
    link_dots(player.finger_nodes,[9,10,11,12])
    link_dots(player.finger_nodes,[13,14,15,16])
    link_dots(player.finger_nodes,[17,18,19,20])
    link_dots(player.finger_nodes,[1,5,9,13,17,0])
    for item in player.finger_nodes:
        circle(item.x,item.y,5,"lightsalmon")

# 连接手部的关键点
def link_dots(d,dots):
    for i in range(len(dots)-1):
        line(d[dots[i]].x,d[dots[i]].y,d[dots[i+1]].x,d[dots[i+1]].y,"brown1",3)

# 坐标换算角度
def get_angle(vx,vy):
    return np.degrees(np.arctan2(vy, vx))

# 向某个物体按特定速度移动
def move_to(start,target,speed):
    if start.x == target.x and start.y == target.y:
        return
    vx = (target.x - start.x) / distance(start,target) * speed
    vy = (target.y - start.y) / distance(start,target) * speed
    start.x += vx
    start.y += vy
    angle = get_angle(vx, vy)
    start.rotate_to(angle)  

player = Player()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

bgm = Sound("https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/sound/festival_bg.mp3")
bgm.set_volume(0.1)
sfx = Sound("https://r.leaplearner.com/a/1/gainTools.mp3")
sfx.set_volume(1.0)
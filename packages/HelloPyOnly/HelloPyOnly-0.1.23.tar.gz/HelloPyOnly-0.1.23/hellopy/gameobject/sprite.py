import pygame
from hellopy.gameobject.rectangle import Rectangle
from hellopy.gameobject.gameobject import GameObject, rotate_point
from hellopy.collision import CollisionComponent
from hellopy.window import window
from hellopy.resource import rss

cache_images = {}

# 绘制图片
def image(x=100, y=200, width=100,height=100,src="./hellopy/src/images/HelloScienceLogo.png"):
    img = pygame.image.load(rss.get(src))
    img = pygame.transform.scale(img,(width,height))
    window.screen.blit(img,(x-width/2, y-height/2))

# 精灵类
class Sprite(GameObject, pygame.sprite.Sprite, CollisionComponent):
    def __init__(self,x=100, y=200, width=None,height=None,src="./hellopy/src/images/HelloScienceLogo.png"):
        self.ox = x
        self.oy = y
        self.img = pygame.image.load(rss.get(src))
        self._w = width or self.img.get_width()
        self._h = height or self.img.get_height()
        self.x = x
        self.y = y
        self._src = src
        self.mask =  pygame.mask.from_surface(self.img.convert_alpha())
        mask_w, mask_h = self.mask.get_size()
        points = []
        for y in range(0,mask_h-1,5):
            for x in range(0,mask_w-1,5):
                if self.mask.get_at((x, y)):
                    if (
                        x == 0
                        or x == width - 1
                        or y == 0
                        or y == height - 1
                        or not self.mask.get_at((x - 1, y))
                        or not self.mask.get_at((x + 1, y))
                        or not self.mask.get_at((x, y - 1))
                        or not self.mask.get_at((x, y + 1))
                    ):
                        points.append((x, y))
        for x in range(0,mask_w-1,5):
            for y in range(0,mask_h-1,5):
                if self.mask.get_at((x, y)):
                    if (
                        x == 0
                        or x == width - 1
                        or y == 0
                        or y == height - 1
                        or not self.mask.get_at((x - 1, y))
                        or not self.mask.get_at((x + 1, y))
                        or not self.mask.get_at((x, y - 1))
                        or not self.mask.get_at((x, y + 1))
                    ):
                        points.append((x, y))
        points = [(self.x-self.w/2, self.y-self.h/2),(self.x+self.w/2, self.y-self.h/2),(self.x+self.w/2, self.y+self.h/2),(self.x-self.w/2, self.y+self.h/2)]
        self.points = points
        
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        super().__init__(self.get_rect())
        self.color = "blue"
        self.scale = 1
        self.line_width = 1
        self.angle = 0
        self.show_rect= False

        self.mask =  pygame.mask.from_surface(self.img)
        self.mask = self.mask.to_surface()
        self.mask.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_MULT)
        


    @property
    def w(self):
        return self._w
    @w.setter
    def w(self,w):
        self._w = w
        pygame.transform.scale(self.img,(self._w,self._h))
    @property
    def h(self):
        return self._h
    @h.setter
    def h(self,h):
        self._h = h
        pygame.transform.scale(self.img,(self._w,self._h))
    @property
    def src(self):
        return self._src
    @src.setter
    def src(self, src):
        if src not in cache_images:
            try:
                file_name = rss.get(src)
                if file_name[-4:] == ".gif":
                    print("Can't use GIF resource.")
                    pass
                else:
                    img = pygame.image.load(file_name)
            except pygame.image.codecs.ImageDecodeException:
                import os, sys
                print("Couldn't load image, please delete the picture and retry.")
                print("Error picture: {}\\{}".format(os.getcwd(), rss.get(src)))
                sys.exit()

            cache_images[src] = img
        self.src = src
        self.img = cache_images[src]
        
    def get_rect(self):
        x_list = []
        y_list = []
        for dot in self.points:
            x_list.append(dot[0])
            y_list.append(dot[1])
        return (min(x_list),min(y_list),max(x_list)-min(x_list),max(y_list)-min(y_list))
    def update_points(self):
        points = [(self.x-self.w/2, self.y-self.h/2),(self.x+self.w/2, self.y-self.h/2),(self.x+self.w/2, self.y+self.h/2),(self.x-self.w/2, self.y+self.h/2)]
        nps = []
        for p in points:
            nps.append(rotate_point((self.x,self.y),p,self.angle))
        self.points = nps.copy()
    def draw(self):
        self.update_points()
        window.screen.blit(self.img,(self.x-self.display_rect[2]/2,self.y-self.display_rect[3]/2))
        if self.show_rect:
            pygame.draw.polygon(window.screen,self.color,self.points,self.line_width)
    def rotate(self, angle=0, center=None):
        self.angle = (self.angle + angle) % 360
        self.r_center = (self.x,self.y)
        if center != None:
            self.r_center = center    
        nps = []
        for p in self.points:
            nps.append(rotate_point(self.r_center,p,angle))
        self.points = nps.copy()
        self.display_rect = self.get_rect()
        self.img = pygame.image.load(rss.get(self.src))
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.img = pygame.transform.rotate(self.img, -self.angle)
        fp = rotate_point(self.r_center,(self.x,self.y),angle)
        self.x = fp[0]
        self.y = fp[1]
        return self.points
    def rotate_to(self, angle=0, center=None):
        a = (angle - self.angle)%360
        self.angle = (angle) % 360
        self.r_center = (self.x,self.y)
        if center != None:
            self.r_center = center    
        nps = []
        for p in self.points:
            nps.append(rotate_point(self.r_center,p,a))
        self.points = nps.copy()
        self.display_rect = self.get_rect()
        self.img = pygame.image.load(rss.get(self.src))
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.img = pygame.transform.rotate(self.img, -self.angle)
        fp = rotate_point(self.r_center,(self.x,self.y),angle)
        self.x = fp[0]
        self.y = fp[1]
        return self.points
    def set_scale(self,scale):
        if self.scale == scale:
            return
        sc = scale/self.scale
        nps = []
        for p in self.points:
            rc = (self.x,self.y)
            nps.append((rc[0]+(p[0]-rc[0])*sc,rc[1]+(p[1]-rc[1])*sc))
        self.points = nps.copy()
        self.w = self.w * sc
        self.h = self.h * sc
        self.scale = scale
        self.img = pygame.image.load(self.src)
        self.img = pygame.transform.scale(self.img,(self.w,self.h))
        self.img = pygame.transform.rotate(self.img, self.angle)
    # def mask_collide(self, other):


    # def get_center(self):
    #     rt = self.get_rect()
    #     return (rt[0] + rt[2]/2, rt[1] + rt[3]/2)
    # def rotate(self,angle=90,rotate_center=None):
    #     # 旋转一个角度
    #     rc = self.get_center()
    #     if rotate_center != None:
    #         rc = rotate_center
    #     nps = []
    #     for p in self.points:
    #         nps.append(rotate_point(rc,p,angle))
    #     self.points = nps.copy()
    #     self.angle = (self.angle + angle) // 360
    # def rotate_to(self,angle=90,rotate_center=None):
    #     # 旋转到某个角度
    #     a = (angle - self.angle)
    #     rc = self.get_center()
    #     if rotate_center != None:
    #         rc = rotate_center
    #     nps = []
    #     for p in self.points:
    #         nps.append(rotate_point(rc,p,a))
    #     self.points = nps.copy()
    #     self.angle = angle // 360
    

    # def __init__(self,x=250,y=200,width=100,height=100,src='./hellopy/src/images/HelloScienceLogo.png',collider_scale = 0.8):
    #     self.w = width
    #     self.h = height
    #     self.x = x
    #     self.y = y
    #     self.sx = x-self.w/2
    #     self.sy = y-self.h/2
    #     super().__init__((self.sx,self.sy,self.w,self.h))
    #     self.src = src
    #     self.img = pygame.image.load(self.src)      
    #     self.img = pygame.transform.scale(self.img,(self.w,self.h))
    #     self.center_x = self.x + self.w / 2
    #     self.center_y = self.y + self.h / 2
    #     self.collider_scale = collider_scale
    # def draw(self):
    #     window.screen.blit(self.img,(self.sx, self.sy))
    # def get_collider(self):
    #     borders = []
    #     self.center_x = self.x + self.w / 2
    #     self.center_y = self.y + self.h / 2
    #     borders.append(self.center_x - self.w / 2 * self.collider_scale) # 左边界
    #     borders.append(self.center_x + self.w / 2 * self.collider_scale) # 右边界
    #     borders.append(self.center_y - self.h / 2 * self.collider_scale) # 上边界
    #     borders.append(self.center_y + self.h / 2 * self.collider_scale) # 下边界
    #     return borders
    # def collide(self, other):
    #     if not isinstance(other, Sprite):
    #         return False
    #     my_borders = self.get_collider()
    #     other_borders = other.get_collider()
    #     if my_borders[0] > other_borders[1]:
    #         return False
    #     elif my_borders[1] < other_borders[0]:
    #         return False
    #     elif my_borders[2] > other_borders[3]:
    #         return False
    #     elif my_borders[3] < other_borders[2]:
    #         return False
    #     return True
    # def rotate(self, angle=0, center=None):
    #     self.angle = (self.angle + angle) // 360
    #     self.img = pygame.image.load(self.src)
    #     rotated_image = pygame.transform.rotate(self.img, self.angle)
    #     ri_rect = rotated_image.get_rect()
    #     self.r_center = (ri_rect.centerx,ri_rect.centery)
    #     if center != None:
    #         self.r_center = center
    #     fp = rotate_point(self.r_center,ri_rect.center,self.angle)
    #     self.x = fp[0] - ri_rect.width/2
    #     self.y = fp[1] - ri_rect.height/2
    #     self.img = rotated_image
    #     return (self.x, self.y, ri_rect.width/2,ri_rect.height/2)
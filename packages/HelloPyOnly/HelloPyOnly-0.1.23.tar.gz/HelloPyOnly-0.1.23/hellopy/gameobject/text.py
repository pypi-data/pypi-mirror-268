import pygame
from hellopy.gameobject.rectangle import Rectangle
from hellopy.resource import rss
from hellopy.window import window


# 绘制文字
def text(text="Hello Science", x=100, y=100, font_size=30, color="black"):
    font = pygame.font.Font(rss.get('https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/msyhl.ttc'), font_size)
    text_render = font.render(text, True, color)
    window.screen.blit(text_render, (x, y))

# 文字类
class Text(Rectangle):
    def __init__(self,text="Hello Science", x=100, y=100, font_size=30, color="black"):
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(rss.get('https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/msyhl.ttc'), self.font_size)
        # self.font = pygame.font.SysFont(None, self.font_size)
        self.x = x
        self.y = y
        self.sx = x
        self.sy = y
        self.color = color
        self.text_align = "left"
        text_render = self.font.render(self.text, True, self.color)
        self.w = text_render.get_width()
        self.h = text_render.get_height()
        super().__init__(self.x, self.y, self.w, self.h, self.color)
    def set_font(self, font_file):
        self.font = pygame.font.Font(rss.get(font_file), self.font_size)
        self.get_rect()
    def get_rect(self):
        text_render = self.font.render(self.text, True, self.color)
        self.set_align(text_render, self.text_align)
        self.w = text_render.get_width()
        self.h = text_render.get_height()
        return (self.sx,self.sy,self.w,self.h)
    def set_align(self,text_render, text_align):
        self.text_align = text_align
        render_width =  text_render.get_width()
        if self.text_align == "middle":
            self.sx = self.x - render_width / 2
            self.sy = self.y
        elif self.text_align == "right":
            self.sx = self.x - render_width
            self.sy = self.y
        else:
            self.sx = self.x
            self.sy = self.y
    def draw(self):
        text_render = self.font.render(self.text, True, self.color)
        self.set_align(text_render, self.text_align)
        window.screen.blit(text_render, (self.sx, self.sy))
    def set_scale(self,scale):
        if self.scale == scale:
            return
        self.font_size = int(self.font_size * (scale/self.scale))
        self.font = pygame.font.SysFont(None, self.font_size)
        text_render = self.font.render(self.text, True, self.color)
        self.w = text_render.get_width()
        self.h = text_render.get_height()
        self.scale = scale
    def rotate(self):
        pass
    def rotate_to(self):
        pass
    def stroke(self):
        pass
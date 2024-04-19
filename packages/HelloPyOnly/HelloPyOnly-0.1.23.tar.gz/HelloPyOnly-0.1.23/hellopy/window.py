import pygame
from hellopy.mouse import mouse
from hellopy.resource import rss

__all__ = ['window', "Window"]

CLOCK = pygame.time.Clock()
# 窗口对象
class Window():
    def __init__(self, width=600, height=400, title="Hello科学少儿编程", icon_src='https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/HelloPyLogo.ico'):
        self.w = width
        self.h = height
        self.screen = pygame.display.set_mode((self.w,self.h))
        self.title = title
        self.icon = pygame.image.load(rss.get(icon_src))
        self.mouse_x = mouse.x
        self.mouse_y = mouse.y
        self.fps = 60
        self.running = True
    
    # 设置窗口标题
    def set_title(self,title):
        self.title = title
        pygame.display.set_caption(self.title)
    
    # 更新鼠标坐标信息
    def update_mouse_pos(self):
        title_text = "{} X:{} Y:{}".format(self.title, mouse.x, mouse.y)
        pygame.display.set_caption(title_text)
    
    # 设置窗口尺寸
    def set_size(self,width,height):
        self.w = width
        self.h = height
        self.screen = pygame.display.set_mode((self.w,self.h))
    
    # 设置窗口图标
    def set_icon(self,icon_src):
        self.icon = pygame.image.load(rss.get(icon_src))
        pygame.display.set_icon(self.icon)
    
    # 显示坐标网格
    def show_axis(self,color="gray",step=50):
        s = step
        for i in range(0,self.w,s):
            pygame.draw.line(self.screen, color, (i,0),(i,self.h))
        for i in range(0,self.h,s):
            pygame.draw.line(self.screen, color, (0,i),(self.w,i))

    # 设置窗口刷新帧率
    def set_fps(self, fps):
        self.fps =fps

    # 清空屏幕
    def clear(self):
        self.screen.fill("black")
    
    # 显示静态窗口
    def show(self,delay_time=0):
        if delay_time>0:
            CLOCK.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 事件：退出游戏
                    window.running = False
                    pass
                if event.type == pygame.MOUSEMOTION:
                    # 事件：鼠标移动
                    mouse.x,mouse.y = event.pos
                    window.update_mouse_pos()
                    pass
            pygame.display.update()
            pygame.time.delay(delay_time)
            return
        while self.running:
            CLOCK.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 事件：退出游戏
                    window.running = False
                    pass
                if event.type == pygame.MOUSEMOTION:
                    # 事件：鼠标移动
                    mouse.x,mouse.y = event.pos
                    window.update_mouse_pos()
                    pass
            pygame.display.update()
        pygame.quit()
        
window = Window()
icon1 = 'https://lldocs-1257261737.cos.ap-shanghai.myqcloud.com/HelloPyLogo.ico'
window.set_icon(rss.get(icon1))
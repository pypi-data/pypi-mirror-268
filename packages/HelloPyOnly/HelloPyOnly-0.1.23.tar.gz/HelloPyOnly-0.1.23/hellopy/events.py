import pygame
from hellopy.window import window
from hellopy.mouse import mouse

__all__ = ['events','detect_events','keydown_event','keyup_event','mousemotion_event','mousedown_event','mouseup_event']


class Event():
    def __init__(self):
        self.registed_events = {}
        self._kd_events = {}
        self._ku_events = {}
        self._mm_events = {}
        self._md_events = {}
        self._mu_events = {}
# 监听事件函数
def detect_events(events):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 事件：退出游戏
            window.running = False
            pass
        if event.type == pygame.KEYDOWN and len(events._kd_events) > 0:
            # 事件：按下键盘按键
            for key,value in events._kd_events.items():
                if event.key == key:
                    value()
            pass
        if event.type == pygame.KEYUP and len(events._ku_events) > 0:
            # 事件：键盘按键松开
            for key,value in events._ku_events.items():
                if event.key == key:
                    value()
            pass
        if event.type == pygame.MOUSEMOTION:
            # 事件：鼠标移动
            mouse.x,mouse.y = event.pos
            window.update_mouse_pos()
            pass
        if event.type == pygame.MOUSEBUTTONDOWN and len(events._md_events) > 0:
            # 事件：鼠标按键按下
            if event.button == 1 and "left" in events._md_events.keys():
                events._md_events["left"]()
            if event.button == 2 and "middle" in events._md_events.keys():
                events._md_events["middle"]()
            if event.button == 3 and "right" in events._md_events.keys():
                events._md_events["right"]()
            pass
        if event.type == pygame.MOUSEBUTTONUP and len(events._mu_events) > 0:
            # 事件：鼠标按键松开
            if event.button == 1:
                events._mu_events["left"]()
            if event.button == 2:
                events._mu_events["middle"]()
            if event.button == 3:
                events._mu_events["right"]()
            pass
events = Event()
# 事件注册函数
# 1-键盘按键按下
def keydown_event(k, f):
    events._kd_events[eval('pygame.'+k)] = f
# 2-键盘按键松开
def keyup_event(k, f):
    events._ku_events[eval('pygame.'+k)] = f
# 3-鼠标移动
def mousemotion_event(k, f):
    events._mm_events[eval('pygame.'+k)] = f
# 4-鼠标按键按下("LEFTBUTTON"-1,"RIGHTBUTTON"-3,"MIDDLEBUTTON"-2)
def mousedown_event(k, f):
    events._md_events[k] = f
# 5-鼠标按键按下
def mouseup_event(k, f):
    events._mu_events[k] = f

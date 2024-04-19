import pygame
from hellopy import rss

__all__ = ['Sound']

class Sound(pygame.mixer.Sound):
    def __init__(self,filename):
        super().__init__(rss.get(filename))
    def play(self, loops=-1):
        lp = loops
        if (lp > -1):
            lp = lp - 1
        else:
            lp = -1
        super().play(loops=lp)
    def stop(self):
        super().stop()
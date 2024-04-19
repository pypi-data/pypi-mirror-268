import pygame

__all__ = ['Key']

class Key():
    def __init__(self,key_name):
        self.key_name = eval('pygame.'+key_name)
    def pressed(self):
        if pygame.key.get_pressed()[self.key_name]:
            return True
        return False
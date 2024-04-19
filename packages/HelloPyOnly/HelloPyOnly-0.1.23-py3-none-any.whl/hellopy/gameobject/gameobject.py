import pygame


def rotate_point(r_center,origin,angle):
    dx = origin[0] - r_center[0]
    dy = origin[1] - r_center[1]
    v2 = pygame.math.Vector2.rotate(pygame.math.Vector2(dx,dy),-angle)
    tx = r_center[0] + v2[0]
    ty = r_center[1] + v2[1]
    return (tx, ty)

class GameObject():
    def __init__(self, display_rect):
        self.display_rect = display_rect
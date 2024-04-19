import pygame
from hellopy.window import window
from hellopy.events import detect_events,events
from hellopy.key import Key

# 运行游戏
CLOCK = pygame.time.Clock()
def run(f):
    while window.running:
        CLOCK.tick(window.fps)
        detect_events(events)
        f()
        pygame.display.update()
    pygame.quit()
import pygame
from level_1 import Level1, Background
pygame.init()
pygame.mixer.init()

infoObject = pygame.display.Info()
WIDTH = int(infoObject.current_w * 0.9)
HEIGHT = int(infoObject.current_h * 0.9)
score = 0

level_1 = Level1(WIDTH, HEIGHT, score)
level_1.start_level()

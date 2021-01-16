import pygame
from level_1 import Level1
import labirinth
from level_3 import Level3
pygame.init()
pygame.mixer.init()

infoObject = pygame.display.Info()
WIDTH = int(infoObject.current_w * 0.9)
HEIGHT = int(infoObject.current_h * 0.9)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра =)")
score = 0
level_1 = Level1(WIDTH, HEIGHT, screen, score)
score = level_1.start_level()
score = labirinth.main(WIDTH, HEIGHT, score)
level_3 = Level3(WIDTH, HEIGHT, screen, score)
score = level_3.start_level()

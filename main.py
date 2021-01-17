import pygame
import loading
from level_1 import Level1
import labirinth
from level_2 import Level2
from level_3 import Level3

pygame.init()
pygame.mixer.init()

# Получение ширины и высоты экрана. От них зависит размер большинства элементов
infoObject = pygame.display.Info()
WIDTH = int(infoObject.current_w * 0.9)
HEIGHT = int(infoObject.current_h * 0.9)
# Создание игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Игра называется "Айдж" =)
pygame.display.set_caption("Айдж")
# Очки в начале игры
score = 0

# Запуск уровня 1
level_1 = Level1(WIDTH, HEIGHT, screen, score)
score = level_1.start_level()

# Загрузка лабиринта
loading.main(screen, WIDTH, HEIGHT)

# Запуск мини-игры "Лабиринт"
# Правила: Управляя белым шаром необходимо как можно быстрее дойти до выхода, избегая красный шар.
score = labirinth.main(WIDTH, HEIGHT, score)

# Запуск уровня 2
level_2 = Level2(WIDTH, HEIGHT, screen, score)
score = level_2.start_level()

# Загрузка уровня 3
loading.main(screen, WIDTH, HEIGHT)
# запуск уровня 3
level_3 = Level3(WIDTH, HEIGHT, screen, score)
score = level_3.start_level()

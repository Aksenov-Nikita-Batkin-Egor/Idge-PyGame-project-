# coding: utf8
import pygame
import time

pygame.init()
pygame.mixer.init()

WIDTH = 2000
HEIGHT = 1000
FPS = 30
frase = 0

text_lvl_1 = ['противник*=)*Делить на ноль можно.',
              'игрок*=)*Согласен / Нельзя',
              'противник*=)*Что ж, ты проиграл / Нет, можно',
              'игрок*=(*Дурак! Нельзя!',
              'противник*=)*Интересно, почему? 6 % 3 = 2; 6 % 1 = 6; 6 % 0.0001 = 60000. '
              'Чем меньше делитель, тем больше будет частное. Ну что скажешь?',
              'игрок*=)*Выучил правило из 5 класса и крутой? / Рассказать правило',
              'противник*=)*Ясно. Давно стал очевиден один факт.',
              '...',
              'противник*=)*Ты так думаешь лишь потому, что тебе так сказали. '
              'Своей головой ты думать видимо не можешь. Ты же знаешь, что если '
              'любое число разделить на себя, то получится единица? Следовательно: 0 / 0 = 1.',
              'игрок*=(*Единица - твоя оценка по матеше.',
              '',
              '',
              '']


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


def judge_1(screen):
    font = pygame.font.Font(None, 33)
    text = font.render("Судья:", True, (255, 127, 80))
    text_x = 100
    text_y = 900
    screen.blit(text, (text_x, text_y))


def rules(screen):
    font = pygame.font.Font(None, 33)
    text = font.render("ЧТОБЫ ВЫБРАТЬ ДЕЙСТВИЕ - НАЖМИТЕ КНОПКИ 1 2 3 4, ЧТОБЫ "
                       "ПЕРЕЛИСТНУТЬ РЕПЛИКУ - НАЖМИТЕ ПРОБЕЛ", True, (255, 127, 80))
    text_x = 100
    text_y = 900
    screen.blit(text, (text_x, text_y))


def show_text(text):
    a = text
    a = list(a)
    count = 0
    if len(a) + 1 > 180:
        for i in range(0, len(a) - 79):
            font = pygame.font.Font(None, 40)
            t = a[0:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = 100
            text_y = 910
            screen.blit(text, (text_x, text_y))
            clock.tick(30)
            pygame.display.flip()
        for i in range(len(a) - 78, len(a) + 3):
            font = pygame.font.Font(None, 40)
            t = a[len(a) - 80:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = 100
            text_y = 950
            screen.blit(text, (text_x, text_y))
            clock.tick(30)
            pygame.display.flip()
    else:
        for i in range(len(a) + 1):
            font = pygame.font.Font(None, 40)
            t = a[0:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = 100
            text_y = 930
            screen.blit(text, (text_x, text_y))
            clock.tick(30)
            pygame.display.flip()


def speak(screen, frase):
    element = text_lvl_1[frase]
    element = element.split('*')
    if element[0] == 'противник':
        screen.blit(bg_1, bg_1_rect)
        screen.blit(enemy_1_common, enemy_1_common_rect)
        pygame.draw.line(screen, BLACK,
                         [0, 980],
                         [2000, 980], 200)
        font = pygame.font.Font(None, 33)
        text = font.render("Противник:", True, (255, 127, 80))
        text_x = 100
        text_y = 890
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        show_text(element[-1])
    else:
        screen.blit(bg_2, bg_2_rect)
        screen.blit(main_common, main_common_rect)
        pygame.draw.line(screen, BLACK,
                         [0, 980],
                         [2000, 980], 200)
        font = pygame.font.Font(None, 33)
        text = font.render("ГГ:", True, (255, 127, 80))
        text_x = 100
        text_y = 890
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        show_text(element[-1])


BLACK = (0, 0, 0)

pygame.mixer.music.load('GAME_FIGHT.mp3')
pygame.mixer.music.play()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
start = True

bg = Background('фон-зал суда.jpg', [0, 0])
bg = pygame.transform.scale(
    bg.image, (2000,
               1000))
bg_rect = bg.get_rect(
    center=(1000, 500))

bg_1 = Background('фон_противника.jpg', [0, 0])
bg_1 = pygame.transform.scale(
    bg_1.image, (2000,
                 1000))
bg_1_rect = bg_1.get_rect(
    center=(1000, 500))

bg_2 = Background('фон_героя.jpg', [0, 0])
bg_2 = pygame.transform.scale(
    bg_2.image, (2000,
                 1000))
bg_2_rect = bg_2.get_rect(
    center=(1000, 500))

main_common = Background('main_common.PNG', [0, 0])
main_common = pygame.transform.scale(
    main_common.image, (600,
                        600))
main_common_rect = main_common.get_rect(
    center=(400, 600))

enemy_1_common = Background('common-enemy.PNG', [0, 0])
enemy_1_common = pygame.transform.scale(
    enemy_1_common.image, (600,
                           600))
enemy_1_common_rect = enemy_1_common.get_rect(
    center=(1500, 600))

old_man = Background('judge-smiling.png', [0, 0])
old_man = pygame.transform.scale(
    old_man.image, (600,
                    600))
old_man_rect = old_man.get_rect(
    center=(400, 600))


while running:
    if start:
        screen.fill(BLACK)
        clock.tick(FPS)
        screen.blit(bg, bg_rect)
        screen.blit(old_man, old_man_rect)
        pygame.draw.line(screen, BLACK,
                         [0, 980],
                         [2000, 980], 200)
        rules(screen)
        pygame.display.flip()
        time.sleep(3)
        pygame.draw.line(screen, BLACK,
                         [0, 980],
                         [2000, 980], 200)
        judge_1(screen)

        pygame.display.flip()

        show_text('Кто выиграет в споре - получит свободу и право сыграть в Великий лабиринт.')

        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speak(screen, frase)
                frase += 1

# coding: utf8
import pygame
import time

pygame.init()
pygame.mixer.init()

infoObject = pygame.display.Info()
WIDTH = int(infoObject.current_w * 0.9)
HEIGHT = int(infoObject.current_h * 0.9)
FPS = 30
frase = 0
score = 0

text_lvl_1 = ['противник*=)*Делить на ноль можно.',
              'игрок*=)*1 - Согласен / 2 - Нельзя',
              'противник*=)*1 - Что ж, ты проиграл / 2 - Нет, можно',
              'игрок*=(*Дурак! Нельзя!',
              'противник*=)*Интересно, почему? 6 % 3 = 2; 6 % 1 = 6; 6 % 0.0001 = 60000. '
              'Чем меньше делитель, тем больше будет частное. Ну, что скажешь?',
              'игрок*=)*1 - Выучил правило из 5 класса и крутой? / 2 - Рассказать правило',
              'противник*=)*Ясно. Давно стал очевиден один факт.',
              '...',
              'противник*=)*Ты так думаешь лишь потому, что тебе так сказали. '
              'Своей головой ты думать видимо не можешь. Ты же знаешь, что если '
              'любое число разделить на себя, то получится единица? Следовательно: 0 / 0 = 1.',
              'игрок*=(*Единица - твоя оценка по матеше.',
              '',
              '',
              '']
SCORES = {
    0: [None, None, None, None],
    1: [0, 0, None, None],
    2: [0, 0, None, None],
    3: [None, None, None, None],
    4: [None, None, None, None],
    5: [None, None, None, None],
    6: [0, 0, None, None],
    7: [None, None, None, None],
    8: [None, None, None, None],
    9: [None, None, None, None],
}


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


def judge_1(screen):
    font = pygame.font.Font(None, int(HEIGHT * 0.04))
    text = font.render("Судья:", True, (255, 127, 80))
    text_x = WIDTH * 0.04
    text_y = HEIGHT * 0.88
    screen.blit(text, (text_x, text_y))


def rules(screen):
    font = pygame.font.Font(None, int(WIDTH * 0.023))
    text = font.render("Чтобы выбрать действие - нажмите 1, 2, 3 или 4, а чтобы "
                       "перелистнуть реплику - нажмите ПРОБЕЛ", True, (255, 127, 80))
    text_x = WIDTH * 0.01
    text_y = HEIGHT * 0.88
    screen.blit(text, (text_x, text_y))


def show_text(text):
    a = text
    a = list(a)
    count = 0
    if len(a) + 1 > 110:
        for i in range(len(a) - 51):
            font = pygame.font.Font(None, int(WIDTH * 0.028))
            t = a[0:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = WIDTH * 0.04
            text_y = HEIGHT * 0.92
            screen.blit(text, (text_x, text_y))
            clock.tick(30)
            pygame.display.flip()
        for i in range(len(a) - 50, len(a) + 3):
            font = pygame.font.Font(None, int(WIDTH * 0.028))
            t = a[len(a) - 52:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = WIDTH * 0.04
            text_y = HEIGHT * 0.96
            screen.blit(text, (text_x, text_y))
            clock.tick(30)
            pygame.display.flip()
    else:
        for i in range(len(a) + 1):
            font = pygame.font.Font(None, int(WIDTH * 0.028))
            t = a[0:count]
            count += 1
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = WIDTH * 0.04
            text_y = HEIGHT * 0.92
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
                         [0, HEIGHT * 0.94],
                         [WIDTH, HEIGHT * 0.94], int(HEIGHT * 0.12))
        font = pygame.font.Font(None, int(WIDTH * 0.03))
        text = font.render("Противник:", True, (255, 127, 80))
        text_x = WIDTH * 0.04
        text_y = HEIGHT * 0.88
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        show_text(element[-1])
    else:
        screen.blit(bg_2, bg_2_rect)
        screen.blit(main_common, main_common_rect)
        pygame.draw.line(screen, BLACK,
                         [0, HEIGHT * 0.94],
                         [WIDTH, HEIGHT * 0.94], int(HEIGHT * 0.12))
        font = pygame.font.Font(None, int(WIDTH * 0.03))
        text = font.render("ГГ:", True, (255, 127, 80))
        text_x = WIDTH * 0.04
        text_y = HEIGHT * 0.88
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
    bg.image, (WIDTH,
               HEIGHT))
bg_rect = bg.get_rect(
    center=(WIDTH // 2, HEIGHT // 2))

bg_1 = Background('фон_противника.jpg', [0, 0])
bg_1 = pygame.transform.scale(
    bg_1.image, (WIDTH,
                 HEIGHT))
bg_1_rect = bg_1.get_rect(
    center=(WIDTH // 2, HEIGHT // 2))

bg_2 = Background('фон_героя.jpg', [0, 0])
bg_2 = pygame.transform.scale(
    bg_2.image, (WIDTH,
                 HEIGHT))
bg_2_rect = bg_2.get_rect(
    center=(WIDTH // 2, HEIGHT // 2))

main_common = Background('main_common.PNG', [0, 0])
main_common = pygame.transform.scale(
    main_common.image, (int(WIDTH * 0.5),
                        int(WIDTH * 0.5)))
main_common_rect = main_common.get_rect(
    center=(WIDTH // 4 - 40, HEIGHT * 3 // 4 - 50))

enemy_1_common = Background('common-enemy.PNG', [0, 0])
enemy_1_common = pygame.transform.scale(
    enemy_1_common.image, (int(WIDTH * 0.5),
                           int(WIDTH * 0.5)))
enemy_1_common_rect = enemy_1_common.get_rect(
    center=(WIDTH * 0.45 + WIDTH // 4, WIDTH // 2 - WIDTH * 0.1))

old_man = Background('judge-smiling.png', [0, 0])
old_man = pygame.transform.scale(
    old_man.image, (int(WIDTH * 0.5),
                    int(WIDTH * 0.5)))
old_man_rect = old_man.get_rect(
    center=(WIDTH * 0.45 + WIDTH // 4, WIDTH // 2 - WIDTH * 0.1))


while running:
    if start:
        screen.fill(BLACK)
        clock.tick(FPS)
        screen.blit(bg, bg_rect)
        screen.blit(old_man, old_man_rect)
        pygame.draw.line(screen, BLACK,
                         [0, HEIGHT * 0.94],
                         [WIDTH, HEIGHT * 0.94], int(HEIGHT * 0.14))
        rules(screen)
        pygame.display.flip()
        time.sleep(3)
        pygame.draw.line(screen, BLACK,
                         [0, HEIGHT * 0.94],
                         [WIDTH, HEIGHT * 0.94], int(HEIGHT * 0.12))
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
            elif event.key == pygame.K_1:
                if SCORES[frase][0]:
                    score += SCORES[frase][0]
                    speak(screen, frase)
                    frase += 1
                    print(score)

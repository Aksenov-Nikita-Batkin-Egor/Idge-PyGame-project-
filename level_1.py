# coding: utf8
import pygame
import time


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


class Level1:
    def __init__(self, width, height, score):
        self.WIDTH = width
        self.HEIGHT = height
        self.BLACK = (0, 0, 0)
        self.FPS = 30
        self.frase = 0
        self.score = score
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.start = True

        self.text_lvl_1 = ['противник*=)*Делить на ноль можно.',
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
        self.SCORES = {
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

        pygame.mixer.music.load('GAME_FIGHT.mp3')
        pygame.mixer.music.play()
        pygame.display.set_caption("My Game")

        self.bg = Background('фон-зал суда.jpg', [0, 0])
        self.bg = pygame.transform.scale(
            self.bg.image, (self.WIDTH,
                            self.HEIGHT))
        self.bg_rect = self.bg.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.bg_1 = Background('фон_противника.jpg', [0, 0])
        self.bg_1 = pygame.transform.scale(
            self.bg_1.image, (self.WIDTH,
                              self.HEIGHT))
        self.bg_1_rect = self.bg_1.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.bg_2 = Background('фон_героя.jpg', [0, 0])
        self.bg_2 = pygame.transform.scale(
            self.bg_2.image, (self.WIDTH,
                              self.HEIGHT))
        self.bg_2_rect = self.bg_2.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.main_common = Background('main_common.PNG', [0, 0])
        self.main_common = pygame.transform.scale(
            self.main_common.image, (int(self.WIDTH * 0.5),
                                     int(self.WIDTH * 0.5)))
        self.main_common_rect = self.main_common.get_rect(
            center=(self.WIDTH // 4 - 40, self.HEIGHT * 3 // 4 - 50))

        self.enemy_1_common = Background('common-enemy.PNG', [0, 0])
        self.enemy_1_common = pygame.transform.scale(
            self.enemy_1_common.image, (int(self.WIDTH * 0.5),
                                        int(self.WIDTH * 0.5)))
        self.enemy_1_common_rect = self.enemy_1_common.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.old_man = Background('judge-smiling.png', [0, 0])
        self.old_man = pygame.transform.scale(
            self.old_man.image, (int(self.WIDTH * 0.5),
                                 int(self.WIDTH * 0.5)))
        self.old_man_rect = self.old_man.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

    def start_level(self):
        while self.running:
            if self.start:
                self.screen.fill(self.BLACK)
                self.clock.tick(self.FPS)
                self.screen.blit(self.bg, self.bg_rect)
                self.screen.blit(self.old_man, self.old_man_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.14))
                self.rules(self.screen)
                pygame.display.flip()
                time.sleep(3)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                self.judge_1(self.screen)

                pygame.display.flip()

                self.show_text('Кто выиграет в споре - получит свободу и право сыграть в Великий лабиринт.')

                self.start = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.speak(self.frase)
                        self.frase += 1
                    elif event.key == pygame.K_1:
                        if self.SCORES[self.frase][0]:
                            self.score += self.SCORES[self.frase][0]
                            self.speak(self.frase)
                            self.frase += 1
                            print(self.score)

    def judge_1(self, screen):
        font = pygame.font.Font(None, int(self.HEIGHT * 0.04))
        text = font.render("Судья:", True, (255, 127, 80))
        text_x = self.WIDTH * 0.04
        text_y = self.HEIGHT * 0.88
        screen.blit(text, (text_x, text_y))

    def rules(self, screen):
        font = pygame.font.Font(None, int(self.WIDTH * 0.023))
        text = font.render("Чтобы выбрать действие - нажмите 1, 2, 3 или 4, а чтобы "
                           "перелистнуть реплику - нажмите ПРОБЕЛ", True, (255, 127, 80))
        text_x = self.WIDTH * 0.01
        text_y = self.HEIGHT * 0.88
        screen.blit(text, (text_x, text_y))

    def show_text(self, text):
        a = text
        a = list(a)
        count = 0
        if len(a) + 1 > 110:
            for i in range(len(a) - 51):
                font = pygame.font.Font(None, int(self.WIDTH * 0.028))
                t = a[0:count]
                count += 1
                text = font.render(''.join(t), True, (255, 255, 255))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.92
                self.screen.blit(text, (text_x, text_y))
                self.clock.tick(30)
                pygame.display.flip()
            for i in range(len(a) - 50, len(a) + 3):
                font = pygame.font.Font(None, int(self.WIDTH * 0.028))
                t = a[len(a) - 52:count]
                count += 1
                text = font.render(''.join(t), True, (255, 255, 255))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.96
                self.screen.blit(text, (text_x, text_y))
                self.clock.tick(30)
                pygame.display.flip()
        else:
            for i in range(len(a) + 1):
                font = pygame.font.Font(None, int(self.WIDTH * 0.028))
                t = a[0:count]
                count += 1
                text = font.render(''.join(t), True, (255, 255, 255))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.92
                self.screen.blit(text, (text_x, text_y))
                self.clock.tick(30)
                pygame.display.flip()

    def speak(self, frase):
        element = self.text_lvl_1[frase]
        element = element.split('*')
        if element[0] == 'противник':
            self.screen.blit(bg_1, bg_1_rect)
            self.screen.blit(self.enemy_1_common, self.enemy_1_common_rect)
            pygame.draw.line(self.screen, self.BLACK,
                             [0, self.HEIGHT * 0.94],
                             [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
            font = pygame.font.Font(None, int(self.WIDTH * 0.03))
            text = font.render("Противник:", True, (255, 127, 80))
            text_x = self.WIDTH * 0.04
            text_y = self.HEIGHT * 0.88
            self.screen.blit(text, (text_x, text_y))
            pygame.display.flip()
            self.show_text(element[-1])
        else:
            self.screen.blit(self.bg_2, self.bg_2_rect)
            self.screen.blit(self.main_common, self.main_common_rect)
            pygame.draw.line(self.screen, self.BLACK,
                             [0, self.HEIGHT * 0.94],
                             [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
            font = pygame.font.Font(None, int(self.WIDTH * 0.03))
            text = font.render("ГГ:", True, (255, 127, 80))
            text_x = self.WIDTH * 0.04
            text_y = self.HEIGHT * 0.88
            self.screen.blit(text, (text_x, text_y))
            pygame.display.flip()
            self.show_text(element[-1])

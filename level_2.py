# coding: utf8
import pygame
import time
import take_coffee


# класс, создающий задний фон
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


class Level2:
    def __init__(self, width, height, screen, score):
        # созданине экрана, переменных
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.BLACK = (0, 0, 0)
        self.FPS = 30
        self.frase = 0  # Номер реплики
        self.score = score  # Очки
        self.sc = 0  # номер реплики без учета фона (для получения кол-ва очков из self.SCORES)
        self.choice = 0  # Выбор варианта клавишами 1-4
        self.clock = pygame.time.Clock()
        self.running = True
        self.start = True

        # включение музыки
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load('chill_music.mp3')
        pygame.mixer.music.play()

        # инициализация звука дверного звонка
        self.bell = pygame.mixer.Sound('bell.mp3')

        # Возможность нажимать клавиши управления и выдаваемые очки ([0] - пробел, [1] - клавиша "1",
        # [2] - клавиша "2", [3] - клавиша "3", [4] - клавиша "4". None - нельзя нажать, Число - кол-во очков.
        self.SCORES = [
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, 1, -1, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, 1, -1, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, -1, 2, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, 1, 2, None, None],
            [0, None, None, None, None],
        ]

        # реплики на первом фоне
        self.text_lvl_2 = ['игрок*=)*Как же хорошо поспал. Такой сон...',
                           'игрок*=/*А почему делить на 0 нельзя?... Ладно, пойду кофе сделаю себе.',
                           'игра*игра',
                           'игрок*=)*Нет ничего лучше хорошего кофе утром.',
                           'звонок в дверь*звонок в дверь',
                           'друг*=|*...',
                           'игрок*=(*1 - Привет. / 2 - Уходи.',
                           'друг*=|*Здравствуйте%/%Не уйду',
                           'игрок*=)*Чего надо?',
                           'друг*=)*Компания "Медные трубы". Хотим взять вас к себе на стажировку. Согласны?',
                           'игрок*=(*1 - Да/ 2 - Нет',
                           'друг*=))*Вам в любом случае придётся пройти со мной.',
                           'игрок*=(*Но почему?',
                           'друг*=(*У меня пистолет.',
                           'игрок*=(*Ладно, пошли.']

        # реплики на втором фоне
        self.text_lvl_2_2 = ['игрок*=)*1 - Молча идти / 2 - А зачем я вам нужен?',
                             'друг*=)*На нас подали иск, а вы в прошлом были лучшим адвокатом этой страны. '
                             'Поэтому нам нужна ваша помощь.',
                             'игрок*=)*А награда будет?',
                             'друг*=)*Да, сколько хотите?',
                             'игрок*=/*1 - 100.000 / 2 - 1.000.000.',
                             'друг*=)*Ладно.']
        # создание спрайтов

        self.bg = Background('фон-дом.jpg', [0, 0])
        self.bg = pygame.transform.scale(
            self.bg.image, (self.WIDTH,
                            self.HEIGHT))
        self.bg_rect = self.bg.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.bg_1 = Background('street.jpg', [0, 0])
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
            center=(self.WIDTH * 0.01 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.main_list = Background('main_list.PNG', [0, 0])
        self.main_list = pygame.transform.scale(
            self.main_list.image, (int(self.WIDTH * 0.5),
                                   int(self.WIDTH * 0.4)))
        self.main_list_rect = self.main_list.get_rect(
            center=(self.WIDTH * 0.01 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.women_common = Background('women_standing.PNG', [0, 0])
        self.women_common = pygame.transform.scale(
            self.women_common.image, (int(self.WIDTH * 0.4),
                                      int(self.WIDTH * 0.5)))
        self.women_common_rect = self.women_common.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.women_speaking = Background('women_speaking.PNG', [0, 0])
        self.women_speaking = pygame.transform.scale(
            self.women_speaking.image, (int(self.WIDTH * 0.4),
                                        int(self.WIDTH * 0.5)))
        self.women_speaking_rect = self.women_speaking.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.women_smiling = Background('women_smiling.PNG', [0, 0])
        self.women_smiling = pygame.transform.scale(
            self.women_smiling.image, (int(self.WIDTH * 0.4),
                                       int(self.WIDTH * 0.5)))
        self.women_smiling_rect = self.women_smiling.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.women_gun = Background('women_gun.PNG', [0, 0])
        self.women_gun = pygame.transform.scale(
            self.women_gun.image, (int(self.WIDTH * 0.4),
                                   int(self.WIDTH * 0.5)))
        self.women_gun_rect = self.women_gun.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.fone = 1

    # функция выводящая текст
    def show_text(self, text):
        try:
            text = text.split('%/%')[self.choice - 1]
        except IndexError:
            text = text.split('%/%')[-1]
        a = list(text)
        new = ''
        new2 = ''
        if len(a) > 140:
            font_size = int(self.WIDTH * 0.024)
            first_line = 0.92
            second_line = 0.945
            third_line = 0.97
        elif len(a) > 70:
            font_size = int(self.WIDTH * 0.028)
            first_line = 0.92
            second_line = 0.96
        else:
            font_size = int(self.WIDTH * 0.03)
            first_line = 0.92
        font = pygame.font.Font(None, font_size)
        for count in range(len(a) + 1):
            if count > 70:
                if count > 140:
                    if a[count - 1] == ' ' and new2 == '':
                        new2 = count
                    if new2 != '':
                        t = a[new2:count]
                        text_y = self.HEIGHT * third_line
                    else:
                        t = a[new:count]
                        text_y = self.HEIGHT * second_line
                else:
                    if a[count - 1] == ' ' and new == '':
                        new = count
                    if new != '':
                        t = a[new:count]
                        text_y = self.HEIGHT * second_line
                    else:
                        t = a[:count]
                        text_y = self.HEIGHT * first_line
            else:
                t = a[:count]
                text_y = self.HEIGHT * first_line
            text = font.render(''.join(t), True, (255, 255, 255))
            text_x = self.WIDTH * 0.04
            print_sound = pygame.mixer.Sound('print.wav')
            pygame.mixer.set_num_channels(100)
            pygame.mixer.find_channel(True).play(print_sound)
            self.screen.blit(text, (text_x, text_y))
            if a[count - 1] == ' ':
                self.clock.tick(10)
            elif count % 2 == 0:
                self.clock.tick(25)
            pygame.display.flip()

    # функция передающая show_text() текст, который надо вывести
    def speak(self, screen, frase, bag):
        if bag == 1:
            element = self.text_lvl_2[frase]
            element = element.split('*')
            if element[0] == 'друг':
                screen.blit(self.bg, self.bg_rect)
                if element[1] == '=|':
                    screen.blit(self.women_common, self.women_common_rect)
                elif element[1] == '=)':
                    screen.blit(self.women_speaking, self.women_speaking_rect)
                elif element[1] == '=))':
                    screen.blit(self.women_smiling, self.women_smiling_rect)
                elif element[1] == '=(':
                    screen.blit(self.women_gun, self.women_gun_rect)
                else:
                    screen.blit(self.women_common, self.women_common_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                font = pygame.font.Font(None, int(self.WIDTH * 0.03))
                text = font.render("Друг:", True, (255, 127, 80))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.88
                self.screen.blit(text, (text_x, text_y))
                pygame.display.flip()
                self.show_text(element[-1])
            elif element[0] == 'игрок':
                screen.blit(self.bg, self.bg_rect)
                if element[1] == '=/':
                    screen.blit(self.main_list, self.main_list_rect)
                else:
                    screen.blit(self.main_common, self.main_common_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                font = pygame.font.Font(None, int(self.WIDTH * 0.03))
                text = font.render("Вы:", True, (255, 127, 80))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.88
                self.screen.blit(text, (text_x, text_y))
                pygame.display.flip()
                self.show_text(element[-1])
            elif element[0] == 'звонок в дверь':
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                pygame.display.flip()
                self.bell.play()
            elif element[0] == 'игра':
                take_coffee.main(self.screen)
                self.frase += 1
                self.sc += 1
                self.speak(self.screen, self.frase, self.fone)

        elif bag == 2:
            element = self.text_lvl_2_2[frase]
            element = element.split('*')
            if element[0] == 'друг':
                screen.blit(self.bg_1, self.bg_1_rect)
                if element[1] == '=|':
                    screen.blit(self.women_common, self.women_common_rect)
                elif element[1] == '=)':
                    screen.blit(self.women_speaking, self.women_speaking_rect)
                elif element[1] == '=))':
                    screen.blit(self.women_smiling, self.women_smiling_rect)
                elif element[1] == '=(':
                    screen.blit(self.women_gun, self.women_gun_rect)
                else:
                    screen.blit(self.women_common, self.women_common_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                font = pygame.font.Font(None, int(self.WIDTH * 0.03))
                text = font.render("Друг:", True, (255, 127, 80))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.88
                self.screen.blit(text, (text_x, text_y))
                pygame.display.flip()
                self.show_text(element[-1])
            elif element[0] == 'игрок':
                screen.blit(self.bg_1, self.bg_1_rect)
                if element[1] == '=/':
                    screen.blit(self.main_list, self.main_list_rect)
                else:
                    screen.blit(self.main_common, self.main_common_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                font = pygame.font.Font(None, int(self.WIDTH * 0.03))
                text = font.render("Вы:", True, (255, 127, 80))
                text_x = self.WIDTH * 0.04
                text_y = self.HEIGHT * 0.88
                self.screen.blit(text, (text_x, text_y))
                pygame.display.flip()
                self.show_text(element[-1])
            elif element[0] == 'звонок в дверь':
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                pygame.display.flip()
                self.bell.play()
                self.frase += 1
                self.sc += 1
                self.speak(self.screen, self.frase, self.fone)

    # функция, создащая уровень и переключающая фразы
    def start_level(self):
        just_started = True
        while self.running:
            if self.start:
                self.screen.fill(self.BLACK)
                self.clock.tick(self.FPS)
                self.screen.blit(self.bg, self.bg_rect)
                pygame.draw.line(self.screen, self.BLACK,
                                 [0, self.HEIGHT * 0.94],
                                 [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
                pygame.display.flip()

                self.start = False

            if just_started:
                try:
                    if self.SCORES[self.sc][0] is not None:
                        self.speak(self.screen, self.frase, self.fone)
                        self.frase += 1
                        self.sc += 1
                except IndexError:
                    return self.finish_level()
                just_started = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.fone == 1:
                            if self.frase + 1 >= len(self.text_lvl_2):
                                self.screen.fill((0, 0, 0))
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase = 0
                                self.fone += 1
                                break
                        try:
                            if self.SCORES[self.sc][0] is not None:
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase += 1
                                self.sc += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_1:
                        try:
                            if self.SCORES[self.sc][1] is not None:
                                self.choice = 1
                                self.score += self.SCORES[self.sc][1]
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase += 1
                                self.sc += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_2:
                        try:
                            if self.SCORES[self.sc][2] is not None:
                                self.choice = 2
                                self.score += self.SCORES[self.sc][2]
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase += 1
                                self.sc += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_3:
                        try:
                            if self.SCORES[self.sc][3] is not None:
                                self.choice = 3
                                self.score += self.SCORES[self.sc][3]
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase += 1
                                self.sc += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_4:
                        try:
                            if self.SCORES[self.sc][4] is not None:
                                self.score += self.SCORES[self.sc][4]
                                self.choice = 4
                                self.speak(self.screen, self.frase, self.fone)
                                self.frase += 1
                                self.sc += 1
                        except IndexError:
                            return self.finish_level()

    # функция, завершающая уровень
    def finish_level(self):
        self.screen.blit(self.bg_1, self.bg_1_rect)
        pygame.draw.line(self.screen, self.BLACK,
                         [0, self.HEIGHT * 0.94],
                         [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
        pygame.display.flip()
        la = pygame.Surface((self.WIDTH, self.HEIGHT), masks=(0, 0, 0))
        la_rect = la.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))
        for i in range(1, 101):
            la.set_alpha(5)
            pygame.draw.line(self.screen, self.BLACK,
                             [0, self.HEIGHT * 0.94],
                             [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
            self.screen.blit(la, la_rect)
            pygame.display.flip()
            pygame.mixer.music.set_volume(1 - 0.01 * i)
            time.sleep(0.03)
        time.sleep(1)
        pygame.mixer.music.stop()
        return self.score

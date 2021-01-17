# coding: utf8
import pygame
import time


# класс, создающий задний фон
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


class Level3:
    def __init__(self, width, height, screen, score):
        # созданине экрана, переменных
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.BLACK = (0, 0, 0)
        self.FPS = 30
        self.frase = 0  # Номер реплики
        self.score = score  # Очки
        self.choice = 0  # Выбор варианта клавишами 1-4
        self.clock = pygame.time.Clock()

        # реплики 3 уровня
        self.text_lvl_1 = ['противник*=||*Здарова.',
                           'игрок*;|*Не здарова, а приветствую, уважаемый. Неуч неуклюжий.',
                           'противник*=|*Приветствую, уважаемый.',
                           'игрок*=|*Здарова.',
                           'противник*=|*Итак, договор считается недействительным, так как инвестор понесёт '
                           'убытки больше 70% своего состояния, что является нарушением прав.',
                           'игрок*||*Так вы хотите доказать его недействительность или всё таки расторгнуть?',
                           'противник*;|*...',
                           'противник*->*И то, и то. Или как говорят у нас на районе - не твоё дело.',
                           'игрок*=|*1 - Так ты невоспитанный / 2 - Почему инвестор должен понести убытки? '
                           '/ 3 - Каковы условия договора? / 4 - Но я должен конкретно знать чего вы хотите.',
                           'противник*=|*Сам такой. Так вот. Ваша компания скоро обанкротится, что легко доказуемо, '
                           'так что договор ваш - фуфло.%/%Потому что компания скоро обанкротится ваша, '
                           'а вы финансовый пузырь сделать хотите.%/%Таковы, что мы даём вам денег, '
                           'а вы в любом случае нам их не возвращаете%/%Мы хотим сделать так, как будто этого '
                           'договора не было, потому что компания ваша скоро обанкротится.',
                           'игрок*=|*То есть? Это "Медные трубы" обанкротятся?',
                           'противник**Так точно.',
                           'игрок*;|*1 - Невозможно / 2 - Пруфы? / 3 - Это ты сейчас во время суда обанкротишься',
                           'противник*=|*Возможно!%/%Ээээ...%/%Ну-ну.']

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
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, -1, 2, 1, 0],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [0, None, None, None, None],
            [None, 0, 2, -1, None],
            [0, None, None, None, None]
        ]

        # Включение музыки
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load('GAME_FIGHT.mp3')
        pygame.mixer.music.play()

        # Создание спрайтов
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

        self.main_list = Background('main_list.PNG', [0, 0])
        self.main_list = pygame.transform.scale(
            self.main_list.image, (int(self.WIDTH * 0.5),
                                   int(self.WIDTH * 0.5)))
        self.main_list_rect = self.main_common.get_rect(
            center=(self.WIDTH // 4 - 40, self.HEIGHT * 3 // 4 - 50))

        self.main_omg = Background('main_omg.PNG', [0, 0])
        self.main_omg = pygame.transform.scale(
            self.main_omg.image, (int(self.WIDTH * 0.5),
                                  int(self.WIDTH * 0.5)))
        self.main_omg_rect = self.main_omg.get_rect(
            center=(self.WIDTH // 4 - 40, self.HEIGHT * 3 // 4 - 50))

        self.enemy_1_common = Background('common-enemy.PNG', [0, 0])
        self.enemy_1_common = pygame.transform.scale(
            self.enemy_1_common.image, (int(self.WIDTH * 0.5),
                                        int(self.WIDTH * 0.5)))
        self.enemy_1_common_rect = self.enemy_1_common.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.enemy_1_resolute = Background('boom-enemy.PNG', [0, 0])
        self.enemy_1_resolute = pygame.transform.scale(
            self.enemy_1_resolute.image, (int(self.WIDTH * 0.5),
                                          int(self.WIDTH * 0.5)))
        self.enemy_1_resolute_rect = self.enemy_1_resolute.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.enemy_1_pointing = Background('pointing-enemy.PNG', [0, 0])
        self.enemy_1_pointing = pygame.transform.scale(
            self.enemy_1_pointing.image, (int(self.WIDTH * 0.5),
                                          int(self.WIDTH * 0.5)))
        self.enemy_1_pointing_rect = self.enemy_1_pointing.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.enemy_1_evil = Background('omg-enemy.PNG', [0, 0])
        self.enemy_1_evil = pygame.transform.scale(
            self.enemy_1_evil.image, (int(self.WIDTH * 0.5),
                                      int(self.WIDTH * 0.5)))
        self.enemy_1_evil_rect = self.enemy_1_evil.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.old_man = Background('judge-common.png', [0, 0])
        self.old_man = pygame.transform.scale(
            self.old_man.image, (int(self.WIDTH * 0.5),
                                 int(self.WIDTH * 0.5)))
        self.old_man_rect = self.old_man.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

        self.old_man2 = Background('judge-common.png', [0, 0])
        self.old_man2 = pygame.transform.scale(
            self.old_man2.image, (int(self.WIDTH * 0.5),
                                  int(self.WIDTH * 0.5)))
        self.old_man2_rect = self.old_man.get_rect(
            center=(self.WIDTH * 0.45 + self.WIDTH // 4, self.WIDTH // 2 - self.WIDTH * 0.1))

    # Запуск уровня и обработка всех событий
    def start_level(self):
        self.screen.fill(self.BLACK)
        self.clock.tick(self.FPS)
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.old_man, self.old_man_rect)
        pygame.draw.line(self.screen, self.BLACK,
                         [0, self.HEIGHT * 0.94],
                         [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.14))
        pygame.display.flip()
        pygame.draw.line(self.screen, self.BLACK,
                         [0, self.HEIGHT * 0.94],
                         [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
        self.judge_1(self.screen)

        pygame.display.flip()

        self.show_text('Инвестор, который по договору был обязан вложить деньги в компанию '
                       '"Медные трубы" подал иск с просьбой расторгнуть договор, так как этот '
                       'договор по его словам, цитирую: «такой же нечестный, как и система '
                       'оценивания на уроках рисования». Начать спор.')
        # Основной цикл, обработка событий
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        try:
                            if self.SCORES[self.frase][0] is not None:
                                code = self.speak(self.frase)
                                if code == 0:
                                    return self.finish_level()
                                self.frase += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_1:
                        try:
                            if self.SCORES[self.frase][1] is not None:
                                self.choice = 1
                                self.score += self.SCORES[self.frase][1]
                                code = self.speak(self.frase)
                                if code == 0:
                                    return self.finish_level()
                                self.frase += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_2:
                        try:
                            if self.SCORES[self.frase][2] is not None:
                                self.choice = 2
                                self.score += self.SCORES[self.frase][2]
                                code = self.speak(self.frase)
                                if code == 0:
                                    return self.finish_level()
                                self.frase += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_3:
                        try:
                            if self.SCORES[self.frase][3] is not None:
                                self.choice = 3
                                self.score += self.SCORES[self.frase][3]
                                code = self.speak(self.frase)
                                if code == 0:
                                    return self.finish_level()
                                self.frase += 1
                        except IndexError:
                            return self.finish_level()
                    elif event.key == pygame.K_4:
                        try:
                            if self.SCORES[self.frase][4] is not None:
                                self.score += self.SCORES[self.frase][4]
                                self.choice = 4
                                code = self.speak(self.frase)
                                if code == 0:
                                    return self.finish_level()
                                self.frase += 1
                        except IndexError:
                            return self.finish_level()

    # Подпись "Судья" для реплик судьи
    def judge_1(self, screen):
        font = pygame.font.Font(None, int(self.HEIGHT * 0.04))
        text = font.render("Судья:", True, (255, 127, 80))
        text_x = self.WIDTH * 0.04
        text_y = self.HEIGHT * 0.88
        screen.blit(text, (text_x, text_y))

    # Функция, выводящая текст (например, текст реплик)
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

    # Функция, запускающая реплики каждого героя
    def speak(self, frase):
        try:
            element = self.text_lvl_1[frase]
        except IndexError:
            return 0
        element = element.split('*')
        if element[0] == 'противник':
            self.screen.blit(self.bg_1, self.bg_1_rect)
            if element[1] == '->':
                self.screen.blit(self.enemy_1_pointing, self.enemy_1_pointing_rect)
            elif element[1] == '=|':
                self.screen.blit(self.enemy_1_common, self.enemy_1_common_rect)
            elif element[1] == ';|':
                self.screen.blit(self.enemy_1_evil, self.enemy_1_evil_rect)
            else:
                self.screen.blit(self.enemy_1_resolute, self.enemy_1_resolute_rect)
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
            if element[1] == '=|':
                self.screen.blit(self.main_common, self.main_common_rect)
            elif element[1] == '||':
                self.screen.blit(self.main_list, self.main_list_rect)
            else:
                self.screen.blit(self.main_omg, self.main_omg_rect)
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

    # Функция, завершающая уровень, выводящая результат суда
    def finish_level(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.old_man2, self.old_man2_rect)
        pygame.draw.line(self.screen, self.BLACK,
                         [0, self.HEIGHT * 0.94],
                         [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
        self.judge_1(self.screen)
        pygame.display.flip()
        if self.score > 8:
            result = f'Стоп. Игра окончена. Вы ПОБЕДИЛИ! Ваш счёт: {self.score}'
            self.show_text(result)
        else:
            result = f'Стоп. Игра окончена. Вы ПРОИГРАЛИ! Ваш счёт: {self.score}'
        self.show_text(result)
        time.sleep(5)
        la = pygame.Surface((self.WIDTH, self.HEIGHT), masks=(0, 0, 0))
        la_rect = la.get_rect(
            center=(self.WIDTH // 2, self.HEIGHT // 2))
        # Затемнение экрана и приглушение музыки
        for i in range(1, 101):
            la.set_alpha(5)
            pygame.draw.line(self.screen, self.BLACK,
                             [0, self.HEIGHT * 0.94],
                             [self.WIDTH, self.HEIGHT * 0.94], int(self.HEIGHT * 0.12))
            self.judge_1(self.screen)
            font_size = int(self.WIDTH * 0.03)
            font = pygame.font.Font(None, font_size)
            text = font.render(result, True, (255, 255, 255))
            text_y = self.HEIGHT * 0.92
            text_x = self.WIDTH * 0.04
            self.screen.blit(text, (text_x, text_y))
            self.screen.blit(la, la_rect)
            pygame.display.flip()
            pygame.mixer.music.set_volume(1 - 0.01 * i)
            time.sleep(0.03)
        time.sleep(1)
        pygame.mixer.music.stop()
        # Возврат общего кол-ва очков
        return self.score

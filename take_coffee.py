import pygame
import time


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location


cof = Background('coffee_image.jpg', [0, 0])
cof = pygame.transform.scale(
    cof.image, (50,
                50))
cof_rect = cof.get_rect(
    center=(25, 25))
center = [25, 25]


class Board:
    def __init__(self, wdth, hght):
        self.flag = True
        self.width = wdth
        self.height = hght
        self.board = [[0] * wdth for _ in range(hght)]
        self.left = 0
        self.top = 0
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scr):
        field = scr
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    pygame.draw.rect(field, 'white', pygame.Rect(self.left + (self.cell_size * col),
                                                                 self.top + (self.cell_size * row), self.cell_size,
                                                                 self.cell_size), width=1)
                elif self.board[row][col] == 1:
                    pygame.draw.rect(field, 'red', pygame.Rect(self.left + (self.cell_size * col),
                                                                 self.top + (self.cell_size * row), self.cell_size,
                                                                 self.cell_size), width=0)

                    pygame.draw.rect(field, 'white', pygame.Rect(self.left + (self.cell_size * col),
                                                                 self.top + (self.cell_size * row), self.cell_size,
                                                                 self.cell_size), width=1)
                elif self.board[row][col] == 2:
                    pygame.draw.rect(field, 'blue', pygame.Rect(self.left + (self.cell_size * col),
                                                               self.top + (self.cell_size * row), self.cell_size,
                                                               self.cell_size), width=0)

                    pygame.draw.rect(field, 'white', pygame.Rect(self.left + (self.cell_size * col),
                                                                 self.top + (self.cell_size * row), self.cell_size,
                                                                 self.cell_size), width=1)

    def get_click(self, mouse_pos, center, count):
        cell = self.get_cell(mouse_pos)
        a = self.on_click(cell, center, count)
        return a

    def get_cell(self, mouse_pos):
        self.x, self.y = mouse_pos[0], mouse_pos[1]
        if (self.x < self.left) or (self.x > self.left + (self.cell_size * len(self.board[0]))) or \
                (self.y < self.top) or (self.y > self.top + (self.cell_size * len(self.board))):
            return None
        else:
            return mouse_pos

    def on_click(self, cell_coords, centeral, count):
        if cell_coords is not None:
            x, y = cell_coords[0], cell_coords[1]
            column = x // (self.cell_size + 3)
            row = y // (self.cell_size + 3)
            if count == 0:
                coffee = (0, 0)
            elif count == 1:
                coffee = (0, 4)
            elif count == 2:
                coffee = (2, 3)
            elif count == 3:
                coffee = (4, 4)
            pressed = (row, column)
            if coffee == pressed:
                if count == 0:
                    screen.fill((0, 0, 0))
                    board.render(screen)
                    cup = Background('coffee_image.jpg', [0, 0])
                    cup = pygame.transform.scale(
                        cup.image, (50,
                                    50))
                    cup_rect = cup.get_rect(
                        center=(225, 25))
                    center = [225, 25]
                    screen.blit(cup, cup_rect)
                    pygame.display.flip()
                    return center
                elif count == 1:
                    screen.fill((0, 0, 0))
                    board.render(screen)
                    cup = Background('coffee_image.jpg', [0, 0])
                    cup = pygame.transform.scale(
                        cup.image, (50,
                                    50))
                    cup_rect = cup.get_rect(
                        center=(175, 125))
                    center = [175, 125]
                    screen.blit(cup, cup_rect)
                    pygame.display.flip()
                    return center
                elif count == 2:
                    screen.fill((0, 0, 0))
                    board.render(screen)
                    cup = Background('coffee_image.jpg', [0, 0])
                    cup = pygame.transform.scale(
                        cup.image, (50,
                                    50))
                    cup_rect = cup.get_rect(
                        center=(225, 225))
                    center = [225, 200]
                    screen.blit(cup, cup_rect)
                    pygame.display.flip()
                    return center
                elif count == 3:
                    screen.fill((0, 0, 0))
                    font = pygame.font.Font(None, 50)
                    text = font.render('Вкусно', 1, (50, 70, 0))
                    text_x = 400 // 2 - text.get_width() // 2
                    text_y = 400 // 2 - text.get_height() // 2
                    text_w = text.get_width()
                    text_h = text.get_height()
                    pygame.draw.rect(screen, (200, 150, 50), (text_x - 10, text_y - 10,
                                                              text_w + 20, text_h + 20))
                    screen.blit(text, (text_x, text_y))
                    pygame.display.flip()
                    time.sleep(3)
                    return 123



class Coffee:
    def __init__(self, position):
        self.x, self.y = position

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        pass

    def render(self, screen):
        pass


board = Board(9, 8)
size = width, height = 400, 400
pygame.init()
screen = pygame.display.set_mode(size)
running = True
screen.fill((0, 0, 0))
count = 0

board.render(screen)

pygame.display.flip()
screen.blit(cof, cof_rect)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = board.get_click(event.pos, center, count)
            if a:
                if a != 123:
                    center = a
                    count += 1
                else:
                    running = False

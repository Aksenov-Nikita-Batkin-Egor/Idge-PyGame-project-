import pygame
import time

pygame.init()

infoObject = pygame.display.Info()
width = int(infoObject.current_w * 0.9)
height = int(infoObject.current_h * 0.9)
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

x1, y1, r1, mx1, my1 = 200, 200, 50, 2, 0.5
x2, y2, r2, mx2, my2 = 300, 200, 50, -1, -1.5
x3, y3, r3, mx3, my3 = 500, 500, 40, 1, 1.5


def move(c, v, r, m):
    c += v
    if c < r: c, v = r, -v
    if c > m-r: c, v = m-r, -v
    return c, v


hit_count = 0
count = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x1, mx1 = move(x1, mx1, r1, width)
    y1, my1 = move(y1, my1, r1, height)
    x2, mx2 = move(x2, mx2, r2, width)
    y2, my2 = move(y2, my2, r2, height)
    x3, mx3 = move(x3, mx3, r3, width)
    y3, my3 = move(y3, my3, r3, height)

    v1 = pygame.math.Vector2(x1, y1)
    v2 = pygame.math.Vector2(x2, y2)
    v3 = pygame.math.Vector2(x3, y3)
    if v1.distance_to(v2) < r1 + r2 - 2:
        hit_count += 1

        nv = v2 - v1
        m1 = pygame.math.Vector2(mx1, my1).reflect(nv)
        m2 = pygame.math.Vector2(mx2, my2).reflect(nv)
        mx1, my1 = m1.x, m1.y
        mx2, my2 = m2.x, m2.y
    elif v1.distance_to(v3) < r1 + r3 - 2:
        hit_count += 1

        nv = v3 - v1
        m1 = pygame.math.Vector2(mx1, my1).reflect(nv)
        m2 = pygame.math.Vector2(mx3, my3).reflect(nv)
        mx1, my1 = m1.x, m1.y
        mx3, my3 = m2.x, m2.y

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 255, 255), (round(x1), round(y1)), r1)
    pygame.draw.circle(window, (255, 255, 255), (round(x2), round(y2)), r2)
    pygame.draw.circle(window, (255, 255, 255), (round(x3), round(y3)), r3)

    font = pygame.font.Font(None, 50)
    text = font.render("ЗАГРУЗКА", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    window.blit(text, (text_x, text_y))
    pygame.draw.rect(window, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    pygame.display.flip()
    count += 1
    if count == 500:
        run = False

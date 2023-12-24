import pygame
import sys

# إعداد Pygame
pygame.init()

# إعداد الشاشة
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("سحب نقطة بالماوس")

# الألوان
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# إعداد النقطة
point_color = black
point_radius = 10
point_pos = pygame.Vector2(width // 2, height // 2)
point_poos = pygame.Vector2(width // 3, height // 3)
p1, p2, dif1, dif2 = pygame.Vector2(0, 0), pygame.Vector2(0, 0), pygame.Vector2(0, 0), pygame.Vector2(0, 0)


# دورة اللعبة
clock = pygame.time.Clock()
running = True
dragging = False
dd = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # زر اليسار
                mouse_pos = pygame.Vector2(event.pos)
                if (mouse_pos - point_pos).length() < point_radius:
                    dragging = True
                    dif1 = point_pos - mouse_pos
                elif (mouse_pos - point_poos).length() < point_radius:
                    dd = True
                    dif2 = point_poos - mouse_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                dd = False

    if dragging:
        mnow = pygame.mouse.get_pos()
        point_pos = mnow + dif1
    
    if dd:
        mnow = pygame.mouse.get_pos()
        point_poos = mnow + dif2

    # رسم النقطة
    screen.fill(white)
    pygame.draw.circle(screen, point_color, (int(point_pos.x), int(point_pos.y)), point_radius)
    pygame.draw.circle(screen, blue, (int(point_poos.x), int(point_poos.y)), point_radius)
    p1 =pygame.Vector2((((point_pos.x - point_poos.x) // 2)+point_poos.x), point_poos.y)
    p2 =pygame.Vector2((((point_pos.x - point_poos.x) // 2)+point_poos.x), point_pos.y)
    #liist = [point_poos.x, point_poos.y, p1.x, p1.y, p2.x, p2.y, point_pos.x, point_pos.y]
    #pygame.draw.lines(screen, red, False, liist, 5)
    liist = [point_poos, p1, p2, point_pos]
    pygame.draw.lines(screen, red, False, liist, 5)
    #pygame.draw.lines(screen, red, liist, 5)


    # تحديث الشاشة
    pygame.display.flip()

    # تحديث معدل الإطارات
    clock.tick(60)

# إغلاق Pygame
pygame.quit()
sys.exit()
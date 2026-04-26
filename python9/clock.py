import pygame, sys
from datetime import datetime
import math


pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы")
clock = pygame.time.Clock()

# Центр и радиус 
cx, cy = WIDTH // 2, HEIGHT // 2
radius = min(WIDTH, HEIGHT) // 2 - 20  # отступы

# Шрифт 
font = pygame.font.SysFont("Arial", 28)

running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # текущее время
    now = datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second

    # Фон и циферблат
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (220, 220, 220), (cx, cy), radius)
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), radius, 2)

    #  цифры 1–12
    for i in range(1, 13):
        angle = math.radians(90 - i * 30)
        x = cx + (radius - 40) * math.cos(angle)
        y = cy - (radius - 40) * math.sin(angle)

        text = font.render(str(i), True, (0, 0, 0))
        text_rect = text.get_rect(center=(int(x), int(y)))
        screen.blit(text, text_rect)

    # Углы стрелок
    angle_h = (-30 * h - 0.5 * m + 90)
    angle_m = (-6 * m - 0.1 * s + 90)
    angle_s = (-6 * s + 90)

    # Функция конца стрелки
    def hand_end(length, angle_deg):
        rad = math.radians(angle_deg)
        x = cx + length * math.cos(rad)
        y = cy - length * math.sin(rad)
        return (int(x), int(y))

    
    pygame.draw.line(screen, (0,0,0), (cx,cy), hand_end(radius*0.5, angle_h), 6)
    pygame.draw.line(screen, (80,80,80), (cx,cy), hand_end(radius*0.8, angle_m), 4)
    pygame.draw.line(screen, (200,0,0), (cx,cy), hand_end(radius*0.9, angle_s), 2)

    # Центр
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), 5)

    pygame.display.flip()

pygame.quit()
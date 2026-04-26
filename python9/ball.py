import pygame

pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Шарик")

x, y = 300, 200
R = 25
STEP = 20

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - STEP - R >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + STEP + R <= H:
                y += STEP
            elif event.key == pygame.K_LEFT and x - STEP - R >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + STEP + R <= W:
                x += STEP

    pygame.draw.circle(screen, (255, 0, 0), (x, y), R)

    pygame.display.flip()

pygame.quit()
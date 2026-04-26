import pygame, sys, os


pygame.init()


try:
    pygame.mixer.init()
    mixer_ok = True
except Exception as e:
    mixer_ok = False

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ipod")


tracks = [
    r"C:\Users\Нурхан\Downloads\song1.mp3",
    r"C:\Users\Нурхан\Downloads\song2.mp3",
    r"C:\Users\Нурхан\Downloads\song3.mp3"
]

current = 0
is_paused = False
status = "Starting..."


for t in tracks:
    if not os.path.isfile(t):
        status = f"File not found: {t}"
        print(status)


if mixer_ok:
    try:
        pygame.mixer.music.load(tracks[current])
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        status = "Playing"
    except Exception as e:
        status = f"Load error: {e}"
else:
    status = "Sound system not working"

font = pygame.font.SysFont(None, 24)

running = True
while running:
    screen.fill((255, 255, 255))

    # Имя файла (без пути)
    name = os.path.basename(tracks[current])
    label = font.render(f"Track: {name}", True, (0,0,0))
    screen.blit(label, (10, 10))

   
    status_label = font.render(f"Status: {status}", True, (0,0,0))
    screen.blit(status_label, (10, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and mixer_ok:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
                status = "Playing"
                is_paused = False

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                status = "Stopped"
                is_paused = False

            elif event.key == pygame.K_SPACE:
                if not is_paused:
                    pygame.mixer.music.pause()
                    status = "Paused"
                    is_paused = True
                else:
                    pygame.mixer.music.unpause()
                    status = "Playing"
                    is_paused = False

            elif event.key == pygame.K_RIGHT:
                current = (current + 1) % len(tracks)
                try:
                    pygame.mixer.music.load(tracks[current])
                    pygame.mixer.music.play()
                    status = "Next track"
                except Exception as e:
                    status = f"Error: {e}"

            elif event.key == pygame.K_LEFT:
                current = (current - 1) % len(tracks)
                try:
                    pygame.mixer.music.load(tracks[current])
                    pygame.mixer.music.play()
                    status = "Previous track"
                except Exception as e:
                    status = f"Error: {e}"

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
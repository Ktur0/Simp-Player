from pathlib import Path

import pygame


AUDIO_PATH = Path("audio.mp3")
WINDOW_SIZE = (800, 500)
TIMELINE_RECT = pygame.Rect(80, 240, 640, 12)


pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("MP3 timeline")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

duration = 0.0
if AUDIO_PATH.exists():
    pygame.mixer.music.load(str(AUDIO_PATH))
    duration = pygame.mixer.Sound(str(AUDIO_PATH)).get_length()
    pygame.mixer.music.play()


def seek_from_mouse(mouse_x):
    if duration <= 0:
        return

    ratio = (mouse_x - TIMELINE_RECT.left) / TIMELINE_RECT.width
    ratio = max(0.0, min(1.0, ratio))
    pygame.mixer.music.set_pos(ratio * duration)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if TIMELINE_RECT.inflate(0, 24).collidepoint(event.pos):
                seek_from_mouse(event.pos[0])

    position = max(0.0, pygame.mixer.music.get_pos() / 1000.0)
    progress = min(1.0, position / duration) if duration else 0.0
    progress_width = int(TIMELINE_RECT.width * progress)

    window.fill((24, 26, 32))
    pygame.draw.rect(window, (70, 74, 84), TIMELINE_RECT, border_radius=6)
    pygame.draw.rect(
        window,
        (70, 170, 255),
        (TIMELINE_RECT.left, TIMELINE_RECT.top, progress_width, TIMELINE_RECT.height),
        border_radius=6,
    )
    pygame.draw.circle(
        window,
        (235, 240, 255),
        (TIMELINE_RECT.left + progress_width, TIMELINE_RECT.centery),
        8,
    )

    current_text = f"{position:.1f}s / {duration:.1f}s"
    label = font.render(current_text, True, (235, 240, 255))
    window.blit(label, (TIMELINE_RECT.left, TIMELINE_RECT.bottom + 20))

    if not AUDIO_PATH.exists():
        missing = font.render("Put an MP3 file named audio.mp3 next to main.py", True, (255, 190, 120))
        window.blit(missing, (80, 170))

    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
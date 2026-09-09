import pygame
import tkinter as tk

pygame.init()

# Cửa sổ Pygame
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("MP3 Player")

# Tkinter
root = tk.Tk()
root.withdraw()


def open_settings():
    window = tk.Toplevel(root)
    window.title("Settings")
    window.geometry("300x200")

    label = tk.Label(window, text="Cài đặt MP3 Player")
    label.pack(pady=20)

    button = tk.Button(window, text="Đóng", command=window.destroy)
    button.pack()


running = True

while running:

    # Xử lý Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                open_settings()

    # Cho Tkinter xử lý sự kiện
    root.update()

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
root.destroy()
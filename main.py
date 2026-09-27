import pygame
from upload_file import *
from load_assets import *

pygame.init()

# Khỏi tạo màn hình
window_info = (800, 500)
window = pygame.display.set_mode(window_info)
pygame.display.set_caption("Simp Player")
run = True

# Khởi tạo màu
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
DARK_THEME = "#121317"
ROSE = "#fa5655"
GREY = "#2e2e2e"
YELLOW = "#f5c518"

# Xử lý âm thanh
sound_names = []
sound_paths = []
sound_folder = "mp3_files"

def load_files():

    global sound_names, sound_paths

    sound_names = []
    sound_paths = []

    for file in os.listdir(sound_folder):
        if file.endswith(".mp3") or file.endswith(".ogg"):
            try:
                sound_paths.append(os.path.join(sound_folder, file))
                # if len(file.split()) > 4:
                #     file = ' '.join(file.split()[:4]) + "..."
                sound_names.append(file)
            except Exception as e:
                print(f"Lỗi khi load {file}: {e}")

load_files()

if len(sound_names) < 3:
    selected_sound = 0
else:
    selected_sound = 1

# Thông số của chuột
mouse_size = 50
   

while run:

    # Cập nhật thông số chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_box = pygame.Rect(mouse_x, mouse_y, mouse_size, mouse_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_box.colliderect(upload_file_button_frame):
                    upload_files()
                    load_files()
                    if len(sound_names) <= 2:
                        selected_sound = 0
                    elif len(sound_names) >= 3:
                        selected_sound = 1

                if mouse_box.colliderect(pre_button_music_frame):
                    if selected_sound > 0:
                        selected_sound -= 1

                if mouse_box.colliderect(next_button_music_frame):
                    if selected_sound < len(sound_names) - 1:
                        selected_sound += 1

    # Hiển thị frame 
    window.fill(DARK_THEME)
    display_uiux(window=window, selected_sound=selected_sound, sound_names=sound_names)
    # display_frame_test()
    print(selected_sound)

    pygame.display.update()

pygame.quit()
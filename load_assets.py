import pygame

pygame.init()

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

# Font chữ
music_name_font = pygame.font.Font("font/Roboto-Black.ttf", 16)

# Tên và thanh tìm kiếm
name_frame = pygame.Rect(20, 18, 200, 47)
search_bar_frame = pygame.Rect(230, 18, 450, 47)
setting_button_frame = pygame.Rect(720, 18, 60, 47)
name_frame_pic = pygame.image.load("assests/name_frame.png")
search_bar_pic = pygame.image.load("assests/search_bar.png")
setting_button_pic = pygame.image.load("assests/setting_button.png")

# Hiện thị danh sách âm thanh
music_frame_1 = pygame.Rect(51, 100, 180, 150)
music_frame_2 = pygame.Rect(300, 85, 198, 164)
music_frame_3 = pygame.Rect(568, 100, 180, 150)
music_name_frame_1 = pygame.Rect(67, 260, 150, 40)
music_name_frame_2 = pygame.Rect(260, 260, 280, 40)
music_name_frame_3 = pygame.Rect(580, 260, 150, 40)
next_button_music_frame = pygame.Rect(760, 128, 40, 110)
pre_button_music_frame= pygame.Rect(5, 128, 40, 110)
music_frame_1_pic = pygame.image.load("assests/music_frame_left.png")
music_frame_2_pic = pygame.image.load("assests/music_frame_big.png")
music_frame_3_pic = pygame.image.load("assests/music_frame_right.png")
music_name_frame_1_pic = pygame.image.load("assests/music_name_frame_small.png")
music_name_frame_2_pic = pygame.image.load("assests/music_name_frame_big.png")
music_name_frame_3_pic = pygame.image.load("assests/music_name_frame_small.png")
next_button_music_frame_pic = pygame.transform.smoothscale(pygame.image.load("assests/next_button.png"), (35, 100))
pre_button_music_frame_pic = pygame.transform.smoothscale(pygame.image.load("assests/pre_button.png"), (35, 100))

# Bảng điều khiển
background_frame = pygame.Rect(21.3, 328.3, 759, 157)
control_mouse = pygame.Rect(37, 344, 9, 40)
timer_frame = pygame.Rect(600, 416, 150, 40)
play_button_frame = pygame.Rect(37, 400, 72, 72)
pre_button_frame = pygame.Rect(130, 410, 57, 57)
next_button_frame = pygame.Rect(205, 410, 57, 57)
upload_file_button_frame = pygame.Rect(280, 410, 57, 57)
delete_file_button_frame = pygame.Rect(355, 410, 57, 57)
background_frame_pic = pygame.image.load("assests/background_frame.png")
timer_frame_pic = pygame.image.load("assests/timer_frame.png")
play_button_pic = pygame.image.load("assests/play_button.png")
pre_button_pic = pygame.image.load("assests/pre_music_button.png")
next_button_pic = pygame.image.load("assests/next_music_button.png")
upload_file_button_pic = pygame.image.load("assests/upload_file_button.png")
delete_file_button_pic = pygame.image.load("assests/delete_file_button.png")


# Hiển thị lên màn hình
def display_frame_test(window):

    # Khu vực tên và thanh tìm kiếm
    pygame.draw.rect(window, BLACK, name_frame)
    pygame.draw.rect(window, BLACK, search_bar_frame)
    pygame.draw.rect(window, BLACK, setting_button_frame)

    # Khu vực hiển thị danh sách âm thanh
    pygame.draw.rect(window, BLACK, music_frame_1)
    pygame.draw.rect(window, BLACK, music_frame_2)
    pygame.draw.rect(window, BLACK, music_frame_3)
    pygame.draw.rect(window, BLACK, music_name_frame_1)
    pygame.draw.rect(window, BLACK, music_name_frame_2)
    pygame.draw.rect(window, BLACK, music_name_frame_3)
    pygame.draw.rect(window, BLACK, next_button_music_frame)
    pygame.draw.rect(window, BLACK, pre_button_music_frame)

    # Khu vực bảng điều khiển
    pygame.draw.rect(window, BLACK, background_frame)
    pygame.draw.line(window, ROSE, (37, 364), (757, 364), 6)
    pygame.draw.rect(window, WHITE, control_mouse)
    pygame.draw.rect(window, GREY, timer_frame)
    pygame.draw.rect(window, ROSE, play_button_frame)
    pygame.draw.rect(window, BLUE, pre_button_frame)
    pygame.draw.rect(window, YELLOW, next_button_frame)
    pygame.draw.rect(window, GREEN, upload_file_button_frame)
    pygame.draw.rect(window, RED, delete_file_button_frame)

    pygame.display.update()

def display_uiux(window, selected_sound, sound_names = []):

    # Xử lý và hiển thị tên 
    text = []

    for name in sound_names:
        if sound_names.index(name) == selected_sound:
            if len(name.split()) > 6:
                text.append(music_name_font.render(' '.join(name.split()[:6]) + "...", True, WHITE))
            else:
                text.append(music_name_font.render(name, True, WHITE))
        else:
            if len(name.split()) > 3:
                text.append(music_name_font.render(' '.join(name.split()[:3]) + "..", True, WHITE))
            else:
                text.append(music_name_font.render(name, True, WHITE))
    
    # Khu vực tên và thanh tìm kiếm
    window.blit(name_frame_pic, name_frame)
    window.blit(search_bar_pic, search_bar_frame)
    window.blit(setting_button_pic, setting_button_frame)

    # Khu vực hiển thị danh sách âm thanh
    window.blit(next_button_music_frame_pic, next_button_music_frame)
    window.blit(pre_button_music_frame_pic, pre_button_music_frame)
    if selected_sound == 0 and len(sound_names) == 1:
        window.blit(music_frame_2_pic, music_frame_2)
        window.blit(music_name_frame_2_pic, music_name_frame_2)
    elif selected_sound == 0 and len(sound_names) >= 2:
        window.blit(music_frame_2_pic, music_frame_2)
        window.blit(music_frame_3_pic, music_frame_3)
        window.blit(music_name_frame_2_pic, music_name_frame_2)
        window.blit(music_name_frame_3_pic, music_name_frame_3)
    elif selected_sound == len(sound_names) - 1:
        window.blit(music_frame_1_pic, music_frame_1)
        window.blit(music_frame_2_pic, music_frame_2)
        window.blit(music_name_frame_1_pic, music_name_frame_1)
        window.blit(music_name_frame_2_pic, music_name_frame_2)
    elif selected_sound >= 1:
        window.blit(music_frame_1_pic, music_frame_1)
        window.blit(music_frame_2_pic, music_frame_2)
        window.blit(music_frame_3_pic, music_frame_3)
        window.blit(music_name_frame_1_pic, music_name_frame_1)
        window.blit(music_name_frame_2_pic, music_name_frame_2)
        window.blit(music_name_frame_3_pic, music_name_frame_3)

    for index in range(len(text)):
            if selected_sound == 0 and len(text) == 1:
                window.blit(text[selected_sound], (music_name_frame_2.x + 10, music_name_frame_2.y + 10))
            elif selected_sound == 0 and len(text) >= 2:
                window.blit(text[selected_sound], (music_name_frame_2.x + 10, music_name_frame_2.y + 10))
                window.blit(text[selected_sound + 1], (music_name_frame_3.x + 10, music_name_frame_3.y + 10))
            elif selected_sound == len(text) - 1:
                window.blit(text[selected_sound - 1], (music_name_frame_1.x + 10, music_name_frame_1.y + 10))
                window.blit(text[selected_sound], (music_name_frame_2.x + 10, music_name_frame_2.y + 10))
            elif selected_sound < len(text) - 1:
                window.blit(text[selected_sound - 1], (music_name_frame_1.x + 10, music_name_frame_1.y + 10))
                window.blit(text[selected_sound], (music_name_frame_2.x + 10, music_name_frame_2.y + 10))
                window.blit(text[selected_sound + 1], (music_name_frame_3.x + 10, music_name_frame_3.y + 10))
    
    # Khu vực bảng điều khiển
    window.blit(background_frame_pic, background_frame)
    pygame.draw.line(window, ROSE, (37, 364), (757, 364), 6)
    pygame.draw.rect(window, WHITE, control_mouse)
    window.blit(play_button_pic, play_button_frame)
    window.blit(upload_file_button_pic, upload_file_button_frame)
    window.blit(delete_file_button_pic, delete_file_button_frame)
    window.blit(timer_frame_pic, timer_frame)
    window.blit(pre_button_pic, pre_button_frame)
    window.blit(next_button_pic, next_button_frame)


    pygame.display.update()
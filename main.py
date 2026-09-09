import pygame

pygame.init()

# Khỏi tạo màn hình
window_info = (800, 500)
window = pygame.display.set_mode(window_info)
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
next_button_frame = pygame.Rect(760, 128, 40, 110)
pre_button_frame = pygame.Rect(5, 128, 40, 110)
music_frame_1_pic = pygame.image.load("assests/music_frame_left.png")
music_frame_2_pic = pygame.image.load("assests/music_frame_big.png")
music_frame_3_pic = pygame.image.load("assests/music_frame_right.png")
music_name_frame_1_pic = pygame.image.load("assests/music_name_frame_small.png")
music_name_frame_2_pic = pygame.image.load("assests/music_name_frame_big.png")
music_name_frame_3_pic = pygame.image.load("assests/music_name_frame_small.png")
next_button_pic = pygame.transform.smoothscale(pygame.image.load("assests/next_button.png"), (35, 100))
pre_button_pic = pygame.transform.smoothscale(pygame.image.load("assests/pre_button.png"), (35, 100))

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
def display_frame_test():

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
    pygame.draw.rect(window, BLACK, next_button_frame)
    pygame.draw.rect(window, BLACK, pre_button_frame)

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

def display_uiux():

    # Khu vực tên và thanh tìm kiếm
    window.blit(name_frame_pic, name_frame)
    window.blit(search_bar_pic, search_bar_frame)
    window.blit(setting_button_pic, setting_button_frame)

    # Khu vực hiển thị danh sách âm thanh
    window.blit(music_frame_1_pic, music_frame_1)
    window.blit(music_frame_2_pic, music_frame_2)
    window.blit(music_frame_3_pic, music_frame_3)
    window.blit(music_name_frame_1_pic, music_name_frame_1)
    window.blit(music_name_frame_2_pic, music_name_frame_2)
    window.blit(music_name_frame_3_pic, music_name_frame_3)
    window.blit(next_button_pic, next_button_frame)
    window.blit(pre_button_pic, pre_button_frame)

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

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Hiển thị frame 
    window.fill(DARK_THEME)
    # display_frame_test()
    display_uiux()

    pygame.display.update()

pygame.quit()
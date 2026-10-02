"""Điểm vào của Simp Player.

Tính năng: tìm bài, phát/tạm dừng, tua timeline, chuyển bài, thêm và xóa file.
Ghi chú refactor: sound_names/sound_paths luôn dùng chỉ số gốc; tìm kiếm chỉ
lọc danh sách hiển thị. Các hàm playback quản lý mixer và trạng thái phát,
còn vòng lặp chính nhận input rồi chuyển dữ liệu sang display_uiux để vẽ.
"""

import pygame
from upload_file import *
from load_assets import *

pygame.init()
pygame.mixer.init()

# Khỏi tạo màn hình
window_info = (800, 500)
window = pygame.display.set_mode(window_info)
pygame.display.set_icon(pygame.image.load("assests/icon.ico"))
pygame.display.set_caption("Simp Player")
run = True
search_query = ""
search_focused = False

# Thông số chuột
mouse_size = 10

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

# Xử lý pygame.mixer
playback_state = "stopped"
loaded_sound_index = None
track_duration = 0
playback_position = 0
playback_started_at = 0
is_seeking = False
seek_target = 0

def stop_playing():
    """Dừng hẳn bài hiện tại và đưa vị trí phát về đầu."""
    global playback_state, playback_position
    pygame.mixer.music.stop()
    playback_state = "stopped"
    playback_position = 0

def get_playback_position():
    """Tính vị trí phát từ tick của Pygame và phát hiện bài đã kết thúc."""
    global playback_state, playback_position

    if playback_state != "playing":
        return playback_position

    if not pygame.mixer.music.get_busy():
        playback_position = track_duration
        playback_state = "stopped"
        return playback_position

    elapsed = (pygame.time.get_ticks() - playback_started_at) / 1000
    return min(playback_position + elapsed, track_duration)

def prepare_track(sound_index):
    """Nạp file vào music stream và đo thời lượng trước khi phát hoặc tua."""
    global playback_state, loaded_sound_index, track_duration
    global playback_position, current_file

    if loaded_sound_index == sound_index:
        return True

    try:
        pygame.mixer.music.stop()
        track_duration = pygame.mixer.Sound(sound_paths[sound_index]).get_length()
        pygame.mixer.music.load(sound_paths[sound_index])
    except (pygame.error, OSError) as error:
        print(f"Không thể mở file: {error}")
        return False

    loaded_sound_index = sound_index
    current_file = sound_index
    playback_position = 0
    playback_state = "stopped"
    return True

def start_track(sound_index, position=0):
    """Phát bài tại chỉ số gốc đã cho, tùy chọn bắt đầu từ vị trí seek."""
    global playback_state
    global playback_position, playback_started_at, current_file

    if not prepare_track(sound_index):
        return False

    try:
        pygame.mixer.music.play(start=position)
    except (pygame.error, OSError) as error:
        print(f"Không thể phát file: {error}")
        return False

    current_file = sound_index
    playback_position = position
    playback_started_at = pygame.time.get_ticks()
    playback_state = "playing"
    return True

def get_visible_sound_indices():
    """Trả về chỉ số gốc của các bài khớp ô tìm kiếm, không đổi playlist."""
    query = search_query.casefold().strip()
    return [
        index for index, name in enumerate(sound_names)
        if query in name.casefold()
    ]

def change_track(step):
    """Chuyển bài trước/sau trong các kết quả đang hiển thị rồi phát ngay."""
    global selected_sound

    visible_indices = get_visible_sound_indices()
    if not visible_indices:
        return

    base_index = current_file if current_file in visible_indices else selected_sound
    if base_index not in visible_indices:
        target_position = 0 if step > 0 else len(visible_indices) - 1
    else:
        target_position = visible_indices.index(base_index) + step

    if 0 <= target_position < len(visible_indices):
        selected_sound = visible_indices[target_position]
        start_track(selected_sound)

def seek_track(position):
    """Tua đến vị trí giây đã chọn và giữ trạng thái phát/tạm dừng trước đó."""
    global playback_state, playback_position, playback_started_at

    if not sound_names or selected_sound < 0:
        return

    if not prepare_track(selected_sound):
        return

    was_playing = playback_state == "playing"
    was_paused = playback_state == "paused"
    position = max(0, min(position, max(track_duration - 0.01, 0)))

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.play(start=position)
        if not was_playing:
            pygame.mixer.music.pause()
    except pygame.error as error:
        print(f"Không thể tua file: {error}")
        return

    playback_position = position
    playback_started_at = pygame.time.get_ticks()
    playback_state = "playing" if was_playing else ("paused" if was_paused else "stopped")

# Xử lý file âm thanh
sound_names = []
sound_paths = []
sound_folder = check_mp3_files()
selected_sound = -1
current_file = None

def load_files():
    """Quét mp3_files, dựng cặp tên/đường dẫn và reset trạng thái bài."""

    global sound_names, sound_paths, selected_sound
    global loaded_sound_index, track_duration, current_file

    sound_names = []
    sound_paths = []

    stop_playing()
    loaded_sound_index = None
    track_duration = 0
    current_file = None

    for file in os.listdir(sound_folder):
        if file.lower().endswith((".mp3", ".ogg")):
            try:
                sound_paths.append(os.path.join(sound_folder, file))
                sound_names.append(file)
            except Exception as e:
                print(f"Lỗi khi load {file}: {e}")

    if len(sound_names) < 3:
        selected_sound = 0
    else:
        selected_sound = 1

load_files()

while run:

    x_mouse, y_mouse = pygame.mouse.get_pos()
    mouse_box = pygame.Rect(x_mouse, y_mouse, mouse_size, mouse_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and search_focused:
            if event.key == pygame.K_BACKSPACE:
                search_query = search_query[:-1]
            elif event.key == pygame.K_ESCAPE:
                search_query = ""
                search_focused = False
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                search_focused = False
            elif event.unicode.isprintable():
                search_query += event.unicode

            visible_indices = get_visible_sound_indices()
            if visible_indices:
                selected_sound = visible_indices[0]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                search_focused = search_bar_frame.collidepoint(event.pos)

                if pre_button_frame.collidepoint(event.pos):
                    change_track(-1)

                if next_button_frame.collidepoint(event.pos):
                    change_track(1)

                visible_indices = get_visible_sound_indices()
                if timeline_frame.collidepoint(event.pos) and selected_sound in visible_indices:
                    if prepare_track(selected_sound):
                        is_seeking = True
                        seek_target = max(0, min(
                            (event.pos[0] - timeline_frame.left) / timeline_frame.width * track_duration,
                            track_duration
                        ))

                if upload_file_button_frame.colliderect(mouse_box):
                    upload_files()
                    load_files()

                if pre_button_music_frame.colliderect(mouse_box):
                    if selected_sound in visible_indices:
                        selected_position = visible_indices.index(selected_sound)
                        if selected_position > 0:
                            selected_sound = visible_indices[selected_position - 1]

                if next_button_music_frame.colliderect(mouse_box):
                    if selected_sound in visible_indices:
                        selected_position = visible_indices.index(selected_sound)
                        if selected_position < len(visible_indices) - 1:
                            selected_sound = visible_indices[selected_position + 1]

                if delete_file_button_frame.colliderect(mouse_box):
                    if selected_sound in visible_indices:
                        try:
                            os.remove(sound_paths[selected_sound])
                        except OSError:
                            print("File not found")
                    
                    load_files()

                if play_button_frame.colliderect(mouse_box):
                    if selected_sound in visible_indices:
                        if loaded_sound_index == selected_sound and playback_state == "playing":
                            playback_position = get_playback_position()
                            pygame.mixer.music.pause()
                            playback_state = "paused"
                        elif loaded_sound_index == selected_sound and playback_state == "paused":
                            pygame.mixer.music.unpause()
                            playback_started_at = pygame.time.get_ticks()
                            playback_state = "playing"
                        else:
                            position = playback_position if loaded_sound_index == selected_sound and playback_position < track_duration else 0
                            start_track(selected_sound, position)

                if mute_button_frame.colliderect(mouse_box):
                    stop_playing()

        if event.type == pygame.MOUSEMOTION and is_seeking:
            seek_target = max(0, min(
                (event.pos[0] - timeline_frame.left) / timeline_frame.width * track_duration,
                track_duration
            ))

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and is_seeking:
            seek_track(seek_target)
            is_seeking = False

    # Hiển thị frame 
    window.fill(DARK_THEME)
    display_position = seek_target if is_seeking else get_playback_position()
    visible_indices = get_visible_sound_indices()
    visible_sound_names = [sound_names[index] for index in visible_indices]
    display_selected = visible_indices.index(selected_sound) if selected_sound in visible_indices else -2
    display_current = visible_indices.index(current_file) if current_file in visible_indices else None
    display_uiux(
        window=window,
        selected_sound=display_selected,
        sound_names=visible_sound_names,
        current_file=display_current,
        playback_position=display_position,
        track_duration=track_duration,
        is_playing=playback_state == "playing",
        search_query=search_query,
        search_focused=search_focused
    )
    # display_frame_test()
    print(selected_sound)
    print(sound_names)

    pygame.display.update()

pygame.quit()
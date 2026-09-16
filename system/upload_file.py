import tkinter as tk
from tkinter import filedialog
import shutil
import os
import sys

def check_mp3_files():

    # Lấy đường dẫn của file py hiện tại
    if getattr(sys, 'frozen', False):
        # Nếu chạy bằng file exe
        current_dir = os.path.dirname(sys.executable)
    else:
        # Nếu chạy bằng file .py
        current_dir = os.path.dirname(os.path.abspath(__file__))

    # Lấy đường dẫn folder mp3_files
    DEST_FOLDER = os.path.join(current_dir, "mp3_files")
    os.makedirs(DEST_FOLDER, exist_ok=True)

    return DEST_FOLDER

def upload_files():

    # ẩn cửa sổ Tkinter chính
    root = tk.Tk()
    root.withdraw()

    # mở cửa sổ chọn file
    file_path = filedialog.askopenfilename()
    root.destroy()  # đóng Tkinter

    # Lưu file vào thư mục
    if file_path:
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(check_mp3_files, file_name)
        shutil.copy(file_path, dest_path)

upload_files()
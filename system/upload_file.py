import tkinter as tk
from tkinter import filedialog
import shutil
import os

def upload_file():

    # Tạo thư mục music nếu chưa có
    os.makedirs("mp3_file", exist_ok=True)

    root = tk.Tk()
    root.withdraw()

    # Chọn file MP3 từ máy
    file_path = filedialog.askopenfilename(
        title="Chọn bài hát",
        filetypes=[
            ("MP3 files", "*.mp3"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        # Lấy tên file
        file_name = os.path.basename(file_path)

        # Đường dẫn đích
        destination = os.path.join("music", file_name)

        # Sao chép file
        shutil.copy2(file_path, destination)

        print("Đã thêm:", file_name)
        print("Lưu tại:", destination)

upload_file()
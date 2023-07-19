import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def choose_input_folder():
    root = tk.Tk()
    root.withdraw()
    input_folder = filedialog.askdirectory(title="Выберите папку с исходными изображениями")
    return input_folder

def convert_images_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")

        try:
            with Image.open(input_path) as img:
                if img.mode != "RGB":
                    img = img.convert("RGB")
                img.save(output_path, "webp")
            print(f"Изображение '{filename}' успешно сконвертировано в WebP.")
        except Exception as e:
            print(f"Ошибка при конвертации изображения '{filename}': {e}")

if __name__ == "__main__":
    input_folder_path = choose_input_folder()
    if not input_folder_path:
        print("Не выбрана папка с исходными изображениями.")
    else:
        output_folder_path = "output_webp_folder" 
        convert_images_to_webp(input_folder_path, output_folder_path)

import os
import shutil

video = (".webm", ".mkv", ".mp4", ".avi", ".m4v", ".flv", ".mov", ".swf")
audio = (".mp3", ".wav", ".flac", ".ogg", ".wma", ".aac", ".m4a")
image = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
three_d = (".3ds", ".obj", ".stl", ".ctb", ".3mf", ".STL")
zip = (".zip", ".rar", ".7z")
executables = (".exe", ".msi")

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_image(file):
    return os.path.splitext(file)[1] in image

def is_3d(file):
    return os.path.splitext(file)[1] in three_d

def is_zip(file):
    return os.path.splitext(file)[1] in zip

def is_exe(file):
    return os.path.splitext(file)[1] in executables

def organize():
    base_dir = "C:/Users/study/downloads"
    os.chdir(base_dir)
    
    folders = ['videos', 'audio', 'images', '3d', 'zips', 'executables', 'other']
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    for file in os.listdir():
        if os.path.isfile(file):
            if is_video(file):
                shutil.move(file, os.path.join(base_dir, "videos", file))
            elif is_audio(file):
                shutil.move(file, os.path.join(base_dir, "audio", file))
            elif is_image(file):
                shutil.move(file, os.path.join(base_dir, "images", file))
            elif is_3d(file):
                shutil.move(file, os.path.join(base_dir, "3d", file))
            elif is_zip(file):
                shutil.move(file, os.path.join(base_dir, "zips", file))
            elif is_exe(file):
                shutil.move(file, os.path.join(base_dir, "executables", file))
            else:
                shutil.move(file, os.path.join(base_dir, "other", file))
            
    print("Done")
organize()

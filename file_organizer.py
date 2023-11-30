import os
import shutil

# Below are the modules needed for watchdog to detect files being added to downloads
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
observer = Observer()
base_dir = "C:/Users/study/downloads"
# Create the handler class to check if a directory is created, and if so ignore it, so it only moves files
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        organize()

observer.schedule(Handler(), path=base_dir, recursive=False)


# Assigning file extensions to variables. More can be added here to fit requirements
video = (".webm", ".mkv", ".mp4", ".avi", ".m4v", ".flv", ".mov", ".swf")
audio = (".mp3", ".wav", ".flac", ".ogg", ".wma", ".aac", ".m4a")
image = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
three_d = (".3ds", ".obj", ".stl", ".ctb", ".3mf", ".STL")
zip = (".zip", ".rar", ".7z")
executables = (".exe", ".msi")
doc = (".txt", ".pdf", ".xlsx", ".docx")

# Checking the file extension, to decide which folder the file will be moved to
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

def is_doc(file):
    return os.path.splitext(file)[1] in doc



def organize():
    # Assigning base directory here, so it can be used in os.path later
    os.chdir(base_dir)

    # Checking if the folders exist, and if not creating them
    folders = ['videos', 'audio', 'images', '3d', 'zips', 'executables', 'docs', 'other']
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # On each file, will find the file extension and move accordingly
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
            elif is_doc(file):
                shutil.move(file, os.path.join(base_dir, "docs", file))
            else:
                shutil.move(file, os.path.join(base_dir, "other", file))
            


if __name__ == '__main__':
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()



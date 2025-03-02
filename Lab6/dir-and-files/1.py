import os

def list_files_and_dirs(path="."):
    return os.listdir(path)

print(list_files_and_dirs())
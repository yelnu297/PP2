import os

def split_path(path):
    if os.path.exists(path):
        return os.path.split(path)
    return None

print(split_path("/home/user/file.txt"))
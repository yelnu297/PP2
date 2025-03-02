import os

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        return f"{filename} deleted."
    return "File does not exist."

print(delete_file("test.txt"))
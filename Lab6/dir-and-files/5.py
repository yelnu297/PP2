def write_to_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)

write_to_file("test.txt", "Hello, world!")
def count_lines(filename):
    with open(filename, "r") as f:
        return sum(1 for line in f)

print(count_lines("test.txt"))
def read_input(filename):
    with open(filename, "r") as f:
        return f.read().strip()

def read_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
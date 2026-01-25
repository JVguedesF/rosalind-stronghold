import os
from utils.io import read_lines

def solve_lexv(alphabet, n):
    def generate(current):
        if current:
            yield current
        
        if len(current) < n:
            for char in alphabet:
                yield from generate(current + char)
                
    yield from generate("")

def solve():
    lines = read_lines()
    if len(lines) >= 2:
        alphabet = lines[0].split()
        n = int(lines[1])

        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "output.txt")
        
        with open(output_path, "w") as f:
            for string in solve_lexv(alphabet, n):
                f.write(string + "\n")

if __name__ == "__main__":
    solve()
from utils.utils import read_lines
from itertools import product

def solve():
    txt, n = read_lines()
    letters = txt.split()
    letters.sort()
    return ["".join(p) for p in product(letters, repeat=int(n))]

if __name__ == "__main__":
    print(*solve(), sep="\n")

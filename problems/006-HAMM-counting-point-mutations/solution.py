from utils.utils import read_lines

def solve():
    seq1, seq2 = read_lines()
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

if __name__ == "__main__":
    print(solve())
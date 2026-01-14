from utils.utils import read_lines

def solve():
    seq1, seq2 = read_lines()
    return [i + 1 for i in range(len(seq1)) if seq1.startswith(seq2, i)]

if __name__ == "__main__":
    print(*solve())

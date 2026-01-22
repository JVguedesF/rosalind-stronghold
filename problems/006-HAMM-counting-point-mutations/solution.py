from utils import read_lines, hamming_distance

def solve():
    seq1, seq2 = read_lines()
    return hamming_distance(seq1, seq2)

if __name__ == "__main__":
    print(solve())
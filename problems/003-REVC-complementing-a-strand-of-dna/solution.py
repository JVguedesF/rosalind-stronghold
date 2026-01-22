from utils import read_input, reverse_complement

def solve():
    dna = read_input()
    return reverse_complement(dna)

if __name__ == "__main__":
    print(solve())
from utils.io import read_fasta
from math import factorial
from collections import Counter

def solve() -> int:
    rna = next(iter(read_fasta().values()))
    counts = Counter(rna)
    return factorial(counts['A']) * factorial(counts['C'])

if __name__ == "__main__":
    print(solve())
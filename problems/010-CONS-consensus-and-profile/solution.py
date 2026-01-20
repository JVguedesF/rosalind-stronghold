from collections import Counter
from utils.io import read_fasta

def solve():
    sequences_dict = read_fasta()
    sequences = list(sequences_dict.values())
    
    if not sequences:
        return

    columns = [Counter(col) for col in zip(*sequences)]
    
    consensus = "".join(max('ACGT', key=lambda char, col=col: col[char]) for col in columns)
    
    print(consensus)
    for char in 'ACGT':
        counts = " ".join(str(c[char]) for c in columns)
        print(f"{char}: {counts}")

if __name__ == "__main__":
    solve()
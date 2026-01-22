from utils.io import read_fasta
from utils.bio import sliding_window
import itertools

def solve():
    data = read_fasta()
    dna = list(data.values())[0]

    k = 4
    counts = {}
    for combo in itertools.product('ACGT', repeat=k):
        kmer = "".join(combo)
        counts[kmer] = 0

    for kmer in sliding_window(dna, k):
        if kmer in counts:
            counts[kmer] += 1
        
    result = " ".join(str(counts[kmer]) for kmer in counts)
    
    return result

if __name__ == "__main__":
    print(solve())

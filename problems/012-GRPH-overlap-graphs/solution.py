from utils.io import read_fasta

def solve():
    sequences = read_fasta()
    k = 3
    results = []

    for id1, seq1 in sequences.items():
        suffix = seq1[-k:]
        for id2, seq2 in sequences.items():
            if id1 == id2:
                continue
            
            prefix = seq2[:k]
            
            if suffix == prefix:
                results.append(f"{id1} {id2}")

    return "\n".join(results)

if __name__ == "__main__":
    print(solve())
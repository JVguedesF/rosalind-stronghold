from utils import read_fasta, get_overlap

def solve():
    sequences = read_fasta()
    results = []
    k = 3

    for id1, seq1 in sequences.items():
        for id2, seq2 in sequences.items():
            if id1 == id2:
                continue
            
            if get_overlap(seq1, seq2, k):
                results.append(f"{id1} {id2}")

    return "\n".join(results)

if __name__ == "__main__":
    print(solve())
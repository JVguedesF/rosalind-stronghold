from utils.utils import read_fasta

def solve():
    sequences_dict = read_fasta()
    if not sequences_dict:
        return ""
    
    sequences = sorted(sequences_dict.values(), key=len)
    shortest_seq = sequences[0]
    other_seqs = sequences[1:]
    
    l_shortest = len(shortest_seq)

    for length in range(l_shortest, 0, -1):
        for start in range(l_shortest - length + 1):
            motif = shortest_seq[start:start + length]
            
            if all(motif in s for s in other_seqs):
                return motif
                
    return ""

if __name__ == "__main__":
    print(solve())
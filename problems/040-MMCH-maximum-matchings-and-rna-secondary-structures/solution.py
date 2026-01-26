import math
from utils.io import read_fasta

def solve():
    sequences = read_fasta()
    rna = list(sequences.values())[0]
    
    a = rna.count('A')
    u = rna.count('U')
    c = rna.count('C')
    g = rna.count('G')
    
    au_max, au_min = max(a, u), min(a, u)
    cg_max, cg_min = max(c, g), min(c, g)
    
    match_au = math.perm(au_max, au_min)
    match_cg = math.perm(cg_max, cg_min)
    
    print(match_au * match_cg)

if __name__ == "__main__":
    solve()
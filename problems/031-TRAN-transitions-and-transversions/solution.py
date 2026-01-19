from utils.utils import read_fasta

def solve():
    data = read_fasta()
    vals = list(data.values())
    
    transitions = 0
    transversions = 0
    purines = {'A', 'G'}

    for a, b in zip(vals[0], vals[1]):
        if a != b:
            if (a in purines) == (b in purines):
                transitions += 1
            else:
                transversions += 1
            
    return transitions / transversions 

if __name__ == "__main__":
    print(solve())

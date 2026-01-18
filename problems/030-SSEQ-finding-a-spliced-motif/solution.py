from utils.utils import read_fasta

def solve():
    data = read_fasta()
    s, t = list(data.values())
    
    indices = []
    current_pos = 0
    
    for symbol in t:
        current_pos = s.find(symbol, current_pos) + 1
        indices.append(current_pos)
        
    return " ".join(map(str, indices))

if __name__ == "__main__":
    print(solve())
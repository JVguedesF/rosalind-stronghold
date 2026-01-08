from utils.utils import read_fasta

def solve():
    data = read_fasta()
    
    max_id = None
    max_gc = 0.0
    
    for seq_id, sequence in data.items():
        c_count = sequence.count('C')
        g_count = sequence.count('G')
        total_len = len(sequence)
        
        gc_content = ((c_count + g_count) / total_len) * 100
        
        if gc_content > max_gc:
            max_gc = gc_content
            max_id = seq_id
            
    return f"{max_id}\n{max_gc}"

if __name__ == "__main__":
    print(solve())

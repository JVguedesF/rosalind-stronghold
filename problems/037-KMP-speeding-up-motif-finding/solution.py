import os
from utils.io import read_fasta

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def solve():
    raw_data = read_fasta()
    sequences = list(raw_data.values())
    seq = sequences[0]
    lps_array = compute_lps(seq)
    return " ".join(str(x) for x in lps_array)

if __name__ == "__main__":
    result_content = solve()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "output.txt")
    
    with open(output_path, "w") as f:
        f.write(result_content)
    
    print(f"Sucesso! Arquivo salvo em:\n{output_path}")
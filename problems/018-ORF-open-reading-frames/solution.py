from utils.utils import read_fasta

def solve():
    dna_dict = read_fasta()
    if not dna_dict:
        return
    
    dna = list(dna_dict.values())[0]
    
    table = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L', 
        'ATC': 'I', 'GTC': 'V', 'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V', 
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P', 
        'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'TCG': 'S', 'CCG': 'P', 
        'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D', 
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'TAA': 'Stop', 'CAA': 'Q', 
        'AAA': 'K', 'GAA': 'E', 'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R', 
        'AGC': 'S', 'GGC': 'G', 'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    def get_reverse_complement(s):
        pairs = str.maketrans("ATGC", "TACG")
        return s.translate(pairs)[::-1]

    def get_proteins(sequence):
        found_proteins = set()
        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == "ATG":
                protein = []
                for j in range(i, len(sequence) - 2, 3):
                    codon = sequence[j:j+3]
                    amino_acid = table.get(codon)
                    if amino_acid == "Stop":
                        found_proteins.add("".join(protein))
                        break
                    if not amino_acid:
                        break
                    protein.append(amino_acid)
        return found_proteins

    results = get_proteins(dna) | get_proteins(get_reverse_complement(dna))
    
    for p in results:
        print(p)

if __name__ == "__main__":
    solve()
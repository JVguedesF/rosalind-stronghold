from utils import read_fasta, reverse_complement, translate_protein

def get_proteins(sequence):
    found_proteins = set()
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == "ATG":
            protein = translate_protein(sequence[i:], strict=True)
            if protein is not None:
                found_proteins.add(protein)
    return found_proteins

def solve():
    dna_dict = read_fasta()
    if not dna_dict:
        return ""
    
    dna = list(dna_dict.values())[0]
    all_proteins = get_proteins(dna) | get_proteins(reverse_complement(dna))
    return "\n".join(all_proteins)

if __name__ == "__main__":
    resultado = solve()
    if resultado:
        print(resultado)
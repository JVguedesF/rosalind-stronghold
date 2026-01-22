from utils import read_input, translate_protein, RNA_CODON_TABLE

def solve():
    rna = read_input()
    return translate_protein(rna, table=RNA_CODON_TABLE)

if __name__ == "__main__":
    print(solve())
from utils import read_fasta, translate_protein

def solve():
    data = read_fasta()
    if not data:
        return ""

    identifiers = list(data.keys())
    dna_sequence = data[identifiers[0]]
    introns = [data[key] for key in identifiers[1:]]

    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, "")

    return translate_protein(dna_sequence)

if __name__ == "__main__":
    print(solve())
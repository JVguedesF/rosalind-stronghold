from utils import read_input, MONOISOTOPIC_MASS_TABLE

def solve():
    protein = read_input()
    
    total_mass = sum(MONOISOTOPIC_MASS_TABLE[aa] for aa in protein)
    
    return round(total_mass, 3)

if __name__ == "__main__":
    print(solve())
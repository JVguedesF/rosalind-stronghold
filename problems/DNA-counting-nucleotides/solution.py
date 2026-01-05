from utils.utils import read_input

def count_letters(dna):
    print(dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T"))

dna = read_input("input.txt")
count_letters(dna)
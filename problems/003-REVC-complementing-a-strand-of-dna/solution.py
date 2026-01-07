"""
Rosalind ID: REVC
Title: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/
"""
from utils.utils import read_input

def solve():
    data = read_input()
    table = str.maketrans("ACGT", "TGCA")
    print(data.translate(table)[::-1])

if __name__ == "__main__":
    solve()

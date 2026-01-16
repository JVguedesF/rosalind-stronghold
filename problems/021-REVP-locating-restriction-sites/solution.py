from utils.utils import read_fasta

def solve():
    dna_dict = read_fasta()
    if not dna_dict:
        return
    
    dna = list(dna_dict.values())[0]
    
    def is_rev_palindrome(s):
        pairs = str.maketrans("ATGC", "TACG")
        rev_comp = s.translate(pairs)[::-1]
        return s == rev_comp

    for i in range(len(dna)):
        for length in range(4, 13):
            if i + length > len(dna):
                break
            
            substring = dna[i:i+length]
            if is_rev_palindrome(substring):
                print(f"{i+1} {length}")

if __name__ == "__main__":
    solve()
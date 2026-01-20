from utils.io import read_fasta

memo = {}

def count_matchings(s):
    if not s:
        return 1
    if s in memo:
        return memo[s]
    
    acc = 0
    for k in range(1, len(s), 2):
        if (s[0] == 'A' and s[k] == 'U') or (s[0] == 'U' and s[k] == 'A') or \
           (s[0] == 'C' and s[k] == 'G') or (s[0] == 'G' and s[k] == 'C'):
            acc += count_matchings(s[1:k]) * count_matchings(s[k+1:])
            
    memo[s] = acc % 1000000
    return memo[s]

def solve():
    data = read_fasta()
    rna = list(data.values())[0]
    return str(count_matchings(rna))

if __name__ == "__main__":
    print(solve())
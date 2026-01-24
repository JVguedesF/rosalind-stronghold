import sys
from utils.io import read_fasta

def solve_lcsq(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))

def solve():
    seqs = list(read_fasta().values())
    
    if len(seqs) >= 2:
        print(solve_lcsq(seqs[0], seqs[1]))

if __name__ == "__main__":
    solve()
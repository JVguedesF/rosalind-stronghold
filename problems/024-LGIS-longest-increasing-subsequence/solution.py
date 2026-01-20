from utils.io import read_lines

def get_subsequence(seq, compare):
    n = len(seq)
    lengths = [1] * n
    parents = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if compare(seq[i], seq[j]) and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                parents[i] = j

    idx = max(range(n), key=lambda i: lengths[i])
    
    result = []
    while idx != -1:
        result.append(seq[idx])
        idx = parents[idx]
        
    return result[::-1]

def solve():
    _, raw_perm = read_lines()
    perm = [int(x) for x in raw_perm.split()]
    
    inc = get_subsequence(perm, lambda curr, prev: curr > prev)
    dec = get_subsequence(perm, lambda curr, prev: curr < prev)
    
    print(*inc)
    print(*dec)

if __name__ == "__main__":
    solve()

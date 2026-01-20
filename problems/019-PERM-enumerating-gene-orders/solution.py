from utils.io import read_input
from itertools import permutations

def solve():
    data = read_input().strip()
    if not data:
        return
        
    n = int(data)
    nums = range(1, n + 1)
    all_perms = list(permutations(nums))
    
    print(len(all_perms))
    for p in all_perms:
        print(*p)

if __name__ == "__main__":
    solve()
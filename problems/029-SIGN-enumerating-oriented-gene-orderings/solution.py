import itertools
from utils.io import read_input

def solve():
    n = int(read_input())
    
    nums = list(range(1, n + 1))
    signed_permutations = []

    for perm in itertools.permutations(nums):
        for signs in itertools.product([-1, 1], repeat=n):
            signed_permutations.append([p * s for p, s in zip(perm, signs)])
    
    output = [str(len(signed_permutations))]
    for p in signed_permutations:
        output.append(" ".join(map(str, p)))
        
    return "\n".join(output)

if __name__ == "__main__":
    print(solve())
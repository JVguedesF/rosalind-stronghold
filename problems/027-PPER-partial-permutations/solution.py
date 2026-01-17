from functools import reduce
from utils.utils import read_input

def solve():
    n, k = map(int, read_input().split())
    
    return reduce(lambda x, y: (x * y) % 1_000_000, range(n, n - k, -1), 1)

if __name__ == "__main__":
    print(solve())
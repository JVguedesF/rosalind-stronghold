from utils.io import read_input
import random

from utils.io import read_input

def solve():
    data = read_input()
    k, m, n = map(int, data.split())
    t = k + m + n
    
    p_recessivo = (
        (n * (n - 1)) + 
        (n * m) + 
        (m * (m - 1) * 0.25)
    ) / (t * (t - 1))
    
    return f"{1 - p_recessivo:.5f}"

if __name__ == "__main__":
    print(solve())

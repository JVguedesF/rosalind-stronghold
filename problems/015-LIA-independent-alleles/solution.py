from utils.io import read_input
from math import comb

def solve():
    data = read_input().split()
    if not data:
        return 0.0
        
    k, n_min = int(data[0]), int(data[1])
    
    total_pop = 2**k
    p_aabb = 0.25
    
    prob_at_least_n = sum(
        comb(total_pop, i) * (p_aabb**i) * ((1 - p_aabb)**(total_pop - i))
        for i in range(n_min, total_pop + 1)
    )
        
    return round(prob_at_least_n, 3)

if __name__ == "__main__":
    print(solve())
from utils.io import read_input

def solve():
    counts = [int(x) for x in read_input().split()]
    probs = [1, 1, 1, 0.75, 0.5, 0]
    
    expected_value = sum(c * p * 2 for c, p in zip(counts, probs))
        
    return expected_value

if __name__ == "__main__":
    print(solve())
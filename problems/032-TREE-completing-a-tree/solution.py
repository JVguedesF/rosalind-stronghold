from utils.utils import read_input

def solve():
    data = read_input().strip().splitlines()
    n = int(data[0])
    existing_edges = len(data) - 1
    
    return (n - 1) - existing_edges

if __name__ == "__main__":
    print(solve())
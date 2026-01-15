from utils.utils import read_input

def solve():
    line = read_input().split()
    if not line:
        return 0
        
    n = int(line[0])
    m = int(line[1])
    
    idades = [0] * m
    idades[0] = 1
    
    for _ in range(1, n):
        novos_coelhos = sum(idades[1:])
        idades = [novos_coelhos] + idades[:-1]
        
    return sum(idades)

if __name__ == "__main__":
    print(solve())
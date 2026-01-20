from utils.io import read_input

def solve():
    data = read_input()
    months, litter_size = map(int, data.split())
    return calculate_rabbit_pairs(months, litter_size)

def calculate_rabbit_pairs(months, litter_size):
    if months <= 2:
        return 1

    current_generation = 1
    previous_generation = 1
    
    for _ in range(3, months + 1):
        current_generation, previous_generation = (current_generation + 
                                                   (previous_generation * litter_size)), current_generation
        
    return current_generation

if __name__ == "__main__":
    print(solve())
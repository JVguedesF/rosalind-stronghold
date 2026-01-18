import math
from utils.utils import read_lines

def main():
    lines = read_lines()
    dna_string = lines[0]
    gc_contents = [float(x) for x in lines[1].split()]

    result = []

    for x in gc_contents:
        log_prob = 0
        p_gc = math.log10(x / 2)
        p_at = math.log10((1 - x) / 2)

        for base in dna_string:
            if base in 'GC':
                log_prob += p_gc
            elif base in 'AT':
                log_prob += p_at
        
        result.append(log_prob)

    print(*(f"{val:.3f}" for val in result))

if __name__ == "__main__":
    main()
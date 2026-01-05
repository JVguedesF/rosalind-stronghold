from utils.utils import read_input

def solve():
    s = read_input() 
    print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))

if __name__ == "__main__":
    solve()
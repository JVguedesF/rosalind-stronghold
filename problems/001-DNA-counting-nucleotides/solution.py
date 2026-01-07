from utils.utils import read_input

def solve():
    data = read_input() 
    print(data.count("A"), data.count("C"), data.count("G"), data.count("T"))

if __name__ == "__main__":
    solve()
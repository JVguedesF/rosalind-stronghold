from utils.io import read_input

def solve():
    s = read_input()
    return s.replace('T', 'U')

if __name__ == "__main__":
  print(solve())
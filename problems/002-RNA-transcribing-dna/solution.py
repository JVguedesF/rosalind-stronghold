from utils.utils import read_input

#! Best solution
"""
def solve():
    s = read_input()
    return s.replace('T', 'U')
"""

def solve():
  data = read_input()
  chars = []
  for char in data:
      if char == "T":
          chars.append("U")
      else:
          chars.append(char)
  return "".join(chars)

if __name__ == "__main__":
  print(solve())
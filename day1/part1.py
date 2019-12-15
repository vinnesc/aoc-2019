import math

file_name = 'in'

with open(file_name) as f:
  lines = f.read().splitlines()
  masses = list(map(int, lines))
  
  total = 0
  for mass in masses:
    fuel = math.floor(mass / 3) - 2
    total += fuel

  print(total)

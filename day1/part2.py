import math

file_name = 'in'

def calc_fuel(mass):
  necessary = math.floor(mass/ 3) - 2
  if necessary <= 0:
    return 0

  return necessary + calc_fuel(necessary) 

with open(file_name) as f:
  lines = f.read().splitlines()
  masses = list(map(int, lines))
  
  total = 0
  for mass in masses:
    fuel = calc_fuel(mass) 
    total += fuel

  print(total)

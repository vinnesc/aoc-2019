import sys

file_name = 'in'

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Move:
  def __init__(self, direction, distance):
    self.direction = direction
    self.distance = distance

"""
  It's pointless to make this a two-pass. The only reason why it's like that is because I tried something else before and didn't work.
  I'm too lazy to change it sorry. Good news is that it works, but it's probably slow as hell.
  So basically just remove Move and add the points as you parse the movements.
"""
def solve(a, b):
  a_n = b_n = 0
  a_m = b_m = 0
  a_moves = []
  b_moves = []

  for move in a:
    if move[0] == 'U':
      a_moves.append(Move(UP, int(move[1:])))   
    if move[0] == 'D':
      a_moves.append(Move(DOWN, int(move[1:])))   
    if move[0] == 'R':
      a_moves.append(Move(RIGHT, int(move[1:])))   
    if move[0] == 'L':
      a_moves.append(Move(LEFT, int(move[1:])))   
  
  for move in b:
    if move[0] == 'U':
      b_moves.append(Move(UP, int(move[1:])))   
    if move[0] == 'D':
      b_moves.append(Move(DOWN, int(move[1:])))   
    if move[0] == 'R':
      b_moves.append(Move(RIGHT, int(move[1:])))   
    if move[0] == 'L':
      b_moves.append(Move(LEFT, int(move[1:])))   
  
  points = set()
  min_distance = sys.maxsize

  x = y = 0
  for move in a_moves:
    for distance in range(move.distance):
      x += move.direction[0]
      y += move.direction[1]
      points.add((x, y))

  x = y = 0
  for move in b_moves:
    for distance in range(move.distance):
      x += move.direction[0]
      y += move.direction[1]
      if (x, y) in points:
        min_distance = min(min_distance, abs(x) + abs(y))
        print("cut in: ({x}, {y})".format(x=x, y=y))  
        print("distance is: {}".format(abs(x) + abs(y)))
  
  print("min distance is {}".format(min_distance))

with open(file_name) as f:
  first_wire = f.readline().split(',')
  second_wire = f.readline().split(',')
  
  solve(first_wire, second_wire)


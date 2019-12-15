file_name = 'in'

def run(program):
  i = 0

  while i < len(program):
    if program[i] == 1:
      # add
      a = program[i + 1]
      b = program[i + 2]
      c = program[i + 3]

      program[c] = program[a] + program[b]
    elif program[i] == 2:
      # multiply
      a = program[i + 1]
      b = program[i + 2]
      c = program[i + 3]

      program[c] = program[a] * program[b]
    elif program[i] == 99:
      break

    i += 4

with open(file_name) as f:
  op_codes = f.read().split(',')
  program = list(map(int, op_codes))

  # Fix program
  program[1] = 12
  program[2] = 2
  
  print(program)
  run(program)
  print(program)

  

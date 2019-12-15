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
  original = list(map(int, op_codes))
  
  for noun in range(0, 100):
    for verb in range(0, 100):
      program = original.copy()
      # Fix program
      program[1] = noun 
      program[2] = verb

      run(program)

      if program[0] == 19690720:
        print('Noun: ' + str(noun))
        print('Verb: ' + str(verb))

        print('Answer: ' + str(100 * noun + verb))
  

count = 0

"""
  Making this overcomplicated for fun :P
"""
def has_adjacent_digits(n):
  previous = -1

  while n > 0:
    if (n % 100) % 11 == 0:
      return True
    if previous != -1 and n % 10 == previous:
      return True
    
    n = n // 10
    previous = n % 10
    n = n // 10

  return False

def number_increases(n):
  previous = n % 10
  while n > 0:
    if n % 10 > previous:
      return False
    previous = n % 10
    n = n // 10

  return True

for i in range(272091, 815432 + 1):
  if has_adjacent_digits(i) and number_increases(i):
    count += 1

print("number of valid passwords: {}".format(count))

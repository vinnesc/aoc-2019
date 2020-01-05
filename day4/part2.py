count = 0

def has_adjacent_digits(n):
  i = 1
  s = str(n)
  
  while i < len(s):
    if s[i] == s[i - 1]:
      matches = 2

      number = s[i]
      i += 1
      while i < len(s) and s[i] == number:
        matches += 1
        i += 1

      if matches == 2:
        return True
   
    i += 1 
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

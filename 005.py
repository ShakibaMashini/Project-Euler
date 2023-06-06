#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def ifDividesAll(num):
  for i in range(2,21):
    if num % i != 0:
      return False
  return True

num = 2520
while True:
  if ifDividesAll(num):
    break
  else:
    num = num + 10
print (num)

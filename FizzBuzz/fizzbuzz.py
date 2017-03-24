def fizzbuzz(val):
  if val% 3 == 0 and val% 5 == 0:
    print('Fizz Buzz')
  elif val% 3 == 0:
    print('Fizz')
  elif val%5 == 0:
    print('Buzz')

fizzbuzz(6)

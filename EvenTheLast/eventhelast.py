def evenlast(array):
  length = len(array)
  
  n = length
  if length % 2 == 0:
    n = length-1
  
  if length != 0:
    sum = 0
    for x in range(0,n):
       if x % 2 == 0:
         sum = sum + array[x]

    print(sum*array[-1])
  else :
   print(0) 


evenlast([1,3,5])

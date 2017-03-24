def index_power(array, n):
  array_length = len(array)
  
  if array_length-1 >= n:
    index_value = array[n]
    print(index_value**n)
  else:
    print(-1)
  


index_power([1,3,10,100,5], 3)

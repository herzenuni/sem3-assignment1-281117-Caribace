def function(number):
  num=str(number)
  sum=0
  for el in num:
      elem=int(el)
      sum+=elem**2
  return sum 

def func():
  for i in range(10, 100):
    if function(i) % 17 == 0:
      print('Двузначное число: {}'.format(i))  
  for i in range(100, 1000):
    if function(i) % 17 == 0:
      print('Трехзначное число: {}'.format(i))
      
      func()  

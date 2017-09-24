

from functools import reduce
def even_sum(lists):
   y=reduce(add,lists)
return y


def add(a,b):
   z=a+b
return z 




c=[]
for element in range(100,501,2):
   c.append(element)
   print(c)
   x=even_sum(c) 
   print(x)



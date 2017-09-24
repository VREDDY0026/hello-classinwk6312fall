from functools import reduce


add=lambda x,y:x+y
numbers=list(range(0,10,2))
print(numbers)
c=[]
for i in numbers:
  i=i**2
  c.append(i)
print(c)

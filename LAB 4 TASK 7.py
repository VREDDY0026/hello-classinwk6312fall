def mid(ls):
  ls.pop(0)
  ls.pop(len(ls)-1)
  return ls


li=[1,2,3,4]
print(li)
result=mid(li)
print(result)




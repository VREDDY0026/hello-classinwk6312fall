lt=[1,2,2,4,5]
ls=[1,2,2,4,5]

for i in range(len(ls)-1):
  for m in range(len(ls)-i-1):
    if lt[i]==ls[m+1+i]:
     print("Duplicate ")
     exit()
print("Nothing duplicate found")  




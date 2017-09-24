list=[1,2,3,4,3,4]
def remaining_dup(l):
    m=[]
    x=0
    for i in range(len(list)):
      m.append(l[0])
      l.pop(0)
      print("New list is"+str(m))
      print("Old list is "+str(l)) 
      x=x+1
      print(m)

remaining_dup(list)

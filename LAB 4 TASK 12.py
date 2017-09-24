def open_stores():

  d=dict()
  fout=open('word.txt','r')
  for line in fout:
   b=line.split()
   for w in b:
    d[w]=w
  search=input("Enter your sentence:")
  if search in d:
   print("YES your word is in dictionary!!")
  else: 
   print("NO your word is not in dictionary")
 

open_stores() 



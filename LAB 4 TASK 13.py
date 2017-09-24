d={'one':1,'two':2,'three':3}
users=input("Enter a word::")
if users in d: 
 print(d.get(users))
else:
 print("Cant be found in dictionary")

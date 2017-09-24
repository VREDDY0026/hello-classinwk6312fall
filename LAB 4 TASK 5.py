def capitalize_nest(l):
  after=[] 
  for element in l:
    if isinstance(element,str):
       x=element.upper()
        
       after.append(x)
    elif isinstance(element,list):
       capitalize_nest(element)
  print(after)

lists=['Vikranth','Reddy',['inwk']]
capitalize_nest(lists)

def cum_sum(lists):
 x=1
 while x<len(lists):
   lists[x]=lists[x-1]+lists[x]
   x+=1
 return lists





ls=[1,2,3,4,5]
print("The original list is "+str(ls))
cs=cum_sum(ls)
print("The cumulative sum is "+str(cs))

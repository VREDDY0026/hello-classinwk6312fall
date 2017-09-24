def is_anagr(wd1,wd2):
  wd1=wd1.upper()
  wd2=wd2.upper()
  x=0
  for elements in wd1:
    if elements in wd2:
       x=x+len(elements)
    else:
       print("Not anagram")
       break
  if x==len(wd1):
    print("Anagram")








word1="Cinema"
word2="iceman"

is_anagr(word1,word2)


inu = str(raw_input("enter the file name: "))
pops = open(inu + '.txt','r')
x = pops.read()

inu_l = str(raw_input("enter the file name: "))
pops = open(inu_l + '.txt','r')
y = pops.read()


rp = x.lower()
rs = y.lower()

str1 = ''.join(rp)
str2 = ''.join(rs)

total1 = 0
total2 = 0

import string
out1 = str1.translate(string.maketrans("",""), string.punctuation)
out2 = str2.translate(string.maketrans("",""), string.punctuation)


words1 = out1.strip().split()
words2 = out2.strip().split()
total1 += len(words1)
total2 += len(words2)
if total1 > total2:
  print (total1,"will be the number of words")
else:
  print (total2,"will be the number of words")

word.sort()
last_word = " "
for word in words:
    if word != last_word:
        count = [i for i, w in enumerate(words) if w == word]
        print(word + "is repeated " + str(len(count)) + "times.")
        

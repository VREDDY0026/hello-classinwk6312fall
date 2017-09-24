pops = open('li.txt','r')
x = pops.read()

replace = x.lower()

str1 = ''.join(replace)

total = 0

import string
out = str1.translate(string.maketrans("",""), string.punctuation)


words = out.strip().split()
total += len(words)
print (total)



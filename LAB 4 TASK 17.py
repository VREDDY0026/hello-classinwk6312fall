
# coding: utf-8

# In[31]:

def fibo1(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n > 2: 
        return fibo1(n-1) + fibo1(n-2)
for n in range(1,10):
    print(fibo1(n))
    
import timeit

start = timeit.default_timer()

stop = timeit.default_timer()
with_out = stop - start
print(with_out)


# In[30]:

fib_cah = {}
## because of this dictionary the spped of second program is increased
def fibo2(n):
    if n in fib_cah:
        return fib_cah[n]
    if n == 1:
        value = 1
    elif n ==2:
        value = 1
    elif n > 2: 
        value = fibo2(n-1) + fibo2(n-2)
    fib_cah[n] = value
    return value
for n in range(1,10):
    print(fibo2(n))

import timeit

start = timeit.default_timer()

stop = timeit.default_timer()

with_cach = stop - start
print(with_cach)


# In[ ]:




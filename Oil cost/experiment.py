import numpy as np 
import matplotlib.pyplot as plt
#act = np.math.factorial
ch = np.random.choice
f_cache = {0:1, 1:1}
def fact(x):
    if x not in f_cache:
        f_cache[x] = x*fact(x-1)
    return f_cache[x]

def C(n, k):
    return fact(n)/(fact(k)*fact(n-k))

def P(x, i, p):
    return (1-p)**(x+i)*p**i

def W(p_, x, i):
    return (x+2*i)*p_

def Expect(stop, x, p):
    res = 0
    for i in range(stop+1):
        res+=W(P(x, i, p), x, i)
    return res

#xs = np.linspace(0, 10, 11)
#ps = np.linspace(0, .8, 21)

#X, Y = np.meshgrid(xs, ps)
#Z = Expect(1000, X, Y)
def f(stop, x, p):
    res = 0
    for i in range(stop+1):
        res+=C(x+2*i, x+i)*(x+2*i)*(((1-p)**(x+i)-1)/2**i)
    res/=2**x
    return res
p = .7
ar = ch(a = np.array([1, -1]), p = np.array([.7, .3]), size = (100000, 5))
k = ar.sum(1)
s = 0
for i in k:
    if i == 3:
        s+=1
m = s/k.size
a = 5*(1-p)*p**4

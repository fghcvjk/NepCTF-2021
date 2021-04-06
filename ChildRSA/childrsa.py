#childrsa
from Crypto.Util.number import *
from gmpy2 import iroot
from os import *
from secret import flag1,flag2,padding1,padding2
assert len(flag1)==20
assert len(flag1)>len(flag2)
assert len(flag2)==len(padding2)
def init1():
    m=(padding1*2**200+bytes_to_long(flag1))*2**200
    r1=getPrime(170)
    r2=getPrime(170)
    p=getPrime(1024)
    q=getPrime(1024)
    N=p*q

    return m,r1,r2,N
    
def enc1(m,r1,r2,N):
    c1=pow(m+r1,3,N)
    c2=pow(m+r2,3,N)
    return c1,c2

def init2():
    prefix = 2**1000
    r3 = prefix+flag2*2**200
    r4 = 2*prefix+padding2*2**200
    return r3,r4

def enc2(r3,r4):
    c3 = pow(r3*r4,3)
    return c3

(m,r1,r2,N) = init1()
(c1,c2)=enc1(m,r1,r2,N)
(r3,r4) = init2()
c3 = enc2(r3,r4)
print N
print(c1,c2,c3)


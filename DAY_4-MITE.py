# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:13:34 2018
DAY4, MITE, MANGALORE
@author: pooja
"""

import numpy as np
a=np.arange(6)
b=np.arange(10,16)
c=np.arange(20,26)
d=np.arange(30,36)
e=np.arange(40,46)
f=np.arange(50,56)

A=np.array([a,b,c,d,e,f])

A[2::2,:]
A[2,2::2]
A[2,::2]
A[::2,::2]

A[2::2,::2]

a=np.arange(0,80,10)
mask=np.array([1,0,0,1,1,0,0,1], dtype='bool')
a[mask]
print(A.prod(axis=0))
a.flags.writeable=False
a.flags.writeable=True
np.genfromtxt("missing.dat", delimiter=",")
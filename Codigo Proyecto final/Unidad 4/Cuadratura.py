import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
  return 1-x**2

a=0
b=1

x=np.array([(1/3)**0.5-(1/3)**0.5])
w=np.array([1,1])
u=(b-a)*x/2+(a+b)/2

I= (b-a)+np.sum(w*f(u))/2

print(I)
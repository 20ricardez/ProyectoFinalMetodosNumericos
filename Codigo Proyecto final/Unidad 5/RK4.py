from math import *

def test1(t, y):
    return y - t**2 + 1

def test2(t, y): 
    return 2 - exp(-4*t) - 2*y

def RK4(a, b, y0, f, N):
    h = (b - a)/N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))
    
    for i in range(1, N+1):
        k1 = h*f(t, w)
        k2 = h*f(t + h/2, w + k1/2)
        k3 = h*f(t + h/2, w + k2/2)
        k4 = h*f(t + h, w + k3)
        w = w + (k1 + 2*k2 + 2*k3 + k4)/6
        t = a + i*h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
    return w

print("Método RK4:")
RK4(0, 2, 0.5, test1, 10)

print("Método RK4:")
RK4(0, 1, 1, test2, 20)



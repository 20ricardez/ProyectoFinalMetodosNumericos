#importamos las librerias q utilizaremos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import math
# definiendo la ED dy/dx en función(x,y) para valores iniciales
def dydx(x, y): 
  return 4*math.e**(0.8*x)-0.5*y #sistema de ecu
# Solicion analitica de la ED en función(x,y)
def solucion (x,y): 
  sol = (4/1.3)*(math.e**(0.8*x)-math.e**(-0.5*x))+2*math.e**(-0.5*x) 
  return sol
#valores iniciales Y'(Xo)=Yo , mientras xf representa hasta que valor se quiere evaluar numericame
n =16 
# Valor que se asume: a mayor valor de n mas iteraciones y mas preciso
x0 =0 
# valor inicial de Y'(Xo)=Yo
y0 =2 
# valor inicial de Y'(Xo)=Yo
xf =4 
# para un valor de Xf se obtiene un yf o solucion numerica: Y'(Xf)=Yf 
h=(xf-x0)/n
#crear array para la los valores de "y" mediante solucion analitica
ysa=np.zeros(n)
#creamos lista que almacenaran las soluciones numericas de "yi" , obtenias a partir de "xi"
x = [x0]
y = [y0]
#iteramos por RK4 a patir de los valores iniciales x0,y0 la cantidad de n veces, para obtener las
for i in range(n): 
  k1=h*dydx(x0,y0) 
  k2=h*dydx((x0+h/2),(y0+k1/2)) 
  k3=h*dydx((x0+h/2),(y0+k2/2)) 
  k4=h*dydx((x0+h),(y0+k3)) 
  y0=y0+(k1+2*k2+2*k3+k4)/6 
  y0=y0 
  x0=x0+h 
  y.append(y0) 
  x.append(x0)
#iteramos en la funcion de la solucion analitica para obtener los valores de "y"=ysa, evaluados fo
for i in range(n):
   ysa[i]=solucion(x[i+1], y[i])

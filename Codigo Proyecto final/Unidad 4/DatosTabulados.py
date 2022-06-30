import numpy as np #LIBRERIAS
import pylab as pl
from sympy import *
import pandas as pd
pd.read_csv

valido = False#VALIDADCION
def validar(valor):
	entero = int(valor)
	return entero >= 0 and entero <= 10

validoB= False
def validarB(valorB):
	enteroD = int(valorB)
	return enteroD >= 0 and enteroD <= 10

x=[0,1,2,3,4,5,6,7,8,9,10]   #ARREGLO
y=[0,1,4,9,16,25,36,49,68,81,100]

df = pd.DataFrame({'1stcolumn                      2ndcolumn':[0,1,4,9,16,25,36,49,68,81,100]}) # TABULACION
print(df)

pl.plot(x, y) #GRAFICACION
pl.show()

print('------------------------------------------------------')# IDENTIFICACION FUNCION
print('Funcion calculada x**2, equis al cuadrado')
print('Derivada')    #DERIVADA
x = sp.Symbol('x') 
y = x**2 
sp.diff(y,x)
print (sp.diff(y,x))

print('Integral')  #INTEGRAL
print('Valor a ')#A
while not valido:
	valor = input()
	valido = validar(valor)
	if not valido:
		print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')
print(f'El valor válido es {valor}.')

print('Valor b ')
#bucle para pedir el valor
while not validoB:
	valorB = input()
	validoB= validarB(valorB)
	if not validoB:
		print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')#B

print(f'El valor válido es {valorB}.')
f = x**2 
print(sp.integrate(f))
sp.integrate(y,(x,valor,valorB))

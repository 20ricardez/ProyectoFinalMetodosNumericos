
import numpy as np


A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])
#procedimiento considerar como 0
casicero = 1e-15 

#evitar truncamiento dde operaciones
A = np.array(A,dtype=float) 

#matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#pivoteo parcial por  filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

#Para cada fila en AB
for i in range(0,n-1,1):
#oolumna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    
    #dondemax no esta en diagonal
    if (dondemax !=0):
        #intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
        
AB1 = np.copy(AB)

#eliminacion hacia adelante 
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

# eliminacion hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    #diagonal a unos
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcolumna])
X = np.transpose([X])

#salida
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminacion hacia adelante')
print(AB2)
print('eliminación hacia atrás')
print(AB)
print('solución de X: ')
print(X)
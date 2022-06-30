#Paso 1: Importar bibliotecas y conjunto de datos
import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
boston = datasets.load_boston()
print(boston)
print('Información en el dataset:')
print(boston.keys())
print('Características del dataset:')
print(boston.DESCR)
print('Cantidad de datos:')
print(boston.data.shape)
print('Nombres columnas:')
print(boston.feature_names)
#Paso 2: dividir el conjunto de datos en 2 componentes
X_p = boston.data[:, np.newaxis, 5]
y_p = boston.target
#Paso 3: ajustar la regresión lineal al conjunto de datos. 
plt.scatter(X_p, y_p)
plt.show()
#	Paso 3: ajustar la regresión lineal al conjunto de datos. 
from sklearn.model_selection import train_test_split
#Paso4; ajuste de la regresión polinomial al conjunto de datos
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)
from sklearn.preprocessing import PolynomialFeatures
#Paso 5: En este paso estamos visualizando los resultados de la regresión lineal usando un diagrama de dispersión.
poli_reg = PolynomialFeatures(degree = 2)
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)
#Paso6: Visualización de los resultados de la regresión polinomial mediante un diagrama de dispersión.
pr = linear_model.LinearRegression()
pr.fit(X_train_poli, y_train_p)
#Paso 7: predecir un nuevo resultado con regresión lineal y polinomial.
Y_pred_pr = pr.predict(X_test_poli)
#Graficamos los datos junto con el modelo
plt.scatter(X_test_p, y_test_p)
plt.plot(X_test_p, Y_pred_pr, color='red', linewidth=3)
plt.show()
print()
print('DATOS DEL MODELO REGRESIÓN POLINOMIAL')
print()
print('Valor de la pendiente o coeficiente "a":')
print(pr.coef_)
print('Valor de la intersección o coeficiente "b":')
print(pr.intercept_)
print('Precisión del modelo:')
print(pr.score(X_train_poli, y_train_p))
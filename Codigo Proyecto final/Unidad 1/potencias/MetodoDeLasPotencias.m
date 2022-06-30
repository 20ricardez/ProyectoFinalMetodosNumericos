  clc 
  clear all
  close all
  
  
  matrizA=zeros(3,3)
  matrizU=zeros(3,1)
  #Agregando datos a la matriz A
  disp('Ingresando datos a matriz A');
  for i=1:3
    for j=1:3
      matrizA(i,j)=input(['Ingrese fila ',num2str(i),' columna ',num2str(j),' : '])
      
    endfor
  endfor 
  #Ingresando datos a la matriz U
  disp('Ingresando matriz U')
  for i=1:3
    matrizU(i,1)=input(['Ingrese fila ',num2str(i),' columna ',num2str(1),' : '])
  endfor
  Potencia(matrizA,matrizU)
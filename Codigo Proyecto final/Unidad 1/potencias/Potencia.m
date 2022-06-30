function Potencia(matrizA,matrizU)
 # matrizUAuxiliar=zeros(3,1)
  #matrizA=zeros(3,3)
  #matrizA=zeros(3,3)
  #matrizU=zeros(3,1)
  #matrizUAuxiliar=zeros(3,1)
  
  iMF=0
  k=1
  z=1
  contadorM=1
  contadorSalir=0
  bandera=true
 
 while bandera!=false
    filasMU=1
    suma=0
    multiplicacion=0
    for i=1:3
      for j=1:3
        multiplicacion=matrizA(i,j)*matrizU(filasMU,1)
        filasMU=filasMU+1
        suma=suma+multiplicacion
      endfor
      matrizUAuxiliar(i,1)=suma
      suma=0
      filasMU=1
    endfor
    disp('****Vector resultante****')
    for i=1:3
      disp([" ",num2str(matrizUAuxiliar(i,1))])
    endfor
    disp('*********************')
    #buscando el elemento de mayor magnitud (facctor de normalizacion) en el vector resultante matrizUAuxiliar
    for j=1:3
      for i=1:2
        if matrizUAuxiliar(i,1)>=matrizUAuxiliar(i+1,1)
          FNormalizacion=matrizUAuxiliar(i,1)
        endif
        if matrizUAuxiliar(i,1)<=matrizUAuxiliar(i+1,1) 
          FNormalizacion=matrizUAuxiliar(i+1,1)
        endif
      endfor
      endfor 
  #disp(['Factor de normalizacion: ',num2str(FNormalizacion)])
  
  disp('***************Factor de normalizacion *********')
FNormalizacion
disp('*************************************************')
  #diviendo entre el factor de normalizacion
  for i=1:3 
   matrizUAuxiliar(i,1)=matrizUAuxiliar(i,1)/FNormalizacion
   matrizU(i,1)=matrizUAuxiliar(i,1)
  endfor
  
  disp('*****Matriz u******')
  for i=1:3
    matrizU(i,1)
  endfor
  disp('*******************')
  disp('Factores de normalizacion anteriores')
  matrizFactorNor(z)=FNormalizacion
  disp('************************************')
  
  if z>=2
   valor1=round(matrizFactorNor(contadorM))
    valor2=round(matrizFactorNor(contadorM+1))
    contadorM=contadorM+1
    if valor1==valor2 
     contadorSalir=contadorSalir+1
      if contadorSalir==30
       bandera=false
      endif
    endif
  endif
  z=z+1
  endwhile
  
  endfunction
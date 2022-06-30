import numpy as np 
def runge_kutta_3(Dy,t0,tn,n,y0): 
    # Paso 1 
    h=(tn-t0)/n 
    tiwi = np.zeros(shape=(n+1,2),dtype=float) 
    tiwi[0] = [t0,y0] 
    ti = t0
    wi = y0 
    # Paso 2 
    for i in range(1,n+1,1): 
        # Paso 3  
        K1 = h * Dy(ti,wi) 
        K2 = h * Dy(ti+h/2, wi + K1/2) 
        K3 = h * Dy(ti+h, wi + 2*K2 -K1)         
        # Paso 4 
        wi = wi + (1/6)*(K1+4*K2+K3) 
        ti = ti + h 
        tiwi[i] = [ti,wi] 
        return(tiwi) 

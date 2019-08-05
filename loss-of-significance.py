import numpy as np
import matplotlib.pyplot as plt 


#### Algoritmo de Arquímedes para calculo de PI ####



lista1 = [] #lista para guardar iteraciones


n = 2   #Numero de diviciones de circunferencia unitaria caso base
sn = 2  #Distancia entre extremos de subdivición, caso base


while True:
    ron = np.sqrt(1-sn**2/4) #Distancia desde el centro hasta cuerda de figura inscrita (ver figura MS)
    an = n*sn*ron/2.         #Relación entre n , sn y ron/2
    Sn = sn/ron              #Distancia entre extremos figura transcrita (ver figura A'B')
    An = n*Sn/2.
    lista1.append((n, 1-ron, sn, Sn, an, An))
    sn = np.sqrt(2-2*np.sqrt(1-sn**2/4)) #Distancia entre extremos figura inscrita (ver figura AB)
    n *= 2
    
    if An == an:    #Cuando la figura inscrita y la transcrita coinciden, termina la iteración
        break
    
an_list1a = []
an_list1e = []

for a,b,c,d,e,f in lista1:
    an_list1a.append(a)
    an_list1e.append(e)
    print a, "\t", b, "\t", c, "\t", d, "\t", e, "\t", f
    
plt.plot(an_list1a,an_list1e)   
    
#### Ahora aplicando el cambio de variable:de suma por diferencia: ####
# Mismo caso que anterior pero para calcular sn se aplica un cambio de variable
    
    
    
lista2 = []


n = 2
sn = 2


while True:
    ron = np.sqrt(1-sn**2/4)
    an = n*sn*ron/2.
    Sn = sn/ron
    An = n*Sn/2.
    lista2.append((n, 1-ron, sn, Sn, an, An))
    sn = np.sqrt(1/2.*sn**2/(1+np.sqrt(1-sn**2/4.)))
    n *= 2
    
    if An == an:
        break

an_list2a = []
an_list2e = []

for a,b,c,d,e,f in lista2:
    an_list2a.append(a)
    an_list2e.append(e)
    print a, "\t", b, "\t", c, "\t", d, "\t", e, "\t", f

    
plt.plot(an_list2a,an_list2e)   

plt.title('Loss of significance when calculating pi')

plt.legend(["Calculo de PI angoritmo de Arquimedes","Calculo con cambio de variable"])
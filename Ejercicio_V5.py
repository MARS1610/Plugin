from math import sqrt,pi,exp
import queue

m = 0 
s = 2 
x = 1.0
f = 1 / (sqrt(2*pi)*s)* exp (-0.5*((x-m)/s)**2)

#Estructuras de control
#Operadores relacionales
'''
== Igual
!= Distinto que
< Menor que 
> Mayor que
<= Menor o igual que 
>= Mayor o igual que'
'''
#Operadores logicos 

'''
and = Y
or = O

x or excluyente 4 == 4 xor 9 < 3 Resultado de 1 o 0 verdadero 
'''

#Estructuras if 

if semaforo == verde:
    print ('Cruzar avenida')
else:
    print ('Espera')

#Bucle while
anio = 2022
while anio <= 2022:
    print('Informes del año',str(anio))
    anio += 1

#Bucle for
list = ['Juan', 'Ricardo', 'Jose']
for i in list: 
    print(i)
    
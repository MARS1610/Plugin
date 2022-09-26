import sys 
import keyword 
import operator 
import os 


print (keyword.kwlist)
print (len(keyword.kwlist))

#identacion
p = 10
if p == 10:
    print('p es igual a 10 ')

#Variable 
o = 5
id(0)
id(p)


p = 20 
q = 20
r = q

#tuplas  no permiten cambios en los valores
#listas permiten cambios
#Diccionarios permiten cambios

lista =  (1,2,3,4,5,'python')
print (lista[2:4])


#diccionario

dic = {'uno':1,'dos': 2,'tres': 3, 'cuatro':4 , 'cisco': 5}
dic['tres'] = 6
print(dic['tres'])
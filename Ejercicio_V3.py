#Trabajando Conjuntos

A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {8,9,10}

A | B 

R = A.union(B)
print(R)
R = A.union(B,C)
print(R)

#interseccion de conjuntos

R = A.intersection(B)
print (R)


#Diferiencia  de conjuntos
R = A.difference(B)
print(R)
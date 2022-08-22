###Ejercicio 1 
# x e y son números enteros
#Devuelve el número más grande
#Si son iguales, devuelve cualquiera de los 2
#Tu codigo

def obtMayor(x,y):
    return x,y
x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo  número: '))
if x>y:
  print('El número ', x ,'es mayor que' , y )
elif x<y:
  print('El número ', y ,'es mayor que' , x )
else:
  print('El numero ' ,x, 'es el mismo')

'''list1 = [8,9,6,5,8,9]
list2 = [8,2,3,6,7,10]


for i in list1:
    for j in list2:
        print('cruce de lista: ', i,j)'''

import os
import sys
import xlrd
import xlwt

alumno = ['Francisco','Saul','Rafael','Antonio','Julio','Efren','Sarai','Ofelia','Azael','Abigail','Brenda','Carlos','Miguel','Abraham','Oliver','Bruno','Edgar','Eduardo']
par1 = ['8','9','10','9','8','7','10','9','9','10','9','7','8','8','9','10','9','8']
par2 = ['8','8','9','10','9','9','9','10','8','10','8','10','9','8','10','10','8','9']
num = len (alumno)
print(num)

lib = xlwt.Workbook()
hoja = lib.add_sheet('Calificaciones')
styleHead = xlwt.easyxf('font: - bold-1-color_black,--height-220;')
styleOrd = xlwt.easyxf('font: bold-1,-color-red;')

def promedio(a, b):
    r = (a + b )/ 2
    return r 
    prom = 0 

for i in range ( num):
    for j in range(4):
        if 1 == 0 and  j  == 0 :
            hoja.write (i ,j ,"Alumno")
        elif i == 0 and j == 1:
            hoja.write(i,j," Primer parcial")
        elif i == 0  and j == 2:
            hoja.write(i,j," Segundo parcial")
        elif i == 0  and j == 3:
            hoja.write(i,j,"Ordinario")
        elif i == 0 and j == 4:
             hoja.write(i,j,"Ordinario", styleHead)
        elif j == 0:
            hoja.write(i,j,alumno[i-1])
        elif j == 1:
            hoja.write(i,j,par1[i-1])
        elif j == 2:
            hoja.write(i,j,par2[i-1])
        elif j == 3:
            """hoja.write(i,j,promedio(int (par1[i-1]), int (par2[i-1]) ))"""
            prom = promedio ((int (par1[i-1]), int (par2[i-1]) ))
            hoja.write(i,j, prom)
        elif j == 4:
            if prom >=8.0:
                hoja.write(i,j, 'Exento')
            elif prom >= 6.0:
                hoja.write(i,j, 'Presenta')
            elif prom >= 6.0:
                hoja.write(i,j, 'Sin derecho',styleHead)

lib.save ("C:/Users/hp pc/Desktop/python/Calificaciones.xls")

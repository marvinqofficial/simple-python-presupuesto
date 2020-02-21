# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:51:36 2020

@author: marvin
"""
print('Ingrese su presupuesto')
presupuesto = int(input())

print('Ingrese el precio de el paquete de frutas')
frutas = int(input())

print('Ingrese el precio de el paquete de verduras')
verduras = int(input())

print('Ingrese el precio de el paquete de granos')
granos = int(input())

#x-3+y-2+z-5<=presupuesto


def funcion(x, y, z):
    valor = (x-3+y-2+z-5)
    if(valor<presupuesto):
        print('Usted es un buen comprador a ahorrado')
    elif(valor==presupuesto):
            print('cuidado')
    else:
        print('Usted es un mal comprador')
    


funcion(frutas, verduras, granos)
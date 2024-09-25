#Funciones de calculadora
import math

def suma(x,y):
	return x+y 

def resta(x,y):
	return x-y

def mul(x,y):
	return x*y 

def div(x,y):
	if y==0:
		return 'ERROR DIV POR 0'
	else:
		return x/y

def raiz2(x):
	return math.sqrt(x)

def modulo(x,y):
	return x%y
		
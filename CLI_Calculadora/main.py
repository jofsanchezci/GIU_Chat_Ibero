from func import suma, resta, mul, div, raiz2, modulo

print('Bienvenido a la calculadora')
print('----------------------------')
print('Escoja una opción: ')
print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. Raiz')
print('6. Modulo')
opcion=int(input('Ingrese la opcion: '))
if opcion == 1:
	num1=float(input('Ingrese el numero 1: '))
	num2=float(input('Ingrese el numero 2: '))
	print('La suma de num1 y num2 es: ',suma(num1,num2))
elif opcion== 2:
	num1=float(input('Ingrese el numero 1: '))
	num2=float(input('Ingrese el numero 2: '))
	print('La resta de num1 y num2 es: ',resta(num1,num2))
elif opcion== 3:
	num1=float(input('Ingrese el numero 1: '))
	num2=float(input('Ingrese el numero 2: '))
	print('La Multiplicación de num1 y num2 es: ',mul(num1,num2))
elif opcion== 4:
	num1=float(input('Ingrese el numero 1: '))
	num2=float(input('Ingrese el numero 2: '))
	print('La división de num1 y num2 es: ',div(num1,num2))




else:
	print('Final')



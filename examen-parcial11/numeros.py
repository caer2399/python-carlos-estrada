# programa numeros.py, que permita al usuario ingresar un numero
# imprimit CERO si ingreso 0,
#    POSITIVO si es mayor a 0,
#    NEGATIVO si es menos a 0,

# ERROR en cualquier otro caso.

n = input("Ingrese un numero: ")
print(n)
 
numero = int(n)

if (numero == 0):
           print('CERO')
elif (numero > 0):
           print('POSITIVO')
elif (numero < 0): 
           print('NEGATIVO')
else:
           print("ERROR")




   




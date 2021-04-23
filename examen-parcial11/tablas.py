# Autor: Carlos estrada
# Universidad Veracruzana
# tablas.py

n = input("Ingresa un numero: ")
numero = int(n)

if (numero > 0):
  for i in range(numero, (numero * 11), numero):
    print(i)
elif (numero < 0):
  print ("ERROR")


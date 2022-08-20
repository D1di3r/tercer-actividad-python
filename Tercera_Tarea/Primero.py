num=1
suma=0
contador=0

while num !=0:

 num=int(input("Digite un número entero (0 para finalizar)"))

 if num !=0:
  suma += num
  contador += 1

if contador == 0:
    print("Error ningun numero o cero ha sido insertado")
else :
    promedio= suma / contador

    print("El promedio de los {} numeros  es igual a {}. ".format(contador,promedio))
import string



n=0
n1=0
m2=0
terminar=1

while terminar ==1:
    n=float(input("Digite el numero 1 :"))
    n1=float(input("Digite el numero 2 :"))
    n2=float(input("Digite el numero 3 :"))
    terminar=int(input("Digite 0 para terminar"))
    if n2<n>n1:
     print("El numero mas grande es", n)
    elif n<n1>n2:
     print("El numero mas grande es", n1)
    elif n1<n2>n:
     print("El numero mas grande es", n2)



     
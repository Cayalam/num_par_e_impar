print("Ejercicio #1: Este ejercicio lee 100 numeros enteros y me dice cuantos son pares y cuantos son impares ")

# Processing
par=0
impar=0

for i in range(100):
    n=int(input("Digita un numero: "))
    if n%2 == 0:
        par=par+1
    else:
        impar=impar+1
print("El numero de pares que ingresaste fue: ",par)
print("El numero de impar que ingresaste fue: ",impar)






































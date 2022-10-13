print("Calcular el factorial de N numero")
#Input
N=int(input("Por favor ingresa el numero al cual deseas sacar el factorial: "))

#processing
fac= 1
for i in range(2,N+1):
    fac= fac*i
print("El factorial de el numero que ingresaste fue: "+ str(fac))
print("Fin del programa")
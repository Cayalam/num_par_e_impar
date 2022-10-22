# Ejercicio con Lista:
# Mirar el nombre de el producto con menor precio
# Estas dos clases de listas so paralelas asi que lo que este e la posicion 0 perteece al primer precio
producto=["Arroz","Yuca","Carne","Pan","Huevo"] # Nombro las dos listas
precio=[2000,600,14000,3000,700]

 # Utilizo la fución llamada min para que me calcule el menor precio
minimo=min(precio) 

# La  index pertenece  a la parte de la lista y me devuelve lo que guarde en la variable minimo 
pos=precio.index(minimo)
product=producto[pos]
print("El producto con menor precio es: ",product)
print("El precio de el producto es: ", minimo)




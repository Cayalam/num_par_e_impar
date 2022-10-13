print("Lamzamiento de N dados")
# Input
N=int(input("Cuantas veces vas a lanzar el dado: "))
# Processing
c1= 0
c2= 0
c3= 0
c4= 0
c5= 0
c6= 0

import random

for j in range(N):
    j = random.randint(1,6)
    if j == 1:
        c1=c1+ 1
    elif j == 2:
        c2= c2 +1 
    elif j == 3:
        c3= c3 + 1 
    elif j == 4:
        c4=c4 + 1  
    elif j == 5:
        c5= c5 + 1
    elif j == 6:
        c6= c6 + 1 
       
print("Las veces que te salio 1 fue: ",c1)
print("Las veces que te salio 2 fue: ",c2)
print("Las veces que te salio 3 fue: ",c3)
print("Las veces que te salio 4 fue: ",c4)
print("Las veces que te salio 5 fue: ",c5)
print("Las veces que te salio 6 fue: ",c6)

print("Game over")
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "
for i in range(1,N+1):
    if i<N:
        s=s+str(i**2)+","
    else:
        s=s+str(i**2)
# Ejercisio No 2:
print(s)
s="serie: "
for i in range(1,11):
    s=s+str(i)+","  
print(s)
# Ejercisio No 3:
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "
for i in range(1,N+1):
    if i<N:
        s=s+str(2**i)+","
    else:
        s=s+str(2**i)
print(s)
# Ejercisio No 4:
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "

for i in range(1,N+1):
    if i<N:
        s=s+"1/" +str(i)+","
       
    else:
        s=s+"1/"+str(i)
        
print(s)
# Ejercisio No 5:
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "

for i in range(1,N+1):
    if i <N:
        s=s+"1/" +str(i**2+1)+","    
    else:
        s= s +"1/" + str(i**2+1)
       
print(s)
# Ejercisio No 6:
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "
n=2
for i in range(1,N+1):
    if i<N:
        s=s+str(n*i)+","
        n=n+1
    else:
        s=s+str(n*i)
        n=n+1
print(s)
# Ejercisio No 7:
N=int(input("Digita No.de elementos de la serie: "))
s="serie: "

for i in range(1,N+1):
    if i<N:
        s=s+str(5*i-2)+","
        
    else:
        s=s+str(5*i-2)
        
print(s)
# Ejercisio No.8:


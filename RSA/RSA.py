p=int(input("p: "))#7
q=int(input("q: "))#11
phi =(p-1)*(q-1)
e=int(input("e= ")) #13
n=p*q
c=int(input("c: "))
a1=1
a2=0
a3=0

b1=0
b2=1
b3=0

d1=phi
d2=e
d3=0


k2=int(d1/d2)


while d1!=1:
    a3=a1-(a2*k2)
    b3=b1-(b2*k2)
    d3=d1-(d2*k2)

    a1=a2
    b1=b2
    d1=d2

    a2=a3
    b2=b3
    d2=d3
    k2=int(d1/d2)
    if d2==1:
        break


d=b2
if d <0:
    d=d+phi

elif d>phi:
     d=d%phi


m= pow ( c, d, n)
print(hex(m) [2:-1].decode('hex'))

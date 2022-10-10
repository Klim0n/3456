from math import *
a=int(input("ievadirtskaitli a: "))
b=int(input("ievadirtskaitli b: "))
c=int(input("ievadirtskaitli c: "))
D=b**2-4*a*c
if D<0:
  print("skaņu nav!")
elif D==0:
  x=-b/2*a
  print("ir viena sakne =",x)
else:
  x1=(-b+sqrt(D))/2*a 
  x2=(-b+sqrt(D))/2*a
  print("ir divas saknes, x1 =",x1," x2 =",x2)

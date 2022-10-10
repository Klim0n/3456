from math import *
sk1=int(input("ievadirtskaitli a: "))
sk2=int(input("ievadirtskaitli b: "))
oper=input("ievadiet matematsikp operaciku: ")
if oper=="+":
  print("summa =", sk1+sk2)
elif oper== "-":
  print("reizinajums =", sk1-sk2)
elif oper== "*":
  print("reizinajums =", sk1*sk2)
elif oper=="/":
  print("reizinajums =", sk1/sk2)
elif oper=="s":
  print("kvadratasakne =", sqrt(sk1))
else:
  print("šāda matematiska operacija netiek atvalstita!!!")
  
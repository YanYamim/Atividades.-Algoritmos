import math

xn1 = int(input("Qual o xn1? "))
xn2 = int(input("E o xn2? "))
xn3 = int(input("E o xn3? "))
logaritmo = math.log(64,2)

x = xn1 + xn2/(xn3 + xn1) + 2*(xn1 - xn2) + logaritmo

print(x)
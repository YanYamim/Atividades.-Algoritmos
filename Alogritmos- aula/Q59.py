import math

cateto1 = int(input("Qual o cateto oposto?"))
cateto2 = int(input("Qual o cateto adjacente?"))
hipotenusa = math.sqrt(cateto1*cateto1 + cateto2*cateto2)

print(hipotenusa)
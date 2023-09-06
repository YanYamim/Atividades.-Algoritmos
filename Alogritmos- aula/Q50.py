import math

Base = int(input("Fale a base do retângulo: "))
altura = int(input("Fale a altura do retângulo: "))

perimetro = (2 * Base) + (2 * altura)
area = Base * altura
diagonal = math.sqrt(Base*Base + altura * altura)

print(perimetro, area, diagonal)


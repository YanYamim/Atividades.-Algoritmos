import math

Base_altura = int(input("Fale a base e a altura do retângulo: "))

perimetro = 4 * Base_altura
area = Base_altura * Base_altura
diagonal = math.sqrt(Base_altura)

print(perimetro, area, diagonal)
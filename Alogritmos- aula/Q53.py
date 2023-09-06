import math

Base = int(input("Fale a base do paralelepípedo: "))
altura = int(input("Fale a altura do paralelepípedo: "))
profundidade = int(input("Fale a profundidade do paralelepípedo: "))

diagonal = math.sqrt(Base*Base + altura * altura + profundidade * profundidade)

print(diagonal)
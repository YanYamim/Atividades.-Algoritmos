import math

n_graus = float(input("Fale um ângulo: "))

if n_graus % 2 == 0:
    angulo_radianos = math.radians(n_graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    print("O seno de", n_graus,"graus é",seno)

else:
    angulo_radianos = math.radians(n_graus)
    cosseno = math.cos(angulo_radianos)
    print("O cosseno de", n_graus,"graus é",cosseno)
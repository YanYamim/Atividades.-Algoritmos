peso = float(input("Fale seu peso em Kg: "))
altura = float(input("E sua altura em metros "))
imc = peso / (altura * altura)

if imc < 20:
    print("Você está abaixo do peso")

elif 20 <= imc <= 25:
    print("Seu peso está normal")

elif 25 <= imc <= 30:
    print("Você está com excesso de peso")

elif 30 <= imc <= 35:
    print("Você está com obesidade")

elif imc > 35:
    print("Você está com obesidade mórbida")
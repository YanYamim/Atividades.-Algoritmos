nome = str(input("Diga seu nome: "))
idade = int(input("Qual a idade? "))

if idade <= 10:
    preco = 30

elif 10 <= idade <= 20:
    preco = 60

elif 29 <= idade <= 45:
    preco = 120

elif 45 <= idade <= 59:
    preco = 150

elif 59 <= idade <= 65:
    preco = 250

elif idade >= 65:
    preco = 400

print("Você", nome, "deverá pagar", preco, "reais")

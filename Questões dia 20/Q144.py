saldo_medio = int(input("Qual o saldo méidio? "))

if 0 <= saldo_medio <= 500:
    credito = saldo_medio 

elif 501 <= saldo_medio <= 1000:
    credito = saldo_medio * 0.3

elif 1001 <= saldo_medio <= 3000:
    credito = saldo_medio * 0.4

elif saldo_medio >= 3001:
    credito = saldo_medio * 0.5

print("Seu saldo é", saldo_medio, "logo seu crédito será de ", credito)
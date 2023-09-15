destino = input("Qual é o seu destino? ").strip().lower()
viagem_volta = input("Terá viagem de volta (Sim/Não)? ").strip().lower()

if destino == "região norte":
    if viagem_volta == 'sim':
        preco_total = 900
    else:
        preco_total = 500
        
elif destino == "região nordeste":
    if viagem_volta == 'sim':
        preco_total = 650
    else:
        preco_total = 350

elif destino == "centro-oeste":
    if viagem_volta == 'sim':
        preco_total = 600
    else:
        preco_total = 350

elif destino == "região sul":
    if viagem_volta == 'sim':
        preco_total = 550
    else:
        preco_total = 300

print(f"Sua viagem para {destino} custará R${preco_total:.2f}.")

n_cdu = int(input("digite os números: "))

unidade = n_cdu % 10
dezena = (n_cdu // 10) % 10
centena = (n_cdu // 100) % 10

n_udc = unidade * 100 + dezena * 10 + centena

print(n_udc)

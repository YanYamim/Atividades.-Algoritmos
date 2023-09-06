hora_aula = float(input("Qual a hora aula? "))
n_aulas = int(input("Quantas aulas dá no mês? "))
desconto_inss = float(input("Qual o INSS? "))

salario_bruto = hora_aula * n_aulas
desconto_salarial = (desconto_inss/100) * salario_bruto
salario_liquido = salario_bruto - desconto_salarial

print(salario_liquido)
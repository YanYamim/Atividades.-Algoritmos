salario_minimo = float(input("Fale o salário: "))
quilowatt_gastos = float(input("Fale quanto quilowatts gastos: "))
cem_quilowatt = (salario_minimo * 1/7)
quilowatt = cem_quilowatt / 100
custo_total = quilowatt_gastos * quilowatt
desconto = custo_total * 0.1
novo_valor = custo_total - desconto

print("Cada quilowatt equivale a", quilowatt)
print("O valor a ser pago será", custo_total)
print("O novo valor com 10% de desconto será", novo_valor)
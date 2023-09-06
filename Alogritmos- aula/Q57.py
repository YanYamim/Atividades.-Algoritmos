pr1 = float(input("Nota da PR1: "))
pr2 = float(input("Nora da PR2: "))

media = (pr1 + pr2)/2

media_truncada = int(media)
media_arredondada = round(media)

print("A média truncada é", media_truncada,"e a média arredondada é", media_arredondada)
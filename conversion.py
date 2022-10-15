monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("ingrese el nombre de la divisa: ")

print(monedas.get(divisa.title(), "La divisa no está."))
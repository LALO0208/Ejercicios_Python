numeros = [12, 33, 44, 5, 32, 67, 98]

for numeros in numeros:
    if numeros % 2 == 0:
        print("el numero {} es par ".format(numeros))
        continue
    if numeros % 2 == 1:
        print("el numero {} es impar ".format(numeros))
        continue
import math

numero = 5.4

print("el numero es:", numero)

parte_decimal, parte_entero = math.modf(numero)
print("Su parte entera es {} y su parte decimal es {}".format(
    parte_entero, parte_decimal))

nombre = input("Escribe tu nombre: ")
numero_entero = int(input("Dijita un munero: "))
numero_flotante = float(input("Dijita un numero con decimal: "))
es_verdadero = bool(input("¿Es correcta la respuesta? True/False: "))
print(f"Hola {nombre} hagamos una suma ", f"la suma de {numero_entero} ", f"mas {numero_flotante} ", f"da como resultado {numero_entero+numero_flotante}", sep="\n")

# Límites de enteros en Python
'''
entero_minimo = -2**31  # Valor mínimo para enteros con signo de 32 bits
entero_maximo = 2**31 - 1  # Valor máximo para enteros con signo de 32 bits

print("Límite mínimo de entero:", entero_minimo)
print("Límite máximo de entero:", entero_maximo)

Límites de números de punto flotante en Python
flotante_minimo = 2.2250738585072014e-308  # Valor mínimo para números de punto flotante en doble precisión
flotante_maximo = 1.7976931348623157e+308  # Valor máximo para números de punto flotante en doble precisión

print("Límite mínimo de punto flotante:", flotante_minimo)
print("Límite máximo de punto flotante:", flotante_maximo)
'''
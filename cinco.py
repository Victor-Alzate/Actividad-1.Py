numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

suma = numero1 + numero2

resta = numero1 - numero2

multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero."

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division}")

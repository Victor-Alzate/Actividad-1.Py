numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))

if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}")
else:
    print("Ambos números son iguales.")

from utilidades import es_primo, filtrar_pares, sumar_lista

usr = int(input("Ingrese un número: "))
resultado = "es primo" if es_primo(usr) == True else "NO es primo"
print(f"El número {usr} {resultado}")

usr = input("\nIntroduce los números: ")
print(filtrar_pares(list(map(int, usr.split()))))

usr = input("\nIntroduce los números: ")
numeros = []
for n in usr.split():
    try:
        numeros.append(int(n))
    except ValueError:
        pass
print(f"El resultado de la suma es: {sumar_lista(numeros)}")

from utilidades import es_primo, filtrar_pares

usr = int(input("Ingrese un número: "))
resultado = "es primo" if es_primo(usr) == True else "NO es primo"
print(f"El número {usr} {resultado}")

usr = input("\nIntroduce los números: ")
print(filtrar_pares(*map(int, usr.split())))

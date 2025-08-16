# Escribe una función es_primo(n) que determine si un número es primo.


def es_primo(n: int) -> bool:
    primo = True

    if n == 1:
        primo = False

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    return primo


if __name__ == "__main__":
    usr = int(input("Ingrese un número: "))
    resultado = "es primo" if es_primo(usr) == True else "NO es primo"
    print(f"El número {usr} {resultado}")

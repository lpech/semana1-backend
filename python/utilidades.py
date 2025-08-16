# Escribe una función es_primo(n) que determine si un número es primo.
# Crea una función filtrar_pares(lista) que reciba una lista de números y devuelva solo los pares.


def es_primo(n: int) -> bool:
    primo = True

    if n == 1:
        primo = False

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    return primo


def filtrar_pares(*lista: list[int]) -> list:
    for i in lista:
        lista_tmp = [n for n in lista if n % 2 == 0]
        lista = list(lista_tmp)
    return lista

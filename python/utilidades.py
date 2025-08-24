# Escribe una función es_primo(n) que determine si un número es primo.
# Crea una función filtrar_pares(lista) que reciba una lista de números y devuelva solo los pares.


def es_primo(n: int) -> bool:
    """Devuelve True si n es un número primo, False si no."""

    primo = True

    if n == 1 or n < 1:
        primo = False

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    return primo


def filtrar_pares(lista) -> list:
    """Devuelve una lista con los números pares de la lista original."""
    return [n for n in lista if isinstance(n, int) and n % 2 == 0]


def sumar_lista(lista=[0]) -> int:
    """Devuelve la suma de los elementos de la lista."""
    lista_tmp = []
    for n in lista:
        lista_tmp.append(n) if isinstance(n, int) else lista_tmp.append(0)
    lista = lista_tmp
    return sum(lista)


def ejemplo_filtro_num(lista):
    # Convierte "null" a 0 y los demás valores a enteros
    # lista_cadenas = ["null", "1", "null", "3"]
    lista = [int(valor) if valor != "null" else 0 for valor in lista]
    return lista


if __name__ == "__main__":
    print(ejemplo_filtro_num(["null", "1", "null", "3"]))

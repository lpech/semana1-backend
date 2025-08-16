# Crea una función filtrar_pares(lista) que reciba una lista de números y devuelva solo los pares.


def filtrar_pares(*lista: list[int]) -> list:
    for i in lista:
        lista_tmp = [n for n in lista if n % 2 == 0]
        lista = list(lista_tmp)
        # lista.remove(i)
    return lista


if __name__ == "__main__":
    # usr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(type(filtrar_pares(*usr1)))
    usr = input("Introduce los números: ")
    print(filtrar_pares(*map(int, usr.split())))

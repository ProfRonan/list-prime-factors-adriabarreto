"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number <=1:
        return False
    x = 1
    while x < number -1:
        x = 1 + x
        if number % x == 0:
            return False
    return True


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""

    lista = []
    i = 1
    if number <=1:
        print("Insira um número maior")
        return []
    while number >1:
        i = i + 1
        if is_prime(i):
            if number % i == 0:
                number = number // i
                lista.append(i)
                if number >1:
                    i = 1
    return lista

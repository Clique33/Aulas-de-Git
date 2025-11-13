#============================
import random


def random_case(s: str) -> str:
    resultado = ""
    for letra in s:
        if random.randint(0, 1) == 0:
            resultado += letra.lower()
        else:
            resultado += letra.upper()
    return resultado


print(random_case("python"))
print(random_case("Algoritmo"))
print(random_case("paraleleípedo"))

    

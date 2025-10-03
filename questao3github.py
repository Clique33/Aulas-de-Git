import string

def pangrama(frase: str) -> bool:
    alfabeto = set(string.ascii_lowercase)
    
    letras_na_frase = set(frase.lower())
    
    return alfabeto.issubset(letras_na_frase)


print(pangrama("a quick brown fox jumps over the lazy dog"))  
print(pangrama("the five boxing wizards jump quickly"))  

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
print(random_case("Paralelepipedo"))

    

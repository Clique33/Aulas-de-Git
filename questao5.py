from random import randint

def aleatorio_maius_minus(s):
    nova = ""
    for letra in s:
        if randint(0, 1) == 0:  # sorteia 0 ou 1
            nova += letra.lower()
        else:
            nova += letra.upper()
    return nova


# Exemplos de teste
print(aleatorio_maius_minus("algoritmo"))
print(aleatorio_maius_minus("paralelepipedo"))

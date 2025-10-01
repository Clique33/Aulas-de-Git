from random import randint

def aleatoriza_string(s: str) -> str:
    resultado = ""
    for char in s:
        if char.isalpha():
            if randint(0,1)==0:
                resultado +=char.lower()

            else:
                resultado += char.upper()

        else:
            resultado += char

    return resultado

print(aleatoriza_string("algoritmo"))

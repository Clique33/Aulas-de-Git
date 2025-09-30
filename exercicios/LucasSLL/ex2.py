def paridade(a: int, b: int) -> str:
    pa, pb = (a % 2 == 0), (b % 2 == 0)
    if pa and pb:
        return "ambos são pares"
    if not pa and not pb:
        return "ambos são ímpares"
    return "um é par e o outro é ímpar"

if __name__ == "__main__":
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite outro número inteiro: "))
    print(paridade(a, b))
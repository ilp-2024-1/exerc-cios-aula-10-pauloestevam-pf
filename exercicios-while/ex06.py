n = int(input("digite um inteiro positivo: "))

anterior = 0 
atual = 1

termo = 1 
while termo <= n:
    print(anterior, end=" ")
    proximo = anterior + atual
    atual = proximo
    termo += 1

print("\nFim do programa")
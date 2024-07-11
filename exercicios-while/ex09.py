soma = 0
n = int(input("digite um número inteiro: "))
termo = 1

while termo <= n:
    soma += 1 / termo
    termo += 1

print(f"a soma da série harmônica até o termo {n} é: {soma}")
print("fim do programa")
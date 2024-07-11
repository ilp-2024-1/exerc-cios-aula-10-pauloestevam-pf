fatorial = 1
num = int(input("digite um número inteiro: "))

while num > 1:
    fatorial *= num
    num -= 1

    print("o número fatorial é:", fatorial)
    print("fim do programa")
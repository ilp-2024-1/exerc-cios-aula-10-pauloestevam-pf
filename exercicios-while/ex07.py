while True:
    print("digite um número de 1 a 10.000 (ou '0' para encerrar):")
    num = int(input())

    if num == 0:
        break

    if num < 2:
        print(f"o número {num} não é primo.")
    else:
        eprimo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                eprimo = False
                break

        if eprimo:
            print(f"o número {num} é primo.")
        else:
            print(f"o número {num} não é primo.")

print("programa encerrado.")
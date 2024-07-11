print("insira os valores para somar.")
print("para encerrar digite 0.")

soma = 0
while True:
    valor = float(input("insira um valor: "))
    if valor == 0:
        break
    soma += valor

print(f"o valor da soma é: {soma}")
print("programa encerrado.")

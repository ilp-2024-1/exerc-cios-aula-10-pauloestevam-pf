asenha = "pf"

print("por favor, digite a senha.")

while True:
    senha = input("digite sua senha: ")
    
    if senha == asenha:
        print("senha correta! acesso liberado.")
        print("programa encerrado.")
        break
    else:
        print("senha incorreta. tente novamente.")

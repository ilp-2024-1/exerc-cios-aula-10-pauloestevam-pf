import random
numeroaleatorio = random.randint(1,100)
tentativas = 0
print("Um numero aleatório entre 1 e 100 foi gerado, tente adivinhar!")
while True:
    valor = float(input())
    if valor != numeroaleatorio:
        tentativas = tentativas+1            
    if valor == numeroaleatorio:
        print("Você acertou o valor! Programa encerrado")
        print("Você errou "+str(tentativas)+" vezes")
        break

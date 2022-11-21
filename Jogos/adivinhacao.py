import random

print("*" * 33)
print("Bem Vindo ao Jogo!")
print("*" * 33)

num_secret = random.randrange(1, 101)
tentativas = 5
print(num_secret)


for rodada in range(1, tentativas + 1):
    print("\nTentativa {} de {}!".format(rodada, tentativas))
    chute = int(input("Digite um número entre 1 e 100:\n"))

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = (chute == num_secret)
    chute_maior = (chute > num_secret)
    chute_menor = (chute < num_secret)

    print("Você digitou o número {}!".format(chute))

    if acertou:
        print("Você Acertou!")
        break
    else:
        if chute_maior:
            print("Você Errou! Seu chute foi maior que o número secreto!")
        elif chute_menor:
            print("Você Errou! Seu chute foi menor que o número secreto!")
print("Fim do Jogo!!!")
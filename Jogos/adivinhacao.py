print("*" * 33)
print("Bem Vindo ao Jogo!")
print("*" * 33)
num_secret = 50
tentativas = 5
rodada = 1

while (rodada <= tentativas):
    print("\nTentativa {} de {}!".format(rodada, tentativas))
    chute = int(input("Digite o número secreto:\n"))
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
    rodada = (rodada + 1)
print("Fim do Jogo!!!")
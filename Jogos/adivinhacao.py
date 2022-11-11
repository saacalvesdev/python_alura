print("Bem Vindo ao Jogo!")

num_secret = 50
chute = int(input("Digite o número secreto:\n"))
acertou = (num_secret == chute)

print("Você digitou {}".format(chute))

if acertou:
    print("Você Acertou!")
else:
    if num_secret > chute:
        print("Você Errou! Seu chute foi maior que o número secreto!")
    elif num_secret < chute:
        print("Você Errou! Seu chute foi menor que o número secreto!")
print("Fim do Jogo!!!")
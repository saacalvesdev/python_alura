import random

def jogar():
        
    print("*" * 33)
    print("Bem Vindo ao Jogo de Adivinhação!")
    print("*" * 33)

    num_secret = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('(1) Facil (2) Médio (3) Difícil.')
    nivel = int(input('Defina o nível:\n'))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 15
    elif (nivel == 3):
        tentativas = 10    

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
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if chute_maior:
                print("Você Errou! Seu chute foi maior que o número secreto!")
            elif chute_menor:
                print("Você Errou! Seu chute foi menor que o número secreto!")
            
            pontos_perdidos = abs(num_secret - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!!!")

if (__name__ == "__main__"):
    jogar()
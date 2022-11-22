import forca
import adivinhacao

def escolhe_jogo():
    print("*" * 33)
    print("Bem Vindo ao Jogo de Forca!")
    print("*" * 33)

    print('(1) Forca (2) Adivinhação')
    jogo = int(input("Escolha seu Jogo: "))

    if (jogo == 1):
        print('Iniciando o jogo da Forca...')
        forca.jogar()
    elif (jogo == 2):
        print('Iniciando o jogo de Adivinhação...')
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
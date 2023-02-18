from random import randrange

def jogar():
    print("#######################################")
    print("Seja bem-vindo ao jogo de adivinhação!")
    print("#######################################")

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    pensado = randrange(1, 101)

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    pontos = 10000
    rodada = 1

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Que número você chutará de 1 a 100? "))

        acertou = chute == pensado
        maior = chute > pensado
        menor = chute < pensado

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if acertou:
            print("Parabéns! Você acertou!")
            break
        elif maior:
            print("Que pena, amigo, você chutou um número acima...")
            pontos_perdidos = abs(pontos - chute) * 2

        else:
            print("Que pena, amigo, você chutou um número abaixo...")
            pontos_perdidos = abs(pontos - chute) * 2

    if not acertou:
        print(f"Eu havia pensado no número {pensado}, mortal.")

    pontos -= abs(pontos)

    print(f"GAME OVER! Seus pontos foram {pontos}.")


if __name__ == "__main__":
    jogar()

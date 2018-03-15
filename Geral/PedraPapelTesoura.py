jogadro1Pontos = 0
jogadro2Pontos = 0
continuar = True
jogador1Jogada = ""
jogador2Jogada = ""

print("Digite o nome do primeiro jogador:")
jogador1Name = input()

print("Digite o nome do segundo jogador:")
jogador2Name = input()

while continuar:

    while (jogador1Jogada != "pedra" and jogador1Jogada != "tesoura" and jogador1Jogada != "papel"):
        print("Jogador 1:")
        jogador1Jogada = input()

    while (jogador2Jogada != "pedra" and jogador2Jogada != "tesoura" and jogador2Jogada != "papel"):
        print("Jogador 2:")
        jogador2Jogada = input()

    if ((jogador1Jogada == "papel" and jogador2Jogada == "pedra") or
            (jogador1Jogada == "pedra" and jogador2Jogada == "tesoura") or
            (jogador1Jogada == "tesoura" and jogador2Jogada == "papel")):
        print("Jogador 1 vence!")
        jogadro1Pontos += 1
    elif ((jogador1Jogada == "papel" and jogador2Jogada == "tesoura") or
              (jogador1Jogada == "pedra" and jogador2Jogada == "papel") or
              (jogador1Jogada == "tesoura" and jogador2Jogada == "pedra")):
        print("Jogador 2 vence!")
        jogadro2Pontos += 1
    else:
        print("Empate")

    print("Deseja continuar? (N para encerrar, qualquer tecla para continuar) ")
    aux = input()
    jogador1Jogada = ""
    jogador2Jogada = ""
    if aux == "N":
        print("Pontuação:")
        print(jogador1Name + " : " + str(jogadro1Pontos))
        print(jogador2Name + " : " + str(jogadro2Pontos))
        continuar = False
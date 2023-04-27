genero=input("Qual genêro de jogo você gosta? ").upper()
idade=int(input("Quantos anos você tem?"))

if genero == "ACAO":
    if idade >=10:
        print("Recomendo Horizon Zero Dawn")
    elif idade <10:
        print ("Recomendo Mario Bross")
    else:
        print("Digite sua idade")
else:
    if idade >=10:
        print("Recomendo Jogos de acao")
    elif idade <10:
        print ("Recomendo Jogos de plataforma")
    else:
        print("Digite sua idade")
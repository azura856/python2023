
def limites(listaInicial, limiteInferior, limiteSuperior):
    posicao=0
    for item in listaInicial:
        if listaInicial[posicao] >= limiteInferior:
            listaNovaInf.append(listaInicial[posicao])
        if listaInicial[posicao] <= limiteSuperior:
            listaNovaSup.append(listaInicial[posicao])
        posicao+=1



def limites2 (listaInicial, limiteInferior, limiteSuperior):
    sublista = []
    for item in listaInicial:
        if item >= limiteInferior and item <= limiteSuperior:   #ou fica: "if limiteInferior <= item <= limiteSuperior:"
            sublista.append(item)
    print(f'Os valores que estão dentro desses limites são:{sublista}')



listaInicial=[12,14,15,16,18,20,24,26,28,32,34,38]
limiteInferior = 13
limiteSuperior = 26
listaNovaInf=[]
listaNovaSup=[]
sublista = []

limites(listaInicial,limiteInferior, limiteSuperior) #chamando a função limites

print(f'O que está dentro do limite inferior é: {listaNovaInf}')
print(f'O que está dentro do limite superior é: {listaNovaSup}')

limites2(listaInicial, limiteInferior, limiteSuperior)



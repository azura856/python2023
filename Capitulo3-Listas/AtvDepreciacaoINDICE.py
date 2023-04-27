
equipamentos = ["bola","bolsa","sapato","chuteira"]
valores = [50,500,200,600]
depreciacao=input("Digite o nome do produto que será desvalorizado:")

for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo:", valores[indice])
        valores[indice] = valores[indice]*0.9
        print("Novo valor: ", valores[indice])
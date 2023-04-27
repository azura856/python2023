numero = float(input("Digite um numero: "))

def raiz_quadrada(numero):
    x = 60
    for i in range(0,10):
         x = (x+numero/x)/2
    return x

raiz = round(raiz_quadrada(numero), 2)
print("A raíz é:", raiz)

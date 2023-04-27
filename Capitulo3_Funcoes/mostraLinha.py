#programa principal
i=1
#função


def título(txt):
    print("_" * 30)
    print(txt)
    print("_" * 30)

'''
def mostraLinha():
    print("_"*30)


#programa principal
while i<3:
    nome1 = input("Digite um nome: ")
    nome2 = input("Digite um nome: ")

    título(nome1)
    título(nome2)

    i=i+1
print("Acabou")






#função



mostraLinha()
print("    Sistema de alunos")
mostraLinha()
print(" Cadastro de Funcionários")
mostraLinha()
'''
'''
def soma (a,b):
    print (f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

soma(4,5)
soma(8,9)
soma(2,1)
'''
'''
def contador(*núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


contador(5,7,3,1,4)
contador(8,4,7)
'''
'''
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')

contador(5,7,3,1,4)
contador(8,4,7)
'''
def dobra(lst):
    posicao=0
    while posicao<len(lst):
        lst[posicao]*=2
        posicao += 1





def divide(lst):
    posicao=0
    while posicao<len(lst):
        lst[posicao]/=2
        posicao += 1



valores=[7.2,5,0,4]
dobra(valores)
print(valores)
divide(valores)
divide(valores)
print(valores)







































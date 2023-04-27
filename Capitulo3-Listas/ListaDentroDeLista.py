'''
bola=5
equipamentos=[bola,"850","12345","RH"]
valores=["10","20"]
inventario=[equipamentos,valores]
print(inventario[0][0])
print(inventario[0][2])
print(inventario[1][1])
'''
inventario=[]
resposta = "S"
#add elementos
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite ""S"" para continuar: ").upper()
#exibir elementos do inventario
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

#busca e xibição de elemento especifico
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..:", elemento[1])
    print("Serial.:", elemento[2])
#desconto
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])
#exclusao por serial
serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)
#exibição de elemento do inventario(novamente)
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])
#acrescentando valores
valores = []
for elemento in inventario:
  valores.append(elemento[1])
#exibição de maximos, minimos e total
if len(valores) > 0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))
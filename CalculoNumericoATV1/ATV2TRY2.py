num = int(input('Escolha um número : '))
guess = 0.0
de = 0.01
step = de**2
total_guesses = 0
while (abs(guess**2 - num)) >= de: #fazendo uso da função absoluta(abs)
    guess += step
    total_guesses += 1

print('O total de guesses foi: ' + str(total_guesses))
if abs(guess**2-num) >= de:
    print('Falha na raiz quadrada de ' + str(num))
else:
    print(str(guess) + ' é o que está mais próximo da raiz quadrada de ' + str(num))

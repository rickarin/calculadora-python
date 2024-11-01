import sys

print('Você ira digitar seu numero, logo em seguida podera escolher entre 4 Operações, Digite / para divisão, Digite * para multiplicação, Digite + para adição e Digite - para subtração')


acao = input('Escolha a operação: ')

if acao not in ["/", "*", "+", "-"]:
    print('Operação inválida! O programa será encerrado.')
    sys.exit() 

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
total = 0

if acao == "/":
    if num2 != 0:  # Verifica se num2 não é zero
        total = num1 / num2
        print("Resultado:", total)
    else:
        print("Erro: Divisão por zero não é permitida.")
elif acao == '*':
    total = num1 * num2
    print("Resultado:", total)
elif acao == '+':
    total = num1 + num2
    print("Resultado:", total)
elif acao == '-':
    total = num1 - num2
    print("Resultado:", total)
else:
    print('Operação inválida!')


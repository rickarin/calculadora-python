print('Você ira digitar seu numero, logo em seguida podera escolher entre 4 Operações, Digite / para divisão, Digite * para multiplicação, Digite + para adição e Digite - para subtração')


acao = input('Escolha a operação: ')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
total = 0


if acao == "/" :
    total = num1 / num2
    print(total)
elif acao == '*' :
    total = num1 * num2
    print(total)
elif acao == '+' :
    total = num1 + num2
    print(total)
elif acao == '-' :
    total = num1 - num2
    print(total)
else:
    print('Operação Invalida')


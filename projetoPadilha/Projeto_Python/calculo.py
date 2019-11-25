#Essa função exibe um menu para executar as funções de calculo.
def menuCalc():
    while True:
        print('-------------------------------------------------------------------------------------------------------')
        menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))
        print('-------------------------------------------------------------------------------------------------------')
        
        if menu == 1:
            soma()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))

        if menu == 2:
            mult()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))

        if menu == 3:
            sub()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))

        if menu == 4:
            div()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))
        
        if menu == 5:
            potencia()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))

        if menu == 6:
            radiacao()
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))

        if menu == 0:
            print('-------------------------------------------------------------------------------------------------------')
            print('foi um prazer trabalhar com você!')
            print('-------------------------------------------------------------------------------------------------------')
            break

        if menu != 1 & 2 & 3 & 4 & 5 & 6 & 0:
            print('-------------------------------------------------------------------------------------------------------')
            print('\n Ops, você digitou algo de errado, por favor selecione: \n')
            menu = int(input('\n 1 - somar \n 2 - multiplicar \n 3 - subtrair \n 4 - dividir \n 5 - potência \n 6 - radiação \n 0 - sair \n '))
            print('-------------------------------------------------------------------------------------------------------')
#Essas funções de calculo tem como objetivo somar, multiplicar, subtrair e dividir.
def soma():
    num1 = float(input('\n digite o primeiro valor: '))
    num2 = float(input('\n digite o segundo valor: '))              

    soma = num1 + num2 

    print('o resultado é: ', soma)

def mult():
    num1 = float(input('\n digite o primeiro valor: '))
    num2 = float(input('\n digite o segundo valor: '))

    mult = num1 * num2 

    print('o resultado é: ', mult)

def sub():
    num1 = float(input('\n digite o primeiro valor: '))
    num2 = float(input('\n digite o segundo valor: '))

    sub = num1 - num2 

    print('o resultado é: ', sub)

def div():
    num1 = float(input('\n digite o primeiro valor: '))
    num2 = float(input('\n digite o segundo valor: '))

    div = num1 / num2 

    print('o resultado é: ', div)

def potencia():
    num1 = float(input('digite o valor a ser elevado: '))
    num2 = float(input('digite o valor da potencia: '))
    
    potencia = num1 ** num2

    print('o valor da potencia é: ', potencia)

def radiacao():
    num1 = float(input('digite o valor a ser radiado: '))

    potencia = (num1 ** 2)
    aux = (potencia ** (1/2))
    radiacao = (aux ** 0.5)

    print('o valor da radiação é: ', radiacao)
    
print(menuCalc())

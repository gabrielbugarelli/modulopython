'''
essa função conta as letras da string digitada pelo usuário e 
logo em seguida a inverte ao contrário e apresenta na tela
'''
def contaLetras():
    print('-------------------------------------------------------------------------------------------------------')
    nome = input('digite o seu nome: ')
    contador = len(nome)
    inverte = nome[::-1]
    print('-------------------------------------------------------------------------------------------------------')
    print (f'Seja bem vindo {nome}! seu nome possui {contador} letras e invertido fica: {inverte}')
    print('-------------------------------------------------------------------------------------------------------')

print(contaLetras())

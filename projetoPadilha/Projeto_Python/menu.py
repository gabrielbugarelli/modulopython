#Essa função tem como objetivo executar as funcionalidades Calc.py 
def menuPrincipal():

    op = 5 
    while(op!=0):
        op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))

        if op == 1:
            import calculo
            op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))
        if op == 2:
            import listaBebe
            op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))

        if op == 3:
            import letras
            op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))

        if op == 4:
            import textos
            op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))
        if op == 5:
            import matriz
            op = int(input('\n 1 - calcular \n 2 - nome \n 3 - letras \n 4 - textos \n 5 - matriz \n 0 - sair \n '))
        if op == 0:
            print(' ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡ ')
            print('                   Professor Padilha ME PASSA PLEASE! <3 ')
            print(' ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡  ♡ ')
            break
        
print(menuPrincipal())


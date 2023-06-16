while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operador = input('Digite o sinal que você quer usar (+ - * /): ')

    numeros_validos = None

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('O número não é valido' )
        continue

    operadores_validos = '+ - * /'

    if operador not in operadores_validos:
        print('Operador invalido')

    if len(operador)>1:
        print('Digite 1 operador de cada vez')

    if operador == '+':
       print(n1_float + n2_float)

    elif operador == '-':
        print(n1_float - n2_float)

    elif operador == '*':
        print(n1_float * n2_float)

    elif operador == '/':
        print(n1_float / n2_float)
    #Final do codigo
    sair = input('Você Deseja sair ? S[SIM]').lower().startswith('s')

    if sair is True:
        break
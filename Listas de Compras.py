lista = []

while True:
    print('Escolha uma opcao abaixo:')
    op = input('[I]nserir, [A]pagar, [L]istar '
               'Digite [S]air :')


    if op == 'i':
        valor = input('Digite o que deseja acrescentar na lista: ')
        lista.append(valor)

    elif op == 'a':
        valor_indice = input('Digite qual lugar você quer apagar')
        try:
            valor= int(valor_indice)
            del  lista[valor]

        except SyntaxError:
            print('Você está digitando letra! ')

        except ValueError:
            print('Digite um número válido! ')

        except Exception:
            print('Erro desconhecido! ')

    elif op == 'l':
        if lista == 0 :
            print('Não há nada para mostrar na lista! ')
        for i, valor in enumerate(lista):
            print(i,valor)

    elif op == 'S':
        print('Saindo do programa, obrigado por usar! ')
        break
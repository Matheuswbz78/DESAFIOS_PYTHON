palavra = 'pirataria'

usuario = input('Digite uma palavra pra nos ai:')
while True:
    if palavra != usuario:
        print('Palavra incorreta digite novamente!')
        usuario = input('Digite uma palavra pra nos ai:')

    elif palavra == usuario:
        print('Parabéns você acertou a palavra !')
        break

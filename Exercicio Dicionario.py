perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1','2','3','4','5'],
        'Resposta': '4',

    },

    {
        'Pergunta': 'Quanto é 5*5',
        'Opcoes': ['10','15','20','25','30'],
        'Resposta': '25',
    },


]
for pergunta in perguntas:
    print('Pergunta: ',pergunta[('Pergunta')])

    opcoes = pergunta['Opcoes']
    for i,perguntas in enumerate(pergunta['Opcoes']):
        print(f'{i})',perguntas)

    escolha = input('Digite a resposta: ')

    acertou = False
    escolha_int = None
    qtd_opcao = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcao:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou')

    else:
        print('Errou')



nome = 'Matheus'

indice = 0
Novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    Novo_nome += f'*{letra}'
    indice +=1

print(Novo_nome)

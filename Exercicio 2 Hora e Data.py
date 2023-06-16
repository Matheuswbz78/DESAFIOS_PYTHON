hora = int(input('Digite um horario: '))

if hora == 0 or 11:
    print('Bom dia! ')

elif hora == 12 or 17:
    print('Boa tarde! ')

elif hora == 18 or 23:
    print('Boa noite')

else:
    print('Digite um horario valido')
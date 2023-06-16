def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplica= multiplicar(1,2,3,4,5)
print(multiplica)


def par_impar(n1):

    if n1 % 2 ==0:
     return f'{n1} é par'
    else:
     return  f'{n1} é impar'

numero = par_impar(float(input('Digite qual número: ')))
print(numero)
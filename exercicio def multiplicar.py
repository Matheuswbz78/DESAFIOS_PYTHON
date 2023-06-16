def multiplicar(numero):
    return numero*2


n= multiplicar(float(input('Digite um número: ')))
print(n)

def triplicar(numero):
    return  numero*3

n2=triplicar(float(input('Digite um número: ')))
print(n2)

def quadruplicar(numero):
    return  numero*4

n3=quadruplicar(float(input('Digite um número: ')))
print(n3)


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
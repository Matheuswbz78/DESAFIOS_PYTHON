cpf = '47191137886'
nove_digitos = cpf[:9]


contador1 = 10
resultado1 =0
for digito in nove_digitos:
    resultado1 += int(digito) * contador1
    contador1 -= 1
print(resultado1)
digito = (resultado1*10 % 11)
print(digito)
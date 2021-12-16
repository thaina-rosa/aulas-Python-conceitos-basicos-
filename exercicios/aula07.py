n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s= n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
o = n1 ** n2
print('A soma é {}, O produto é {} e a Adivisao é {:.2f}'.format( s, m, d), end=' .')
print('Divisao inteira {} e a potencia{}'.format(di, o))
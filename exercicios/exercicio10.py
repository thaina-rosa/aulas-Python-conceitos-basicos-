# from time import sleep
# print('[====================jogo de adivinhacao===============]')
# nu = int(input('Digite um numero: '))
# num = random.randint(0, 5)
# print('PENSANDO...')
# sleep(3)
# print('O numero sorteado foi: {}'.format(num))
# if nu == num:
#     print('Parabens voce conseguiu adivinhar!!')
# else:
     # print('Não foi dessa vez')

#####################################Exercicio2########################

# velocidade = float(input('Digite um qual a velocidade que o carro esta andando: '))
# cal = ( velocidade-80)*7
# if velocidade > 80:
    # print('Voce foi multado em R${:.2f}'.format(cal))
    # print('Dirija com cuidado')

#####################################Exercicio3########################

# nu = int(input('Digite um numero: '))
# if nu % 2 == 0:
#     print('Este numero é par!')

# else:

    # print('Este numero é impar!!')

#####################################Exercicio4########################
# viagem = int(input('Digite a distancia da sua viagem: '))
# d1 = viagem * 0.50
# d2 = viagem * 0.45
# if viagem <= 200:
#     print('Seu foi gasto com viagem foi de R${}'.format(d1))
#
# else:
#     print('Seu foi gasto com viagem foi de R${}'.format(d2))

#####################################Exercicio4########################
from datetime import date
# ano = int(input('Digite qual o ano que você quer consultar? Caso queira analizar esse ano digite 0 '))
# if ano == 0:
    # ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # print('O ano {} bissexto'.format(ano))
# else:
    # print('O ano {}  nao é um ano bissexto'.format(ano))

#####################################Exercicio5########################

# nu = int(input('Digite um numero: '))
# n2 = int(input('Digite o segundo numero: '))
# n3 = int(input('Digite o terceiro numero: '))
# if nu > n2 and nu > n3:
    # print('O primeiro numero é o numero maior!')
# if n2 > nu and n2 > n3:
    # print('O segundo numero é o numero maior!')
# if n3 > nu and n3 > n2:
    # print('O terceiro numero é o numero maior!')
# if n2 < nu and n2 < n3:
    # print('O segundo numero é o numero menor!')
# if nu < n2 and nu < n3:
    # print('O primeiro numero  é o numero menor!')
# if n3 < nu and n3 < n2:
    # print('O terceiro numero  é o numero menor!')
# else:
    # print('Tente de novo')
#####################################Exercicio5########################

# sa = int(input('Digite seu salario: '))
# ca = (sa * 10)/100
# c2 = (sa * 15)/100
# if sa <= 1250:
#     print('Voce receberá um aumento de 10% e seu salario passará a ser R${}'.format(sa + c2))
# else:
    # print('Voce receberá um aumento de 15% e seu salario passará a ser R${}'.format(sa + ca))

##################################Exercicio6##############################
# print('[====================jogo do triangulo ===============]')
# d1 = int(input('Digite a primeira retas: '))
# d2 = int(input('Digite a segunda retas: '))
# d3 = int(input('Digite a terceira retas: '))
# if d1 < d2 + d3 and d2 < d1 + d3 and d3 < d1 + d2:
    # print('Parabens voce tem um triangulo')
# else:
    # print('Os lados nao se encaixam')

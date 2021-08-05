"""
Exercício 1:
print('Informe dois valores: ')
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print(f'O maior valor é {num1}')

elif num1 == num2:
    print(f'Os dois valores são iguais')

else:
    print(f'Maior valor é {num2}')"""

""" Exercício 2:

print('Informe um número qualquer: ')
import math

num = float(input())
if num  > 0:
    raiz = math.sqrt(num)  # transformei raiz = math.sqrt(num) em uma variável local, ficando fora do else para não dar 
    erro
    print(f'{raiz}')

elif num == 0:
    print(f'Número nêutro')

else:
    print(f'{num} é um número inválido')"""

""" Exercício 3:
 int = todos os numeros que são exatos(não tem vírgula)

print('Informe um valor')
import math
num = int(input()) --> variável global

if num > 0:
    raiz = math.sqrt(num)  --> Variável local
    print(f'{raiz}')
else:
    numelevado = num **2
    print(f'{numelevado}')"""

"""# Exercício 4:
print('Informe um valor qualquer: ')
num = int(input())
import math
if num > 0:
    raiz = math.sqrt(num)
    elevado = raiz **2
    print(f'Número final é: {elevado}')
elif num == 0:
    print('Número nêutro.')

else:
    print('Número inválido')
"""

""""# Exercício 5:
print('Informe um valor: ')
num = int(input())

if num % 2 != 0: # % imprime o módulo da divisão (o resto)
    print('O número inserido é ímpar')

else:
    print('O número inserido é par!')"""

"""# Exercício 6:

print('Informe dois valores inteiros: ')
num1 = int(input())
num2 = int(input())

if num1 > num2:
    sub = num1 - num2
    print(f'Maior número é {num1} e o resultado da  subtração é igual a  {sub}')

elif num1 == num2:
    print(f'Os dois valores são igauis, e sua subtração é igual a 0')

else:
    sub2 = num2 - num1
    print(f'O maior número é {num2} e o resultado da  subtração é igual a  {sub2}')"""

"""# Exercício 7:
print('Informe dois valores: ')
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(f'Maior número é {num1}')
elif num1 == num2:
    print(f'Números iguais!')
else:
    print(f'Maior número é {num2}')"""

""" # Exercício 8:
av1 = 0
av2 = 0
nota1 = float(input('Informe a primeira nota do aluno: \n'))
if 0 <= nota1 < 11:
    av1 = nota1
else:
    print(f'Nota inválida')
    exit()

nota2 = float(input('Informe a segunda nota do aluno: \n'))
if 0 <= nota2 < 11:
    av2 = nota2
else:
    print(f'Nota inválida')
    exit() --> para de executar o programa

notafinal = (nota1 + nota2) / 2
print(f'Nota final do aluno é {notafinal}!')"""

""" # Exercício 9:

salairo = float(input('Informe o valor do salário: \n'))
prestacao = float(input('Informe o valor da prestação: \n'))

if prestacao > (salairo * 0.20):
    print('Emprestimo não liberado.')
else:
    print('Emprestimo liberado.')"""

"""# Exercício 10:

sexo = int(input("Digite seu sexo\n"
                 'Digite 1 para homem \n'
                 'Digite 2 para mulher \n'))

h = float(input('Digite sua altura \n'))

if sexo == 1:
    pi = (72.7 * h) - 58
    print(f'Seu peso ideal é {pi}')
elif sexo ==2:
    pi = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {pi}')
else:
    print('Você não digitou nenhum valor')"""

"""# Exercício 11:
num = int(input('Insira um número: \n'))
num1 = str(num)

if num > 0:
    soma = int(num1[0]) + int(num1[1]) + int(num1[2]) + int(num1[3])
    print(f'Valor final  é {soma}')
else:
   print(f'Valor inválido ')"""

""" # Exercício 12:
import math

num = int(input('Insira um número \n'))
if num > 0:
    print(f'{math.log(num)}')
else:
    print(f'Número inválido!')"""

""" # Exercício 13:

nota1 = float(input('Insira a nota 1: \n'))
peso1 = int(input(f'Insira o peso da prova \n'))

nota2 = float(input('Insira a nota 2: \n'))
peso2 = int(input(f'Insira o peso da prova \n'))

nota3 = float(input('Insira a nota 3: \n'))
peso3 = int(input(f'Insira o peso da prova \n'))

prova1 = nota1 * peso1
prova2 = nota2 * peso2
prova3 = nota3 * peso3/ peso3

media_final = (prova1 + prova2 + prova3) / 3

if media_final >= 6.0:
    print(f'Aluno aprovado! Sua nota foi: {media_final} ')
else:
    print(f'Aluno reprovado! Sua nota foi: {media_final}')"""

""" # Exercício 14:
Nota trabalho --> peso2 
Nota prova semestral --> peso3
 nota da prova final --> peso5 

trabalho = float(input('Informe a nota do trabalho: \n'))
peso1 = int(input('Informe o peso do trabalho: \n'))

prova_semestral = float(input('Informe a nota da prova semestral: \n'))
peso2 = int(input('Informe o peso da avaliação semestral:  \n'))

prova_final = float(input('Informe a nota da prova final: \n'))
peso3 = int(input('Informe o peso do exame final: \n'))

nota1 = trabalho * peso1

nota2 = prova_semestral * peso2

nota3 = prova_final * peso3

pesofinal = peso1 + peso2 + peso3
notafinal = (nota1 + nota2 + nota3) / pesofinal

if notafinal < 2.9:
    print(f'Aluno reprovado! Sua nota foi {notafinal}')
elif (notafinal > 3) and (notafinal < 4.9):
    print(f'Aluno em recuperação! Sua nota  foi {notafinal}')
else:
    print(f'Aluno aprovado! Sua nota foi {notafinal}')"""

"""# Exercício 15:

diadasemana = ['domingo',
               'segunda',
               'terça',
               'quarta',
               'quinta',
               'sexta',
               'sábado']

dia = int(input('Digite o dia da semana  \n'))

if 1 < dia > 7:
    print(f'Esse dia não existe')
else:
    print(f'O dia selecionado é: {diadasemana[dia - 1]}.')"""

"""# Exercício 16:

mesdoano = ['janeiro',
            'fevereiro',
            'março',
            'abril',
            'maio',
            'junho',
            'julho',
            'agosto',
            'setembro',
            'outubro',
            'novembro',
            'dezembro']

mes = int(input('Informe um mês do ano: \n'))

if 1 < mes > 12:
    print(f'Esse mês não existe!')
else:
    print(f'O mês selecionado foi {mesdoano[mes - 1]}')"""

"""# Exercício 17:

basemaior = float(input('Informe a base maior do trapézio: \n'))
basemenor = float(input('Informe a base menor do trapézio: \n'))
altura = float(input('Informe a altura do trapézio:  \n'))

area = ((basemaior + basemenor) * altura) / 2

if basemaior < 0 or basemenor < 0:
    print(f'Base invalida')
else:
    print(f'Área correspondente do trapézio é: {area}')"""

"""# Exercício 18:

operacao = input('Informe a operação desejada: \n')

if operacao == 'Soma' or operacao == 'soma':
    print(f'Informe dois valores: ')
    a = float(input())
    b = float(input())
    resultado = a + b
    print(f'Resultado final é {resultado}')

elif operacao == 'Subtração' or operacao == 'subtraçao':
    print(f'Informe dois valores: ')
    a = float(input())
    b = float(input())
    resultado = a - b
    print(f'Resultado final é: {resultado}')

elif operacao == 'Divisão' or operacao  == 'divisao':
    print(f'Informe dois valores: ')
    a = float(input())
    b = float(input())
    resultado = a / b
    print(f'Resultado final é: {resultado}')

elif operacao == 'Multiplicação' or operacao == 'multiplicaçao':
    print(f'Informe dois valores: ')
    a = float(input())
    b = float(input())
    resultado = a * b
    print(f'Resultado final é: {resultado}')"""

""" # Exercício 19:
num = int(input('Informe um numero que seja divisivel por 3 e 5, mas não pelos dois respectivamente \n'))

while num % 3 == 0 and num % 5 == 0:
    num = int(input("Digite o numero novamente, pois esse numero é divisível por 3 e 5 \n"))

while num % 3 != 0 and num % 5 != 0:
    num = int(input("Digite o numero novamente, pois esse numero não é divisível por 3 ou 5 \n"))

if num % 3 == 0:
    print(f'O número informado é divisível por 3')
else:
    print(f'O número informado é divisível por 5')
# --> Necessita de loop"""

""" # Exercício 20:

lado1 = int(input('Informe o lado 1: \n'))
lado2 = int(input('Informe o lado 2: \n'))
lado3 = int(input('Informe o lado 3: \n'))

if lado1 == lado2 and lado2 == lado3:
    print(f'É um triângulo equilátero.')

elif lado1 == lado2 or lado2 == lado3:
    print(f'É um triângulo isóceles')

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print(f'É um triângulo escaleno')
    --> Necessita de loop
    """
"""# Exercício 21:
while True:
    opcao = str(input('Escolha:'
                  'Soma de 2 números, Diferença de dois números (maior pelo menor), Produto entre dois números, '
                  'e Divisão de 2 números, o denominador nao pode ser zero! \n'))

    if opcao == 'Soma de 2 números':
        a = int(input())
        b = int(input())
        resultado = a + b
        print(f'Resultado final é {resultado}')

    elif opcao == 'Diferença de dois números':
        a = int(input())
        b = int(input())
        resultado = a - b
        print(f'Resultado final é {resultado}')

    elif opcao == 'Produto entre dois números':
        a = int(input())
        b = int(input())
        resultado = a * b
        print(f'Resultado final é {resultado}')

    elif opcao == 'Divisão de 2 números':
        a = int(input())
        b = int(input())
        resultado = a / b
        print(f'Resultado final é {resultado}')

    else:
        if opcao != 'Soma de 2 números' or 'Diferença de dois números' or 'Produto entre dois números' or 'Divisão de 2 números': print(f'ERRO!')"""

"""# Exercício 22:

idade = int(input('Informe sua idade: '))
servico = int(input('Informe o tempo de serviço: '))

if idade >= 65:
    print(f'Pode se aposentar!')
elif servico >= 30:
    print(f'Pode se aposentar!')
elif idade >= 60 and servico > 25:
    print(f'Pode se aposentar!')
else:
    print(f'Não pode se aposentar!')"""

"""# Exercício 23:

ano = int(input('Informe um ano: '))

if (ano % 4 == 0) and (ano % 100 != 0)            :
    print(f'Ano bissexto!')
else:
    print(f'Não é!')
"""

"""# Exercício 24:
#while True:
    preco = int(input('Informe o preço do produto: '))
    estado = str(input('Informe o estado desejado: '))

    if estado == 'MG':
        resultado = preco * 7 / 100
        print(f'Valor do imposto é {resultado:.4f}')

    elif estado == 'SP':
        resultado = preco * 12 / 100
        print(f'Valor do imposto é {resultado}')

    elif estado == 'RJ':
        resultado = (preco * 15 / 100)
        print(f'Valor do imposto é {resultado}')

    elif estado == 'MS':
        resultado = (preco * 8 / 100)
        print(f'Valor do imposto é {resultado}')

    else:
        if estado != 'MG' or estado != 'SP' or estado != 'Rj' or estado != 'MS':
            print(f'Erro!')"""

"""# Exercício 25:
import math
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print(f'Não existe raiz!')

elif delta == 0:
    raiz = (-1 * b + (math.sqrt(delta))/(2 * a))
    print(f'Existe uma raiz apenas, que é {delta}')

elif delta >= 0:
    x1 = (-1 * b + math.sqrt(delta) / (2 * a))
    x2 = (-1 * b - math.sqrt(delta) / (2 * a))
    print(f'AS raizes são: {x1} e {x2}')"""

"""# Exercício 26:

km = float(input('Informe quantos KM rodaram: \n'))
litros = float(input('Informe quantos litros de gasolina foram gastos: \n'))

consumo = km / litros

if consumo < 8:
    print(f'Venda o carro!')
elif 8 < consumo < 14:
    print(f'Econômico!')
elif consumo > 12:
    print(f'Super econômico!')
"""

"""# Exercício 27:

idade = int(input('Informe sua idade: \n'))

if 5 <= idade <= 7:
    print(f'Categoria Infatil A')
elif 8 <= idade <= 10:
    print(f'Categoria Infantil B')
elif 11 <= idade <= 13:
    print(f'Categoria Juvenil A')
elif 14 <= idade <= 17:
    print(f'Categoria Juvenil B')
elif idade >= 18:
    print(f'Categoria Sênior')
else:
    if idade < 5:
        print('Idade inválida!')"""

"""# Exercício 28:

x = int(input('Informe o valor de X: \n'))
y = int(input('Informe o valor de Y: \n'))
z = int(input('Informe o valor de Z: \n'))

opcao = str(input('Informe qual opção quer: '))
if opcao == 'Geométrica' or opcao == 'geometrica':
    print(f'A média Geométrica dos valores escolhidos é: {(x * y * z) ** (1 / 3)}')
elif opcao == 'Ponderada' or opcao == 'ponderada':
    print(f'A média Ponderada dos valores escolhidos é: {((x + 2 * y + 3 * z) / 6)}')
elif opcao == 'Harmônica' or opcao == 'harmonica':
    print(f'A média Hamônica dos valores escolhidos é: {1 / (1 / x + (1 / y) + (1 / z))}')
elif opcao == 'Aritmética' or opcao == 'aritmetica':
    print(f'A média Aritmética dos valores escolhidos é: {(x + y + z) / 3}')
else:
    if opcao != 'Geométrica' or 'Ponderada' or 'Harmônica' or 'Aritmética':
        print('Erro ao selecionar operação!')
"""

"""# Exercício 29:
from random import randint --> randint importa números aleatórios 

count = 0
cert = 0

while count < 5:
    count = count + 1
    num1 = randint(0, 99)
    num2 = randint(0, 99)
    aResp = int(input(f'Pergunte um número  {count}. \n'
                      f'Digite abaixo a soma de  {num1} +{num2} \n'))
    resp = (num1 + num2)
    if aResp != resp:
        print(f'Você errou, a soma de {num1} + {num2} \n')
        print(f'Você tem {cert} acertos')
    else:
        print(f'Você acertou! A soma de {num1} + {num2} é: {aResp} \n')
        cert = cert + 1
        print(f'Você tem {cert} acertos \n')"""

"""# Exercício 30:

numero1 = int(input('Informe um número: \n'))
numero2 = int(input('Informe um número: \n'))
numero3 = int(input('Informe um número: \n'))

if numero1 < numero2 < numero3:
    print(f'A ordem é: {numero1} , {numero2} e {numero3}')
elif numero2 < numero1 < numero3:
    print(f'A ordem é: {numero2} , {numero1} e {numero3}')
elif numero3 < numero1 < numero2:
    print(f'A ordem é: {numero3} , {numero1} , {numero2}')
elif numero1 > numero2 > numero3:
    print(f'{numero3} , {numero2} , {numero1}')
else:
    if numero1 == numero2 == numero3:
        print(f'São iguais!')
    elif numero1 == numero2:
        print(f'Número 1 e 2 são iguais!')
    elif numero1 == numero3:
        print(f'Número 1 e 3 são iguais!')
    elif numero2 == numero3:
        print('Número 2 e 3 são iguais!')"""

"""# Exercício 31:

altura = float(input('Informe seua altura: \n'))
peso = float(input('Informe seu peso: \n'))

if altura < 1.20 and peso <= 60:
    print(f'Classificação A')
elif altura < 1.20 and 60 < peso <= 90:
    print(f'Classificação D')
elif altura < 1.20 and peso > 90:
    print(f'Classificação G')
elif 1.20 < altura <= 1.70 and peso <= 60:
    print(f'Classificação B')
elif 1.20 < altura < 1.70 and 60 < peso <= 90:
    print(f'Classificação E')
elif 1.20 < altura < 1.70 and peso > 90:
    print(f'Classificação H')
elif altura > 1.70 and peso <= 60:
    print(f'Classificação C')
elif altura > 1.70 and 60 < peso <= 90:
    print(f'Classificação F')
elif altura > 1.70 and peso > 90:
    print(f'Classificação I')
else:
    print(f'Valores inválidos, ou, você está muito magro!')"""

""""# Exercício 32:
print('               CARDÁPIO \n'
      'Especificação:      Código:    Preço: \n'
      ' -Cachorro Quente    |100|      R$ 1.20 \n'
      ' -Bauru Simples      |101|      R$ 1.30 \n'
      ' -Bauro com Ovo      |102|      R$ 1.50 \n'
      ' -Hamburguer         |103|      R$ 1.20 \n'
      ' -Chessburguer       |104|      R$ 1.70 \n'
      ' -Suco               |105|      R$ 2.20 \n'
      ' -Refrigerante       |106|      R$ 1.00 \n')
codigo = 0
while codigo == 100 or 101 or 102 or 103 or 104 or 105 or 106:
    codigo = int(input('Informe o código do produto: \n'))
    quantidade = int(input('Informe a quantidade: \n'))

    if codigo == 100:
        preco = quantidade * 1.20
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 101:
        preco = quantidade * 1.30
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 102:
        preco = quantidade * 1.50
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 103:
        preco = quantidade * 1.20
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 104:
        preco = quantidade * 1.70
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 105:
        preco = quantidade * 2.20
        print(f'Preço total é: {preco:.2f}')
    elif codigo == 106:
        preco = quantidade * 1.00
        print(f'Preço total é: {preco:.2f}')
    else:
        if codigo != 100 or 101 or 102 or 103 or 104 or 105 or 106:
            print(f'Código do produto inválido!')
            break"""

"""# Exercício 33:

preco = float(input('Informe o preço do produto: '))

if preco <= 50:
    precofinal = preco + 1.05
elif 50 < preco < 100:
    preco = preco * 1.10
else:
    preco = preco * 1.15

print(f'O valor do produto atualizado é {preco:.2f}')

if preco <= 80:
    print(f'Barato')
elif 80 < preco <= 120:
    print(f'Normal')
elif 120 < preco <= 200:
    print(f'Caro')
else:
    print(f'Muito caro!')"""

"""# Exercício 34:

nota = float(input('Informe sua nota: \n'))
faltas = int(input('Informe a quantidade de faltas: \n'))

while 10 < nota > 0:
    print("Nota invalida, digite uma nota de 0 a 10 \n")
    nota = float(input("Digite a nota do aluno \n"))
if 9 < nota <= 10 and faltas <= 20:
    print(f'Conceito até 20 faltas: A')
elif 9 < nota <= 10 and faltas >= 20:
    print(f'Conceito acima de 20 faltas: B')
elif 7.5 < nota <= 8.9 and faltas <= 20:
    print(f'Conceito até 20 faltas: B')
elif 7.5 < nota <= 8.9 and faltas >= 20:
    print(f'Conceito acima de 20 faltas: C')
elif 5 < nota <= 7.4 and faltas <= 20:
    print(f'Conceito até 20 faltas: C')
elif 5 < nota <= 7.4 and faltas >= 20:
    print(f'Conceito mais de 20 faltas: D')
elif 4 < nota <= 4.9 and faltas <= 20:
    print(f'Conceito até 20 faltas: D')
elif 4 < nota <= 4.9 and faltas >= 20:
    print(f'Conceito de acima de 20 faltas: E')
elif 0 < nota <= 3.9 and faltas <= 20:
    print(f'Conceito até 20 faltas: E')
elif 0 < nota <= 3.9 and faltas >= 20:
    print(f'Conceito de acima de 20 faltas: E') """

""" # Exercício 35:

data = input('Insira uma data qualquer: dd/mm/yyyy ')
dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

valida = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if 1 <= dia <= 31:
        valida = 1
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= dia <= 30:
        valida = 1
elif mes == 2:
    if ano %400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        if dia <= 29:
            valida = 1
    elif dia <= 28:
        valida = 1

if valida == 1:
    print(f'A data {data} é válida')
else:
    print(f'A data {data} não é válida') """

"""# Exercício 36

venda = float(input('Informe o valor da venda: '))

if venda >= 100.000:
    comissao = (venda * 0.16) / 100
    final = comissao + 700
    print(f'Valor a receber é {final:.2f} ')
elif 100.000 > venda >= 80.000:
    comissao = (venda * 0.14) / 100
    final = comissao + 650
    print(f'Valor a receber é : {final:.2f}')
elif 80.00 > venda >= 60.000:
    comissao = (venda * 0.14) / 100
    final = comissao + 600
    print(f'Valor a receber é: {final:.2f}')
elif 60.000 > venda >= 40.000:
    comissao = (venda * 0.14) / 100
    final = comissao + 550
    print(f'Valor a receber é: {final:.2f}')
elif 40.000 > venda >= 20.000:
    comissao = (venda * 0.14) / 100
    final = comissao + 500
    print(f'Valor a receber é {final:.2f}')
elif venda < 20.000:
    comissao = (venda * 0.14) / 100
    final = comissao +  400
    print(f'Valor a receber é {final:.2f}') """

""" # Exercício 37:

chegada = str(input('Digite a hora de chegada \n'))
saida = str(input('Digite a hora de saída \n'))

hor, minu = chegada.split(':')
sHor, sMinu = saida.split(':')

hor = int(hor)
minu = int(minu)
sHor = int(sHor)
sMinu = int(sMinu)
temM = 0
temH = 0

if hor < sHor:
    temH = 24 - (sHor - hor)
    if minu < sMinu:
        temH = temM + 1
elif hor > sHor:
    temh = 24 - (hor - sHor)
    if minu < sMinu:
        temH = temH + 1
elif hor == sHor and minu > sMinu:
    temH = 24
elif hor == sHor and minu == sMinu:
    temH = 1
elif hor == sHor and minu < sMinu:
    temH = 1

if temH < 3:
    print(f'O valor a ser cobrado será de R${temH * 1:.2f}')
elif 2 < temH < 5:
    print(f'O valor a ser cobrado será de R${(2 * 1) + ((temH - 2) * 1.4):.2f}')
else:
    print(f'O valor a ser cobrado será de R${((2 * 1) + (2 * 1.4) + (temH - 4) * 2):.2f}')"""

"""# Exercício 38:

data = input('Insira uma data qualquer: dd/mm/yyyy ')
dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)
valida = 0
if ano >= 2008:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 1 <= dia <= 31:
            valida = 1
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if 1 <= dia <= 30:
            valida = 1
    elif mes == 2:
        if ano %400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            if dia <= 29:
                valida = 1
        elif dia <= 28:
            valida = 1

if valida == 1:
    print(f'A data {data} é válida!')
else:
    print(f'A data {data} não é válida!')"""

"""# Exercício 39:

salario = float(input('Informe seu salário atual:  \n'))
tempo_na_empresa = int(input('Informe quantos meses está na empresa: \n'))

tempo_na_empresa = tempo_na_empresa / 12

if salario <= 500:
    salario = salario * 1.25
elif salario <= 1000:
    salario = salario * 1.20
elif salario <= 1500:
    salario = salario * 1.15
elif salario <= 2000:
    salario = salario * 1.10

if 0 < tempo_na_empresa < 4:
    salario = salario + 100
elif 3 < tempo_na_empresa < 7:
    salario = salario + 200
elif 6 < tempo_na_empresa < 11:
    salario = salario + 300
elif tempo_na_empresa > 10:
    salario = salario + 500

print(f'O novo salário é de R${salario:.3f}')"""


"""# Exercício 40:
custo = float(input('Informe o valor: \n'))

if custo <= 12000:
    custo_de_fabrica = custo * 1.05
    print(f'Valor final é {custo_de_fabrica:.2f} reais.')
elif 12000 < custo < 250000:
    custo_de_fabrica = custo * 1.10
    valor_imposto = custo_de_fabrica + (custo_de_fabrica * 0.15)
    print(f'Valor final é {valor_imposto:.2f} reais.')
elif custo > 25000:
    custo_de_fabrica = custo * 1.15
    valor_imposto = custo_de_fabrica + (custo_de_fabrica * 0.20)
    print(f'Valor final é {valor_imposto:.2f} reais.') """

"""# Exercício 41:
# IMC = peso/ (altura x altura)

peso = float(input('Informe seu peso: \n'))
altura = float(input('Informe sua altura: \n '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f'Abaixo do peso')
elif 18.6 < IMC < 24.9:
    print(f'Saudável')
elif 25.0 < IMC < 29.9:
    print(f'Peso em excesso')
elif 30.0 < IMC < 34.9:
    print(f'Obesidade Grau 1')
elif 35.0 < IMC < 39.9:
    print(f'Obesidade Grau 2')
elif IMC >= 40.0:
    print(f'Obesidade Grau 3 (Mórbida!)')"""

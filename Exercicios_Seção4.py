
# Exercícios seção 4:

# 1:
"""valor = 1
print(valor) 

# 2:
valoro = 0.5
print(valoro) 

# 3:

valor1 =int(input('Digite um valor: '))
valor2 =int( input('Digite um segundo valor: '))
valor3 = int(input('Digite um terceiro valor: '))
soma= valor1+valor2+valor3
print(f'a soma de {valor1} mais {valor2} mais {valor3} é {soma}')"""""

# 4
"""valor1= int(input('Insira um número: '))
valor2 = valor1 ** 2
print(f'Resultado final é {valor2}')"""

# 5
"""valor1 = int(input('Insira um numero: '))
valor2 = valor1 / 5
print(f'Resultado é {valor2}')

# 6

print('Insira um valor:')
F = float(input())
num =(F * (9/5) + 32)
print(f'Resultado em fahrenheit é {num}')
print(type(num))

# 7

print('Insira um valor:')
F = float(input())
C = 5 * (F - 32)/9
print(f'Resultado em celsius é {C}')

# 8
print('Insira um valor')
K = float(input())
C = (K - 273.15)
print(f'Resultado é {C}')

# 9
print('Insira um valor:')
C = float(input())
K = (C + 273.15)
print(f'Resultado em K é {K}')

# 10
print('Insira a velocidade:')
# M =K/3.6
K = float(input())
M = (K / 3.6)
print(f'Velocidade em MS é {M}')

# 11

print('Insira a velocidade desejada:')
M = float(input())
K = (M * 3.6)
print(f'Velocidade em KM é {K}')

# 12
# K = 1.61  * M
print('Informe a distância:')
M = float(input())
K = (1.61 * M)
print(f'A distância em KM é {K}')

# 13
print('Insira a distância: ')
K = float(input())
M = (K / 1.61)
print(f'A distância em milhas é: {M}')

# 14

print('Informe um valor')
G = float(input())
R = G * 180/ 3.14
print(f'O resultado é {R}')

# 15
print('Informe um valor:')
R = float(input())
G = R * 180 / 3.14
print(f'Resultado é {G}')

# 16
print('Informe o comprimento total:')
P = float(input())
C = P * 2.54
print(f'A distância em CM é {C}') 

# 17
print('Informe o comprimento atual: ')
C = float(input())
P = C / 2.54
print(f'A distância em milhas é {P}') 

# 18

print('Informe o valor: ')
M = float(input())
L = 1000 * M
print(f'Valor em litros cúbicos é {L}')

# 19
print('Informe o volume:')
L = float(input())
P = L / 1000
print(f'Valor é {P}')

# 20
print('Informe o peso:')
quilogramas =  float(input())
KG = quilogramas / 0.45
print(f'Valor em KG é {KG}')

# 21
print('Insira um valor:')
L = float(input())
quilogramas = L * 0.45
print(f'Valor é {quilogramas}')

# 22
print('Insira o comprimento:')
J = float(input())
M = J * 0.91
print(f'Valor em metros  é {J}')

# 23
print('Insira o comprimento')
M = float(input())
J = M / 0.91
print(f'Valor em Jardas é {J}')

# 24
print('Insira o valor')
M = float(input())
Acre = M * 0.000247
print(f'Valor em Acres é {Acre}') 

# 25
print('Insira o valor:')
Acres = float(input())
Mquadrados = Acres * 4048.58
print(f'Valor em M² é {Mquadrados}')

# 26
print('Insira o valor desejado: ')
metrosquadrados = float(input())
hectares = metrosquadrados * 0.0001
print(f'o resultado em hectares é {hectares}')

# 27
print('Insira o valor desejado:')
hectares = float(input())
Metrosquadrados = hectares * 10000
print(f'O resultado é {Metrosquadrados}')

# 28
print('Insira tres números:')
print('Valor 1')
val1 = float(input())
print('Valor 2')
val2 = float(input())
print('Valor 3 ')
val3 = float(input())
qv1 = val1 ** 2
qv2 = val2 ** 2
qv3 = val3 ** 2
soma = qv1 + qv2 + qv3
print(f'valor é {soma}')

# 29
print('Insira o valor das quatro notas:')
print('Nota 1:')
media1 = float(input())
print('Nota 2:')
media2 = float(input())
print('Nota 3: ')
media3 = float(input())
print('Nota 4: ')
media4 = float(input())
mediafinal = (media1 + media2 + media3 + media4) / 5
print(f'Média final é {mediafinal}')

# 30
print('Insira o valor')
real = float(input())
cotacao = real * 5.00
print(f'Valor em dólar é {cotacao}')

#31
print('Insira um número:')
A = int(input())
B = A + 1
C = A - 1
print(f'O sucessor é {B} e o antecessor é {C}')

# 32

print('Insira um valor inteiro: ')
A = int(input())
B = (A + 1) * 3
C = (A - 1) * 2
print(f'O antecessor é {C} e o sucessor é {B}')

# 33
print('Insira um valor ')
A = float(input())
B = A ** 2
print(f'A área é {B}') 

# 34
print('Insira o valor do raio do círculo:')
C= float(input())
AC =  C ** 2 * 3.141592
print(f'A Área do círculo é {AC}') 

#  35
import math
print('Insira o valor A: ')
A = float(input())
print('Insira o valor B: ')
B = float(input())
H = math.sqrt(A**2 + B**2)
print(f'Hipotenusa é {H}')

# 36
print('Insira a altura: ')
altura = float(input())
print('Insira o raio: ')
raio= float(input())
volumecilindro = 3.141592 * raio ** 2 * altura 
print(f'Volume do cilindro é {volumecilindro}') 

# 37
print('Insira o valor total:')
valortotal = float(input())
valorfinal = valortotal - (valortotal * 12 /100)
print(f'Valor final é {valorfinal}') 

# 38
print('Insira valor do salário:')
salario = float(input())
novosalario = salario + (salario * 25 /100)
print(f'Novo salário é {novosalario}') 

# 39
"primeiro colocado --> 46%" \
"segundo colocado --> 32%" \
" terceiro colocado --> 28%"
primeirocolocado = (780.000 * 46) / 100
segundocolocado = (780.00 * 32) / 100
terceirocolocado = (780.000 * 22) / 100
print(f"O primeiro colocado vai ganhar {primeirocolocado}")
print(f'O segundo colocado vai ganhar {segundocolocado}')
print(f'O terceiro colocado vai ganhar {terceirocolocado}') 

# 40
print('Informe a quantidade de dias trabalhados:')
dias = float(input())
pagamento = dias * 30
pagamento_final = (pagamento * 8) / 100
pagamentofinalfinal = (pagamento - pagamento_final)
print(f'Valor final {pagamentofinalfinal}') 

# 41
print('Informe a quantidade de dias trabalhados e horas')
diastrabalhados = float(input())
horastrabalhadas = float(input())
salario = diastrabalhados * horastrabalhadas
salario_final = salario + (salario * 10 / 100)
print(f'Salário final é de {salario_final} reais')

# 42
print('Informe seu salário')
salario_base = float(input())
salario_medio = salario_base + (salario_base * 5 / 100)
salario_pre_final = salario_medio - (salario_medio * 7 / 100)
print(f'Salário final é R${salario_pre_final}')

# 43
print('Informe o valor da mercadoria ')
mercadoria = float(input())
mercadoria_avista = mercadoria - (mercadoria * 10 / 100)
mercadoria_parcelada = mercadoria / 3
comissao_avista = (mercadoria_avista * 5) / 100
comissao_parcelada = (mercadoria_parcelada * 5) / 100

print(f"Se a mercadoria for paga a vista, o valor será de {mercadoria_avista:.2f}")
print(f"Se a mercadoria for paga parcelada, o valor será de {mercadoria_parcelada:.2f}")
print(f"A comissão a vista será de: {comissao_avista}")
print(f"A comissão parcelada será de {comissao_parcelada}") 

# 44
print('Informe a altura do degrau em CM: ')
altura_degrau = float(input())
print('Informe qual altura deseja atingir subindo a escada(em CM)')
altura_atingir = float(input())
alturafinal = altura_atingir / altura_degrau
print(f"Você vai precisar subir {alturafinal} degrais") 

# 45
print('Informe um texto ')
nome = str(input())
print(nome.lower())

# 46
    Forma bonita  
print('Informe um número de 100 a 999')
num = int(input())
while num < 100 or num > 999:
    print('Digite um numero de 100 a 999')
    num = int(input())

num = str(num)
reverse = num[::-1]
print(f"O numero digitado invertido é {reverse}")
-
    Forma Feia
print('Informe um valor entre 100 e 999')
numero = int(input())
num = str(numero)
print(num[::-1]) 

# 47
print("Digite um número entre 1000 e 9999" )
num = int(input())

while num < 1000 or num > 9999:
 print("Digite um número entre 1000 e 9999")
 num = int(input())

print(f"Primeiro digito é {str(num)[0]}")
print(f"Segundo digito é {str(num)[1]}")
print(f"Terceiro digito é {str(num)[2]}")
print(f"Quarto digito é {str(num)[3]}")

# 48
print('Insira um valor: ')
segundos = float(input())
minutos = segundos / 60
horas = segundos / 3600
segundos = segundos
print(f"Valor em minutos é {minutos}")
print(f"Valor em horas é {horas}")
print(f"Valor em segundos é {segundos}") 

# 49
print('Informe as horas, minutos e segundos abaixo')
print('Horas(s)')
hor = int(input())
print('Minuto(s)')
min = int(input())
print('Segundo(s)')
seg = int(input())
print('Informe a duração em segundos: ')
dur = int(input())

hor = hor * 3600
min = min * 600
tSec = hor + min + seg + dur

hFinal = int(tSec / 3600)
rest = tSec % 3600
miFinal = int(rest / 60)
rest = rest % 60

print(f"A experiência irá terminar as: {hFinal}:{miFinal}:{rest}") 

# 50
print('Informe sua idade')
idade = int(input())
print('Informe o ano que estamos')
ano = int(input())
final = ano - idade
print(f"Você nasceu no ano de {final}")

# 51
x1 = int(input(f"Informe x1 ==> "))
y1 = int(input(f"Informe y1 ==> "))

# elevar à uma fracão corresponde a tirar a raiz tendo como com indice
#  número indicado no denominador

distancia = int((((0 - x1) ** 2) + (( 0 - y1) ** 2)) ** (1/2))

print(f"A distância entre a origem (0,0) e o ponto de"
      f"coordenadas ({x1}, {y1} é {distancia}")

# Demonstrando o cálculo

print(f'x2 - x1 = {0 - x1}, \n'
      f'y2 - y1 = {0 - y1}')
print(f'(x2 - x1) ** 2 = {(0 - x1) ** 2}, \n'
      f'(y2 - y1) ** 2 = {(0 - y1) ** 2}')

print(f'Distância da origem = {distancia}') 

# 52
print('Informe o valor do prêmio: ')
premio = float(input())
print('Informe o valor do apostador 1: ')
ap1 = float(input())
print('Informe o valor do apostador 2: ')
ap2 = float(input())
print('Informe o valor do apostador 3: ')
ap3 = float(input())

aTotal = ap1 + ap2 + ap3

pap1 = ap1 / aTotal
pap2 = ap2 / aTotal
pap3 = ap3 / aTotal

val1 = pap1 * premio
val2 = pap2 * premio
val3 = pap3 * premio

print(f"O prêmio do apostador 1 é:  {val1:.2f}")
print(f"O prêmio do apostador 2 é: {val2:.2f}")
print(f"O prêmio do apostador 3 é: {val3:.2f}")

# 53
print('Informe o comprimento do terreno')
c = float(input())
print('Informe a largura do terreno')
l = float(input())
print('Digite o valor do metro da tela:')
tela = float(input())
precotela = c * l
precofinal = precotela * tela
print(f"Valor total é {precofinal}")"""

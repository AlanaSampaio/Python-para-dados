#Imports

import math
import random
import datetime
import calendar

# 1 - Escreva um programa que mostre a mensagem 'Hello World!' na tela.

print("Hello World!\n\n")

# 2 - Faça um programa que solicite um número do usuário e apresente a seguinte mensagem na tela: "O número digitado foi [número]".

num = input("Digite um número: ")
print(f"O número digitado foi {num}\n\n")

# 3 - Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.

nome = input(str("Digite seu nome: "))
sobrenome = input(str("Digite seu sobrenome: "))
print(f"Seu nome completo é {nome} {sobrenome}\n\n")

# 4 - ::Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))
soma = num_1+num_2+num_3
print("A soma dos números é: {:.2f}" .format(soma))
print(f'A soma dos números é: {soma:.2f}\n\n')

# 5 - Escreva um programa que solicite duas notas do usuário e apresente a média na tela da seguinte forma:
#"A média das notas [nota1] e [nota2] é [média]"

nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
media = (nota_1+nota_2)/2
print(f'A média das notas {nota_1:.2f} e {nota_2:.2f} é {media:.2f}\n\n')

# 6 - Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa deve mostrar na tela o resultado da raiz quadrada do número inserido.

num_4 = float(input("Insira um número: "))
print(f"A raiz quadrada de {num_4} é {math.sqrt(num_4):.2f}\n\n")

# 7 - Faça um programa que peça 5 números de ponto flutuante do usuário e apresente no final a média dos números digitados.

numero_flutuante_1 = float(input("Digite o primeiro número: "))
numero_flutuante_2 = float(input("Digite o segundo número: "))
numero_flutuante_3 = float(input("Digite o terceiro número: "))
numero_flutuante_4 = float(input("Digite o quarto número: "))
numero_flutuante_5 = float(input("Digite o quinto número: "))
media_flutuante = (numero_flutuante_1+numero_flutuante_2+numero_flutuante_3+numero_flutuante_4+numero_flutuante_5)/5
print(f"A média dos números digitados é {media_flutuante:.2f}\n\n")

# 8 - Escreva um programa que faça a conversão de um dado valor de metro para quilômetro.

metro = int(input("Insira o valor dos metros: "))
conversao_1 = metro/1000
print(f"Em quilômetros {metro} corresponde a: {conversao_1:.1f} quilômetros\n\n")

# 9 - Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.
# Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.

raio = float(input('Insira o valor o raio: '))
circunferencia = math.pi*(raio**2)
print(f"A circunferência é de {circunferencia:.2f}\n\n")

# 10 - Faça um programa que peça uma temperatura em Fahrenheit (F) e converta esta temperatura para grau Celsius (C), mostrando o resultado da conversão na tela.
# Use a fórmula: C = 5 * ((F-32) / 9).

temp_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
conversao_celsius = 5*((temp_fahrenheit-32)/9)
print(f"A temperatura em Celsius é de {conversao_celsius:.2f} graus\n\n")

# 11 - Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:
# "[número1]x[número2]=[multiplicação]"
# "[número1]/[número2]=[divisão]"

num_5 = float(input('Digite o primeiro número da operação: '))
num_6 = float(input('Digite o segundo número da operação: '))
print(f"{num_5} x {num_6} = {num_5*num_6:.2f}")
print(f"{num_5} / {num_6} = {num_5/num_6:.2f}\n\n")

# 12 - Escreva um programa que receba o nome, sobrenome e idade do usuário e apresente a seguinte mensagem na tela:
# "Seja bem-vindo [nome] [sobrenome]."
# "Você possui [idade] anos de idade."
# No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite 
# remover os espaços antes e depois da string, enquanto que o último permite colocar a string no formato titlecased (capitaliza a string).

nome_1 = str(input('Digite seu nome: '))
sobrenome_1 = str(input('Sobrenome: '))
idade_1 = int(input("Idade: "))
print(f'Seja bem-vindo {nome_1.strip().title()} {sobrenome_1.strip().title()}.')
print(f'Você possui {idade_1} anos de idade.\n\n')

# 13 - Escreva um programa que peça um número do usuário via método input e converta esse número para o formato float.

num_7 = int(input("Digite um número: "))
conversao_2 = float(num_7)
print(f'Tipo do {num_7} é: {type(num_7)}\n\n')

# 14 - Escreva um programa que peça o nome e a idade do usuário. Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem: 
# "Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte mensagem: "Você não pode acessar nosso site [nome].".

nome_2 = str(input('Digite seu nome: '))
idade_2 = int(input("Digite sua idade: "))
if idade_2 >= 18:
    print(f'Seja bem-vindo ao nosso site {nome_2.strip().title()}!\n\n')
else:
    print(f'Você não pode acessar nosso site {nome_2.strip().title()}.\n\n')

# 15 - Elabore um programa para calcular a hipotenusa de um triângulo.
# Dicas:
# Veja o módulo math (math.hypot)
# Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

cateto_oposto = float(input('Digite o Cateto Oposto: '))
cateto_adjacente = float(input('Digite o Cateto Adjacente: '))
print(f'Hipotenusa: {math.hypot(cateto_oposto, cateto_adjacente):.2f}\n\n')

# 16 - Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número. <br>
# Dica: utilize o módulo math do Python, especificamente math.fatorial.

num_8 = int(input('Digite um valor inteiro: '))
print(f'O fatorial de {num_8} é: {math.factorial(num_8)}\n\n')

# 17 - Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.
# Dica: utilize o módulo math.

num_9 = float(input('Digite um valor: '))
print(f'O log na base 10 é: {math.log10(num_9):.2f}')
print(f'O log na base 2 é: {math.log2(num_9):.2f}\n\n')

# 18 - Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

base = float(input('Base: '))
altura = float(input("Altura: "))
area = (base*altura)/2
perimetro = 2*base+2*altura
print(f'Area: {area:.2f} e perímetro: {perimetro:.2f}\n\n')

'''19 - 
Escreva um programa que solicite o nome, o sobrenome e o salário atual de um funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos, com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir o seguinte padrão:
"Olá, [nome] [sobrenome]"
"Seu salário atual é : [salário]"
"Seu salário com 10% de aumento é: [salário]"
"Seu salário com 25% de aumento é: [salário]"
"Seu salário com 30% de aumento é: [salário]"
"Seu salário com 50% de aumento é: [salário]"
No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o primeiro método permite remover os espaços antes e após a string, enquanto que o último permite colocar a string no formato titlecased (capitaliza string).
'''

nome_3 = str(input("Digite seu nome: "))
sobrenome_3 = str(input("Digite seu sobrenome: "))
salario_atual = float(input("Digite o seu salário: "))
print(f"Seu nome completo é {nome_3.strip().title()} {sobrenome_3.strip().title()}\n"
      f"Seu salário atual é: {salario_atual}\n"
      f"Seu salário com 10% de aumento é: {salario_atual*0.1}\n"
      f"Seu salário com 25% de aumento é: {salario_atual*0.25}\n"
      f"Seu salário com 30% de aumento é: {salario_atual*0.3}\n"
      f"Seu salário com 50% de aumento é: {salario_atual*0.5}\n\n"
      )


# 20 - Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

num_10 = int(input('Digite um número inteiro: '))
for i in range(1, 11, 1):
    print(f'{num_10} x {i} = {num_10*i}')
print('\n\n')

# 21 - Faça um programa que solicite um número inteiro e mostre o seu valor absoluto. Dica: use a função built-in abs().

num_11 = int(input("Insira um número inteiro: "))
print(f'O número absoluto de {num_11} é {abs(num_11)}\n\n')

# 22 - Faça um programa que peça uma string ao usuário e mostre na tela a quantidade de caracteres.
# Dica: use a função built-in len() e trate a string com o método strip().

caracteres = str(input("Digite uma palavra ou frase: "))
print(f'A palavra ou frase "{caracteres}" possui {len(caracteres)} caracteres\n\n')

# 23 - Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:
# "O número [número] é [par/ímpar]"

num_12 = int(input('Digite um valor inteiro: '))
if num_12 % 2 == 0:
    print(f'O número: {num_12} é par\n\n')
else:
    print(f'O número: {num_12} é ímpar\n\n')

# 24 - O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.
# IMC<17 - Muito abaixo do peso ideal
# 17<=IMC<18,5 - Abaixo do peso
# 18,5<=IMC<25 - Peso normal
# 25<=IMC<30 - Acima do peso
# 30<=IMC<35 - Obesidade I
# 35<=IMC<40 - Obesidade II (severa)
# IMC>=40 - Obesidade III (mórbida)
# Lembre que: IMC=massa/(altura*altura)
#Fonte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal

nome_4 = str(input('Insira seu nome: '))
idade_4 = int(input('Insira sua idade: '))
peso_4 = float(input('Insira seu peso: '))
altura_4 = float(input('Insira sua altura em metros: '))
imc = peso_4/math.pow(altura_4, 2)

if imc < 17:
    print('Muito abaixo do peso ideal\n\n')
elif imc >= 17 and imc < 18.5:
    print('Abaixo do peso\n\n')
elif 18.5 <= imc < 25: # Lê-se 'Senão, se o IMC for maior ou igual a 18.5 e menor que 25'
    print('Peso normal\n\n')
elif 25 <= imc < 30:
    print('Acima do peso\n\n')
elif 30 <= imc < 35:
    print('Obesidade I\n\n')
elif 35 <= imc < 40:
    print('Obesidade II (severa)\n\n')
elif imc >= 40:
    print('Obesidade III (mórbida)\n\n')

# 25 - Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar dois números iguais.

num_13 = float(input('Digite o primeiro número flutuante: '))
num_14 = float(input('Digite o segundo número flutuante: '))

if num_13 == num_14:
    print('Os números são iguais\n\n')
elif num_13 > num_14:
    print(f'O primeiro número digitado {num_13} é o maior\n\n')
elif num_13 < num_14:
    print(f'O segundo número digitado {num_14} é o maior\n\n')

# 26 - Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

num_15 = float(input('Digite um número: '))

if num_15 == 0:
    print('O número digitado é nulo\n\n')
elif num_15 < 0:
    print('O número é negativo\n\n')
else:
    print('O número é positivo\n\n')

# 27 - Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

numero_00 = float(input('Digite o primeiro número: '))
numero_01 = float(input('Digite o segundo número: '))
numero_02 = float(input('Digite o terceiro número: '))

if numero_00 > numero_01 and numero_00 > numero_02:
    print(f'O maior número digitado foi o primeiro: {numero_00}\n\n')
elif numero_01 > numero_00 and numero_01 > numero_02:
    print(f'O maior número digitado foi o segundo: {numero_01}\n\n')
elif numero_02 > numero_01 and numero_02 > numero_00:
    print(f'O maior número digitado foi o terceiro: {numero_02}\n\n')

# 28 - Escreva um programa que gere um número aleatório entre 1 e 100 e mostre na tela.
# Dica: utilize o módulo random.

numero_03 = random.randint(1, 101)
print(f'O número sorteado foi: {numero_03}\n\n')

# 29 - Elabore um progama para verificar se um ano é bissexto ou não. A condição para ser um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for divisível por 100. 

ano_00 = int(input('Digite o ano: '))
if ano_00 % 400 == 0 or (ano_00 % 4 == 0 and ano_00 % 100 != 0):
    print('O ano é bissexto\n\n')
else:
    print('O ano NÃO é bissexto\n\n')

# 30 - Elabore um programa para calcular o tamanho de uma string.

caracteres_00 = str(input('Insira uma palavra ou frase: '))
print(f'A quantidade de caracteres é de: {len(caracteres_00)}\n\n')

# 31 - Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.

hora_atual_00 = datetime.datetime.now()
print(f'{hora_atual_00.strftime('%d/%m/%Y - %H:%M:%S')}\n\n')

# 32 - Escreva um programa que inverta uma string. Exemplos:
# Hello World!
# Python
# !dlroW olleH
# nohtyP

caracteres_01 = str(input('Digite uma palavra ou frase: '))
print({caracteres_01[::-1]}) #início:fim:passo, implicitamente = ultimo_caracter:primeiro:-1
print(f'{caracteres_01[-1:-1:-1]}\n\n')

# 33 - Escreva um programa para mostrar na tela o calendário do mês de dezembro de 2020.
# Dica: importe o modulo calendar

print(f'{calendar.month(2020, 12)}\n\n')

# 34 - Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

mes = int(input('Insira o mês: '))
ano_00 = int(input('Insira o ano: '))
print(f'{calendar.month(ano_00, mes)}\n\n')

# 35 - Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário. 
# Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida (número entre 1 e 10) mostre na tela uma mensagem personalizada.

categoria = int(input('Digite a categoria: '))
if categoria == 1:
    print(f'O valor do produto é $0.5\n\n')
elif categoria == 2:
    print(f'O valor do produto é $11.3\n\n')
elif categoria == 3:
    print(f'O valor do produto é $17.5\n\n')
elif categoria == 4:
    print(f'O valor do produto é $33.97\n\n')
elif categoria == 5:
    print(f'O valor do produto é $103.47\n\n')
elif categoria == 6:
    print(f'O valor do produto é $44.67\n\n')
elif categoria == 7:
    print(f'O valor do produto é $12.55\n\n')
elif categoria == 8:
    print(f'O valor do produto é $14.87\n\n')
elif categoria == 9:
    print(f'O valor do produto é $98.12\n\n')
elif categoria == 10:
    print(f'O valor do produto é $131.40\n\n')
else:
    print(f'Opção inválida!\n\n')

# 36 - Resolva o exercício anterior para as categorias de 1 a 8. Utilize estruturas aninhadas.

categoria_00 = int(input('Digite a categoria: '))
if categoria_00 == 1:
    print(f'O valor do produto é $0.5\n\n')
else:
    if categoria_00 == 2:
        print(f'O valor do produto é $11.3\n\n')
    else:
        if categoria_00 == 3:
            print(f'O valor do produto é $17.5\n\n')
        else:
            if categoria_00 == 4:
                print(f'O valor do produto é $33.97\n\n')
            else:
                if categoria_00 == 5:
                    print(f'O valor do produto é $103.47\n\n')
                else:
                    if categoria_00 == 6:
                        print(f'O valor do produto é $44.67\n\n')
                    else:
                        if categoria_00 == 7:
                            print(f'O valor do produto é $12.55\n\n')
                        else:
                            if categoria_00 == 8:
                                print(f'O valor do produto é $14.87\n\n')
                            else:
                                if categoria_00 == 9:
                                    print(f'O valor do produto é $98.12\n\n')
                                else:
                                    if categoria_00 == 10:
                                        print(f'O valor do produto é $131.40\n\n')
                                    else:
                                        print(f'Opção inválida!\n\n')

# 37 - Determine se uma letra inserida pelo usuário é uma vogal ou consoante. Armazene as vogais em uma lista e implemente sua solução. Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.

caracter_00 = str(input('Insira uma letra: '))
vogais = ['a', 'e', 'i', 'o', 'u']

if caracter_00 in vogais:
    print('Vogal\n\n')
else:
    print('Consoante\n\n')

# 38 - Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:
#Triângulo equilátero: todos os lados possuem o mesmo tamanho;
#Trângulo escaleno: todos os lados possuem medidas diferentes;
#Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

lado_a = float(input('Digite o tamanho do primeiro lado: '))
lado_b = float(input('Digite o tamanho do segundo lado: '))
lado_c = float(input('Digite o tamanho do terceiro lado: '))

if lado_a == lado_b == lado_c:
    print('Triângulo equilátero\n\n')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Triângulo isósceles\n\n")
else:
    print('Triângulo escaleno\n\n')

# 39 - Implemente uma calculadora simples com as operações aritméticas básicas. O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir dois valores. Caso, o usuário escolha divisão e insira o valor do denominar 0 mostre uma mensagem personalizada. Para os demais casos, mostre na tela o resultado da operação desejada.

operacao = str(input('Insira a operação desejada (*, /, +, -): '))
numero_04 = float(input('Insira o primeiro número da operação: '))
numero_05 = float(input('Insira o segundo número da operação: '))
if operacao == '*':
    print(f'{numero_04} x {numero_05} = {numero_04*numero_05:.1f}\n\n')
elif operacao == '+':
    print(f'{numero_04} + {numero_05} = {numero_04+numero_05:.1f}\n\n')
elif operacao == '-':
    print(f'{numero_04} - {numero_05} = {numero_04-numero_05:.1f}\n\n')
elif operacao == '/':
    if numero_05 == 0:
        print('Divisão indefinida\n\n')
    else:
        print(f'{numero_04} / {numero_05} = {numero_04/numero_05:.1f}\n\n')

# 40 - Escreva um programa que mostre de 1 até 50 na tela.

for i in range(1, 51):
    print(i)
print('\n\n')

# 41 - Escreva um programa que mostre de 50 até 1 na tela.

for j in range(50, 0, -1):
    print(j)
print('\n\n')

# 42 - Escreva um programa que mostre de 150 até 200 na tela.

for a in range(150, 201):
    print(a)
print('\n\n')

# 43 - Escreva um programa de contagem regressiva, ou seja, imprima na tela o seguinte padrão numérico:

for b in range(5, -1, -1):
    print(b)
print('\n\n')

# 44 - Faça um programa que imprima na tela de 1 até um número digitado pelo usuário.

numero_06 = int(input('Digite a condição de parada: '))
for c in range(1, numero_06+1, 1):
    print(c)
print('\n\n')

# 45 - Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.

multiplos_05 = []
contador = 0
d = 1

while contador < 20:
    if d % 5 == 0:
        multiplos_05.append(d)
        contador += 1
    d += 1

for multiplos in multiplos_05:
    print(multiplos)
print('\n\n')

# 46 - Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada (multiplicação) de um número inserido pelo usuário.

numero_07 = int(input("Qual numero deseja ver a tabuada de multiplicação? "))
for e in range(1, 11, 1):
    print(f'{numero_07} x {e} = {numero_07*e}')
print('\n\n')

# 47 - Utilizando estruturas de repetição escreva um programa que mostre os resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.

for f in range(1, 11, 1):
    for g in range(1, 11, 1):
        print(f'{f} x {g} = {f*g}')
print('\n\n')

# 48 - Em um único loop escreva um programa que mostre na tela de 1 a 10 três vezes e ao final mostre a mensagem Fim . No primeiro loop utilize for e nos dois loops seguintes while. O resultado do seu programa deverá ter o seguinte formato:

h = 1
while h < 4:
    for k in range(1, 11):
        print(k)
    h += 1
print('Fim\n\n')

l = 1
for l in range(1,11):
    print(l)
    if l==10:
        while l<=10:
            print(l)
            l+=1
            if l==11:
                m=1
                while m<=10:
                    print(m)
                    m+=1
                    if m==11:
                        print('Fim')
print('\n\n')

# 49 - Escreva um programa que peça ao usuário números entre 0-10. Se o usuário inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

while True:
    numero_08 = int(input('Insira um número entre 0 - 10: '))
    if 0 <= numero_08 <= 10:
        continue
    else:
        print('Fim do programa!\n\n')
        break

# 50 - Em um único loop escreva um programa que mostre na tela de 0-5, cinco vezes e ao final mostre a mensagem Fim . Utilize apenas for em sua implementação. Seu programa deverá gerar um output com o seguinte formato:

for n in range(0, 6):
    print(n)
    if n == 5:
        for o in range(0, 6):
            print(o)
            if o == 5:
                for p in range(0, 6):
                    print(p)
print('Fim!\n\n')
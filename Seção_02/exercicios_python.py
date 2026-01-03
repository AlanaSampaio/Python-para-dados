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

import math
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
print(f"Em quilômetros {metro} crresponde a: {conversao_1} quilômetros\n\n")

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
print(f'Hipotenusa: {math.hypot(cateto_oposto, cateto_adjacente)}\n\n')

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
# 21 - 

# 22 - 

# 23 - 

# 24 - 

# 25 - 

# 26 - 

# 27 - 

# 28 - 

# 29 - 

# 30 - 

# 31 - 

# 32 - 

# 33 - 

# 34 - 

# 35 - 

# 36 - 

# 37 - 

# 38 - 

# 39 - 

# 40 - 
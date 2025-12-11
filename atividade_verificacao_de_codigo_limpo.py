
numero = int(input('Digite o número aqui para descobrir seu valor: '))

if numero > 0:
    print('Seu número é positivo')
elif numero == 0:
    print( '0 é neutro')
else:
    print( 'Seu número é negativo')
    
print('Escreva 3 comprimentos de triângulo e descubra se ele é equilátero, isósceles ou escaleno.')

comp1 = float(input('Comprimento 1: '))
comp2 = float(input('Comprimento 2: '))
comp3 = float(input('Comprimento 3: '))

if comp1 == comp2 == comp3:
    print('Seu triangulo é equilátero')
elif comp1 == comp2 != comp3:
    print('Seu triângulo é isósceles')
else:
    print('Seu triangulo é escaleno')

idade = int(input('Digite sua idade para ver o show: '))

if idade >= 18:
    print('Você é maior de idade, aproveite o show')
else:
    print('Você é menor de idade, não poderar assistir o show')
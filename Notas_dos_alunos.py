senha = 'nn'


for n in range(3):
    senha = input('Insira a senha: ')
    while senha == 'nn':
          print('Insira as notas abaixo.')
          nota1 = float(input('Matématica: '))
          nota2 = float(input('Português: '))
          nota3 = float(input('Geografia: '))
          nota4 = float(input('História: '))
          media = (nota1 + nota2 + nota3 + nota4)/4
          print('A média do aluno é' , round(media , 2))
          senha = input('deseja continuar?: ')

else:
   print('conta bloqueada')

# código da professora
# senha =  '123'
#usuario = 'x'

#for chances in range(3):
    #senha_us =  input('Senha: ')
   ## usuario_ = input('Usuario: ')
   # if senha_us == senha and usuario_ == usuario:
        #cadastra_n = input('deseja registrar as nostas? ')
       # while cadastra_n == 'sim':
           # nome =  input('Nome do aluno: ')
           # n1  =  float(input('Nota 1'))
           # n2  =  float(input('Nota 2'))
           # n3  =  float(input('Nota 3'))
           # media  =  (n1 +  n2 + n3) / 3
           # print('Media do aluno',nome, '-', round(media, 2) )
           # cadastra_n = input('deseja continuar com o registro de  nostas? ')
       # else:
           # print('Deslogar ...')
#else:
#    print('Conta bloqueada!!! ')
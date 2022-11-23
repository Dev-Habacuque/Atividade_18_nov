# Tabela da verdade é um dispositivo para estudo da lógica matemática. Com os símbolos: ~ ^ v -> <-> . Atraves destes símbolos, é possivel criar condições mais especificas e produzir algoritmos mais precisos.

#Variavel é um local onde se armazena determincado valor, podendo ser Bool, Int, Str, List, Dict, Tuple, Complex, Float. O nome da variavel nao pode ser declarado com caracteres especiais (~ ´ `) ou números. Trazendo uma simples analogia cotidiana, a variavel é como uma gaveta, onde sao armazenadas informações mutaveis, que serao usadas posteriormente.

#Tuplas: É um agrupamento de elementos imutáveis que sao declarados atraves de parenteses '()', separados atráves de virgulas ',' e escritos dentro de aspas.

#Dict: É um agrupamento de elementos imutáveis que sao declarados atraves de chaves '{}', separados atráves de virgulas ',' e escritos dentro de aspas.


#List: É um agrupamento de elementos mutáveis que sao declarados atraves de colchetes '[]', separados atráves de virgulas ',' e escritos dentro de aspas.

#Média dos alunos

name_student = input('Nome do aluno: ' )

nota1 = int(input('Primeira nota: '))
nota2 = int(input('segunda nota: '))
nota3 = int(input('terceira nota: '))
nota4 = int(input('quarta nota: '))

nota_participacao = int(input('nota de par: '))

media_final = (nota1 + nota2 + nota3 + nota4)/4

if media_final >= 7:
    print(f'{name_student} obteve média necessária para aprovação!')
elif media_final == 6 and nota_participacao >= 6:
    print(f'{name_student} fica de recuperação.')
else:
    print(f'{name_student} não obteve média necessária para aprovação.')








    

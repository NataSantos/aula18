'''1) Escreva um programa utilizando a Linguagem Python que leia a quantidade de alunos de uma turma e, 
baseado nesse número, leia também: o nome de cada aluno e a sua média final. Calcular e escrever 
quantos alunos dessa turma tiveram média menor que 6.0 e quantos tiveram média maior ou igual a 6.0. 
Use uma função para calcular a média.'''

def calcularMedia(notaUm,notaDois):
  calcMedia=(notaUm+notaDois)/2
  return calcMedia

cont=0
resp='s'
medMenor=0
medMaior=0
while resp=='s':
  nome=input("Digite seu nome: ")
  n1=int(input("Digite a sua primeira nota: "))
  n2=int(input("Digite a sua segunda nota: "))
  media=calcularMedia(n1,n2)
  if media>=6:
    print(f"{nome} sua média foi {media}, portanto você está aprovado")
  else:
    print(f"{nome} sua média foi {media}, portanto você está de recuperação")
  if media>=6:
    medMaior+=1
  else:
    medMenor+=1
  resp=input("Deseja continuar a calcular mais alunos? s --> sim: ")
  cont+=1
print(f"Teve {cont} alunos com média calculada")
print(f"Temos {medMaior} alunos com notas acima da media. E {medMenor} abaixo da média.")
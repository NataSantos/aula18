''' 6) Escreva um programa que leia o número total de alunos em uma turma (quantidade).
Após isto, baseado nesse número, deve ser lida a nota de cada aluno dessa turma. Ao 
término de todas as leituras, escrever:
a) A média geral das notas dos alunos dessa turma
b) Quantos alunos tem nota maior ou igual a 8.0
c) Os nomes dos alunos que tem média maior ou igual a 8 '''

def media(nota1,nota2):
  media=(nota1+nota2)/2
  return media

notaMaior=0
notaMenor=0
mediaGeral=0
contAlunos=0
resp='s'
lista=[]

while resp=='s':
  nome=input("Digite seu nome: ")
  n1=int(input("Digite sua primeira nota: "))
  n2=int(input("Digite sua segunda nota: "))
  med=media(n1,n2)
  mediaGeral+=med
  if med>=8:
    notaMaior+=1
    lista.append (nome)
  contAlunos+=1
  resp=input("Deseja continuar calculando? s --> s: ")
mediaGeral=mediaGeral/contAlunos
print(f"A média geral foi {mediaGeral}")
print(f"O número de alunos com nota igual ou maior que 8 foram: {notaMaior}")
print(f"Os alunos com nota maior ou igual a 8 foram: {lista}")
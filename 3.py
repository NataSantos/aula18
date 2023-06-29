'''3) (Escreva um programa para ler a idade de cada aluno da FACCAT. 
O programa deve ler quantas idades o usuário quiser digitar, ou seja, 
o programa vai encerrar as leituras quando for digitado (lido) o valor 999 para a idade. 
Após encerrar as leituras, o programa deve escrever quantas idades foram lidas (total) e qual a maior idade lida.
'''

cont=0
maiorIdade=0
idade=0

while idade!=999:
  idade=int(input("Digite a sua idade: "))
  if idade!=999:
    if idade>maiorIdade:
      maiorIdade=idade
      cont+=1
print(f"Foram lidas {cont} idades e a maior lida foi {maiorIdade} anos")
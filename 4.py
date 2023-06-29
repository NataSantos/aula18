'''4) Escreva um programa para ler um valor X escolhido pelo usuário. 
O programa deve aceitar somente valores maiores que 1 para X, caso o valor 
informado seja menor ou igual a 1, deverá ser lido um novo valor 
para X informando ao usuário a mensagem: “Valor Inválido!
Digite um novo valor!”. Após lido o valor X, o programa deve escrever 
todos os valores inteiros entre 1 (inclusive) e X (inclusive).'''

cont=1
x=int(input("Digite um  valor: "))
while x<=1:
  x=int(input("Valor inválido, Digite um outro valor: "))
while cont<=x:
    print(cont)
    cont+=1
'''2) A prefeitura de uma cidade quer fazer uma pesquisa entre seus habitantes. 
Faça um programa para ler o salário e o número de filhos de cada habitante da cidade. 
O algoritmo deve calcular a média dos salários da população, média do número de filhos e o maior salário lido. 
Para finalizar a leitura dos dados, o algoritmo deve ler um salário negativo. Após o término das leituras 
e dos cálculos, o algoritmo deve escrever os resultados na tela.'''

totalSalarios=0
totalFilhos=0
maiorSalario=0
contHabitantes=0
salario=0
while salario>=0:
  salario = float(input("Digite o salário do habitante (digite um número negativo para parar!): "))
  if salario>=0:
    filhos = int(input("Digite o número de filhos do habitante: "))
    totalSalarios+=salario
    totalFilhos+=filhos
    contHabitantes+=1
    mediaSalarios=totalSalarios/contHabitantes
    mediaFilhos=totalFilhos/contHabitantes
    if salario>maiorSalario:
      maiorSalario=salario
print(f"A média dos salários foi de {mediaSalarios} reais")
print(f"A média do número de filhos foi de {mediaFilhos:.0f} filhos por habitante")
print(f"O maior salário foi de {maiorSalario} reais")
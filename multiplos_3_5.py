#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#inicializa a variavel de soma total
somaTotal = 0

#Faz um loop verificando quais elementos naturais abaixo de 1000 são multiplos
#de 3 e 5 e adiciona eles na variável somaTotal
for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
      somaTotal += i

#Mostra o resultado final
print(somaTotal)
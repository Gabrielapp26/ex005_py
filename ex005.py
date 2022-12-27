#Desafio 04
#Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milímetros
print("Escreva o número em metros para saber seu valor em centímetros e milímetros")
m = float(input("Valor em metros: "))
c = m*100
mm = c*10
print("O valor {} m é {} cm e {} mm".format(m,c,mm))
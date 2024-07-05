print(" algoritimo que faça a somatoria dos numeros de 0 ate o que o usuario digitou ")
soma=  0
n=int(input("digite o ultimo número : "))
i=0
while i <= n :
    soma=soma+i
    i=i+1
print(f" a soma de todos os numero de 0 até {n} é de {soma}")
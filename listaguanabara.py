lista=[]
for i in range (1,6):
    lista.append(int(input(f" digite o {i} valor : ")))
x=max(lista)
y=min(lista)
a=lista.index(x)
z=lista.index(y)
print(f"voce digitou os valores {lista}")
print(f"o maior valor digitado foi : {x}\n o menor valor digitado foi :{y}\n o  maior valor esta na  posição : {a}\n o menor valor esta na posiçao : {z}")



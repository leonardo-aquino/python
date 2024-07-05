
lista2=[]
cont="S"
while cont=="S":
    lista=[]
    lista.append(input("digite o nome : "))
    rg=((input("digite o rg : ")))
    while len(rg)!=10:
        rg=(input("rg tem no maximo 10 digitos  : "))   
    lista.append(rg)
    sexo=input("digite o sexo M/F : ").upper()
    while sexo not in ["M", "F"]:
        sexo=input("Sexo invalido , digite M ou F : ").upper()
    lista.append(sexo)
    idade=(int(input("digite a idade : ")))
    while idade < 0 or idade >120:
        idade=int(input("idade incoerente, digite uma idade coerente : "))
    lista.append(idade)
    if lista[3] > 30 and lista[2] == "F":
        lista2.append(lista[:4])
    else:
        ()
    cont=input("deseja continuar S/N : ").upper()
    
print(f"aqui esta os dados das mulheres com mais de 30 anos : ")
for p in lista2:
    print(f"nome : {p[0]} rg: {p[1]} sexo: {p[2]} idade {p[3]}")


    
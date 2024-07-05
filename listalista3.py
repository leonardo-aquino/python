lista=[]
lista2=[]
nome="oi"
while nome!="fim":
        nome=input("Digite seu nome : ")
        if nome != "fim":
            lista.append(nome)
            idade=(input("Digite sua idade : "))
            lista.append(idade)
            sexo=input("Digite seu sexo M/F : ")
            if idade > lista[0]:
                lista2.append(lista[:])
            else:
                ()
        else:
            print("prenchimento encerrado")
            for p in lista2:
                print(f"nome : {p[0]} idade : {p[1]} sexo: {p[2]}")
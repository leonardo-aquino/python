nome=str(input("Digite seu nome : "))
cpf=int(input("Digite seu cpf : "))
renda_anual=float(input("Digite sua renda anual : "))
nd=float(input("Digite o número de dependentes : "))
desconto=110*nd 
rl= renda_anual -desconto
if rl <= 800:
    print("insento")
else:
    if  rl >= 801 and rl <= 4000:
        ali=rl*2.5
        print("vc devera pagar : ",ali)
    else:
        if rl >= 4001 and rl <= 9000 :
            ali=rl*5
            print("vc devera pagar : ",ali)
        else:
            if rl > 9000:
                ali=rl*10
                print("vc devera pagar : ",ali)
            else:
                print("erro")
        
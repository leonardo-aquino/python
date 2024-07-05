print("Que comecem os jogos ! \n")
j1=int(input("Jogador 1, escolha o número para ser adivinhado :"))
while j1 < 1 and j1 > 10:
    j1=int(input("Digite um número entre 1 e 10 : "))
print("agora é a vez do jogador 2 tentar adivinhar\n ")
a=0
dc="S"
while dc == "S":
    j2=int(input("Qual numero vc acha que o jogador 1 digitou ? ")) 
    if j2==j1 :
        a=a+1
        print(f"parabens , vc acertou em {a} tentativas.")
        dc=3
    else:
        a=a+1
        dc=input("""errou, precione S para tentar de novo ou  precione N para sair do programa : """).upper()
        if dc != "S":
            print("programa finalizado")
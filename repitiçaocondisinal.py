print("programa que mostra as peças aprovadas e desaprovadas ")
a=0
r=0
for t in range (1,401):
    n=int(input("Digite o numero da peça: "))
    e=input("aprovada =1\nreprovada=2 : ")
                    
    if e == "1":
        r=r+1
    else:
        a=a+1
        print(f"{n} reprovada ")
print(f"""temos {a} peças aprovadas 
            e {r} reprovadas """)
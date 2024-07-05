print("""---------TABUADA------------


""")
n=int(input("digite o primeiro numero : "))
n1=int(input("digite o segundo numero : "))
print("""o que vc quer fazer com esses números ?  

             1 = somar
            2 = subtrair 
            3 = dividir 
            4 = multiplicar """)

v=input(" Digite sua escolha : ")
import os 
os.system("cls")

if v== "1":
    s=n1+n
    print(f" a soma de {n} mais {n1} é igual a {s}")
elif v=="3":
    if n1 == 0:
        print(" esse número nao é divisível")
    else:
        d=n/n1
        print(f" a divisão de {n} dividido por {n1} resulta em {d}")

elif v== "2":
    s=n-n1
    print(f"o resultado da divisão de {n}-{n1} é de {s}")
elif v=="4" :
    m=n*n1
    print(F" o resultado de {n}x{n1} é de {m}")
else:
    print("escolha uma opção correta ")



    





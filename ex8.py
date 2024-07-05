print ("programa que calcula o peso ideal")
s=str(input(" digite seu sexo : "))
a=float(input("digite sua altura : "))
if s== "F" or "M" or s=="f" or "m":
    if a <= 3 and a >= 0:
        if s== "M" or "m":
            ph=(72.7*a)-58
            print(f"seu peso ideal é de : {ph} kg")
        else:
            s== "F" or "f"
            pf=(62.1*a)-44.7
            print("seu peso ideal é de : ",pf)
    else:
        print("erro")
else:
    print("erro")

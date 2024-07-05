print(" algoritimo que determina o grau de obesidade ! ")
p=float(input("digite seu peso em kilos : "))
if p < 300 and p > 0:
    a=float(input(" digite sua altura : "))
    if a < 3.00 and a >0.3:
        m=p/a*a 
        if m < 26:
            print(" voçê é normal")
        else:
            if m >= 30 :
                print("obeso morbido")
            else:
                if m >=26 and a <= 30:
                    print(" vc é obeso")
                else:
                    print("oi")   
    else:
        print("erro")                    
else:
    print("erro")                

















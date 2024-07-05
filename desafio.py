sal_min=float(input("Digite seu slário minimo : "))
if sal_min > 800:
    turno=input("digite seu turno : ")
    if turno=="M" or turno=="V" or turno=="N":
        categoria=input("Digite sua categoria : ")
        if categoria == "O" or categoria == "G":
            ht=float(input("Digite a quantidade de horas trabalhadas : "))
            if ht > 0 :
                if turno== "M" :
                    coef=sal_min*0.1   
                else:
                    if turno=="V":
                        coef=sal_min*0.15     
                    else:
                        coef=sal_min*0.12
                sal_bruto=ht*coef         
                if categoria == "O": 
                    if sal_bruto>=300:
                        imp=sal_bruto*0.05
            
                    else:
                        imp=sal_bruto*0.03
                else:
                    if sal_bruto>=400:
                        imp=sal_bruto*0.06
                    else:
                        imp=sal_bruto*0.04
                if turno=="N" and turno==ht>80:
                        grat=50
                else:
                        grat=30
                        if categoria =="O" or coef <=25: 
                            aux=50
                        else:
                            aux=30
                        sal_liq=sal_bruto-imp+aux
                        if sal_liq <350:
                            print("mal remunerado")




                        else:
                            if sal_liq>600:
                                print("bem remunerado")
                            else:
                                print("normal")
                        print(coef,sal_bruto,imp,grat,aux,sal_liq)
            else:
                print("valor invalido")
           
                
        else:
            print("Categoria inválida")

    else: 
        print("Turno inválido")
else:
    print("Salário mínimo invalido")
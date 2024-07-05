import os 
os.system("cls")
print("Programa que calcula iterativamente para que a populaçao do pais A ultrapasse ou iguale a do pais B\n")
print("País A 98.000.000 habitantes\t ")
print("País B 200.000.000 hzbitantes\n")
pa=98000000
pb=200000000
dc="S"
q=input("Deseja ver em quantos anos o país A ultrapassa o país B ou iguala ? S/N : ").upper()
while q != 'S' and q != 'N' :
    print ("digite apenas s ou n !")
    q=input("Deseja ver em quantos anos o país A ultrapassa o país B ou iguala ? S/N : ").upper()
        
while dc=="S" :   
    if q=="S": 

        import os 
        os.system("cls")       
        a = float(input("Quantos anos você acha? "))
        p1 = 3.5 * a
        pf = pa*p1/100+pa
        p2 = 1.5 * a
        pt = pb*p2/100+pb
        if pf>pt :
            print(f"\npais A passou pais B ")
            print(f"pais a tem {pf} e pais B tem {pt}")
        else:
            if pf==pt:
                print("\nPais A tem a mesma quantidade de habitantes que país B")
                print(f"os dois estao com {pf} habitantes !!")
            else:
                print("pais A ainda nao ultrapassou o país B\n")
                print(f"país A com {pf} habitantes e país B com {pt} habitantes !! \n")
                
            
    else:
        print("programa desligado!")
    dc=input("Deseja continuar ? S/N :").upper()
    import os 
    os.system("cls")
if dc != 's' :
    print("programa finalizado !")

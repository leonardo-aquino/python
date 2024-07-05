import os.path
cod=input(" digite o codigo do funcionário : ")
sal=float(input("digite o salario atual : "))
match cod: 
    case "101":
        novos=sal*1.1
    case  "102":
        novos=sal*.2
    case "103":
        novos=sal*1.3
    case _: 
        novos=sal*1.4
print("seu salario antigo é de ",sal)
print("novo salario é de : ",novos)
di=novos-sal
print(" a difença foi de ",di)

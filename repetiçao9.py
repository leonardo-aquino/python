print("algoritimo que calcula a media de 10 alunos ")
r=0
for i in range (1,11):
    n1=float(input(" digite sua primeira nota : "))
    n2=float(input(" digite sua segunda nota : "))
    media = (n1+n2)/2
    r=r+n1+n2
    print(f" a media do {i} aluno é de : {media}\n")
q=r/20
print(f"a média total é de {q}")
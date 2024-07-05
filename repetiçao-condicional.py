print("programa que faz a média de alunos ! ")
alunos="sim"
while alunos=="sim" or alunos=="SIM":
    n1=float(input("Digite a primeira nota : "))
    n2=float(input("digite2 a segunda nota : "))
    m=(n1+n2)/2
    print(f" esse aluno tem media {m} ")
    alunos=input(" quer ver mais médias ? sim ou nao ? ")
print(" muito obrigado!")


Media=0.0
conc=''
Not1=0 
Not2=0
Not3=0
Not1=float(input("digite o sua nota: "))
Not2=float(input("digite o sua nota: "))
Not3=float(input("digite o sua nota: "))

Media=(Not1+Not2+Not3)/3

if Media>=9:
    conc='Conceito A'
if Media>=7.5 and Media<9:
    conc='Conceito B'
if Media>=6 and Media<7.5:
    conc='Conceito C'     
if Media>4 and Media<6:
    conc='Conceito D'
if Media<4:
    conc='Conceito E'
print(f"Sua média é {Media:.2f}, você atingiu o {conc}")
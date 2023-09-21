b = 0
c = 0
d = 0
print("choisir une operation a faire entre :addition, soustraction, multiplication ou division.")
a = input()
if a == "addition" :
    b = int(input("donner un nombre : "))
    c = int(input("donner un nombre : "))
    d = b + c
    print(f"l'addition de {b} + {c} : {d}")

if a == "soustraction" :
    b = int(input("donner un nombre : "))
    c = int(input("donner un nombre : "))
    d = b - c
    print(f"la soustraction de {b} - {c} : {d}")

if a == "multiplication" :
     b = int(input("donner un nombre : "))
     c = int(input("donner un nombre : "))
     d = b*c
     print(f"la multiplication de {b} * {c} : {d}")
    
if a == "division" :
    b = int(input("donner un nombre : "))
    c = int(input(" donner un nombre : "))
    print(f"la division de {b} / {c} : {d}")


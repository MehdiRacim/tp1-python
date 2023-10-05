def multiply():
    while True:
        try:
            n = int(input("Donnez un nombre entier positif : "))
            if n < 0:
                print("Le nombre doit être positif.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    i = 1
    b = 1
    a = 0
    while i <= n:
        b = b * i 
        a = a + i
        i = i + 1
    print(" + ".join(map(str, range(1, i ))) + " = " + str(a))
    print(str(a) + " = " + " + ".join(map(str, range(1, i))))
    print(" * ".join(map(str, range(1, i))) + " = " + str(b))
    print(str(b) + " = " + " * ".join(map(str, range(1, i))))
    
    recommencer = str(input("Voulez-vous recommencer ? (oui/non)")).lower()
    if recommencer == "oui": 
        multiply()
    elif recommencer == "non":
        from menu import restart

multiply()

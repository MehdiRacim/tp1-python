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
    liste = [1]
    while i <= n:
        b = b * i 
        a = a + i
        i = i + 1
    print(a, b)
    recommencer = str(input("Voulez-vous recommencer ? (oui/non)")).lower()
    if recommencer == "oui": 
        multiply()
    elif recommencer == "non":
        exit()

multiply()

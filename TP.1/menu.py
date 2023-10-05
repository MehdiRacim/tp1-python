def restart():
    print("Choisir un exercise du TP1 à lancer : \n1- exo1\n2- exo2\n3- exo3\n4- exo4\n5- exo5\n6- Quitter")
    answer = input()
    if answer== "1" :
        with open("exo1.py") as f:
            exec(f.read())
    elif answer== "2" :
        from exo2 import multiply
    elif answer== "3" :
        from exo3 import verb
    elif answer== "4" :
        with open("exo4.py") as f:
            exec(f.read())
    elif answer== "5" :
        with open("exo5.py") as f:
            exec(f.read())
    elif answer== "6" : 
        exit()
    else:
        print('Exercise invalide ou réponse inattendu... veuillez recommencer !')
        restart()

        
restart()
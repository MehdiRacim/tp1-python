def restart():
    print("Choisir un exercise du TP1 à lancer : \n- exo1\n- exo2\n- exo3\n- exo4\n- exo5")
    answer = input().lower()
    if answer== "exo1" :
        with open("exo1.py") as f:
            exec(f.read())
    elif answer== "exo2" :
        from exo2 import multiply
    elif answer== "exo3" :
        from exo3 import verb
    elif answer== "exo4" :
        with open("exo4.py") as f:
            exec(f.read())
    elif answer== "exo5" :
        with open("exo5.py") as f:
            exec(f.read())
    else:
        print('Exercise invalide ou réponse inattendu... veuillez recommencer !')
        restart()
        
restart()
def verb():
    a = input("choisir un verbe : ")
    from verbecc import Conjugator
    cg = Conjugator(lang='fr')
    conjugation = cg.conjugate(a)
    present = conjugation['moods']['indicatif']['présent']
    for element in present : 
        print(element)

verb()
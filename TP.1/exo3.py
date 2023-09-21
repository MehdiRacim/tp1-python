
a = input("choisir un verbe :")
from verbecc import Conjugator
cg = Conjugator(lang='fr')
conjugation = cg.conjugate(a)
présent = conjugation['moods']['indicatif']['présent']
for élément in présent : 
    print(élément)

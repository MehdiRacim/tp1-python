from verbecc import Conjugator
cg = Conjugator(lang='fr')
conjugation = cg.conjugate('manger')
présent = conjugation['moods']['indicatif']['présent']
for élément in présent : 
    print(élément)

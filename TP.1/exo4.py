yen = 156.79
dollar = 1.42408
livre =  0.795447

livres = 0
yens = 0
dollars = 0

print("En quelle devise voulez vous convertir vos euros ?" )
print("\n- Yen", "\n- Dollars", "\n- Livres")
choix = input().lower()
if choix == "yen": 
	print("Entrez le nombre d'euros que vous voulez convertir en yen:")
	euros = int(input())
	yens = euros * yen
	print (euros, "euros vallent", yens, "yens")
	from menu import restart
elif choix == "dollars": 
	print ("Entrez le nombre d'euros que vous voulez convertir en dollars:")
	euros1 = int(input())
	dollars = euros1 * dollar
	print (euros1, "euros vallent", dollars, "dollars")
	from menu import restart
elif choix == "livres":
	print("Entrez le nombre d'euros que vous voulez convertir en livres:")
	euros2 = int(input())
	livres = euros2 * livre
	print (euros2, "euro vallent", livres, "livres")
	from menu import restart
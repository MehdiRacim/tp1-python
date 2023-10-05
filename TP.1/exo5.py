palindrome = str(input("donner une chaine de caractere : "))
if palindrome == palindrome[::-1]:
    print("cette chaine de caractere est un palindrome")
    from menu import restart
else : 
    print("cette chaaine de caractere n'est pas un palindrome")
    from menu import restart
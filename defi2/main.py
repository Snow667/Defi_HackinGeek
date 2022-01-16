"""niveau 1: 
Compté le nombre d'occurrences d'une lettre choisie dans un mot.
ex : lettre choisie o, mot bonjour o apparait 2 fois dans bonjour
niveau 2:
compté le nombre d'occurrences de chaque lettre d'une phrase puis afficher le résultat dans l'ordre décroissant ex : phrase : "bonjour moi" résultat : o -> 3 b,n,j,u,r,m,i -> 1
niveau 3 :
faire un programme permettant de réduire une chaine par rapport au nombre d'occurence de ces lettres ex parce que c'est pas clair:
chaine : aaaacccttttt résultat 4a3c5t
Bonus : votre programme peu faire le niveau 3 dans les 2 sens ex : 
chaine 5d3e7f -> dddddeeefffffff
Bonne chance !!!!"""


mot = input("Ecrivez n'importe quel mot : ")
liste = list(mot.strip())
nb_carac = []

for i in liste:
    if i in liste:
        a = liste.count(i)
        nb_carac.append(a)
    
phrase = []
for i in range(0, len(liste)):
    if (f" {liste[i]}{nb_carac[i]}") not in phrase:
        phrase.append(f" {liste[i]}{nb_carac[i]}")
    
    
print("".join(phrase))

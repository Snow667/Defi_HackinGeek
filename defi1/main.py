"""Votre programme doit prendre 5 entrée différente et donné la plus grande
(Utilisation de variable de if et de while/for)
Niveau 2 :
votre programme prends 5 entrée, il affiche celle qui sont supérieures à une 6e
(If while/for et un peu de tri)
Niveau 3:
Votre programme prend 5 entrée et affiche la plus proche d'une 6e (prévoir le cas d'une égalité) 
(Du tri plus poussé)

Dans toute défi on utilisera uniquement des nombre entier

Comme d'habitude, le but sera de réaliser le plus rapidement chaque niveau, il y aura un gagnant (qui aura le rôle @winner défi) par niveau.
Pour les question vous pouvez les poser ici ou me contacter en privé, pour les réponses envoyées moi votre code en privé.
Le langage de programmation n'est pas imposé"""

valeur_choisi = []
for i in range(0, 5):
    a = input("Choisi un nombre au hasart ? ")
    int_a = int(a)
    valeur_choisi.append(int_a)

FINAL = input("Choisi le nombre que tu veux et ainsi sortira le nombre le plus proche ? ")
final_int = int(FINAL)
print(min(valeur_choisi, key=lambda x:abs(x-final_int)))

from ntpath import join


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
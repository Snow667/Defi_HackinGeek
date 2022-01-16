# Liste -> 5 INT
# PLus proche de Input −> print

valeur_choisi = []
for i in range(0, 5):
    a = input("Choisi un nombre au hasart ? ")
    int_a = int(a)
    valeur_choisi.append(int_a)

FINAL = input("Choisi le nombre que tu veux et ainsi sortira le nombre le plus proche ? ")
final_int = int(FINAL)
print(min(valeur_choisi, key=lambda x:abs(x-final_int)))

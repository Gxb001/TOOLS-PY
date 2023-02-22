# def main():
#     # recolter une premiere note 
#     note1 = int(input("Entrer la première note"))
#     # recolter une deuxieme note
#     note2 = int(input("Entrer la deuxième note"))
#     #recolter la derniere note
#     note3 = int(input("Entrer la dernière note"))
#     #calculer la moyenne
#     result = (note1 + note2 + note3) / 3
#     #afficher le resultat
#     print("La moyenne est de" + str(result))

nbr_notes = int(input("Entrer le nombre de notes :"))
moyenne = 0
for e in range (nbr_notes): 
    note = float(input("Entrez votre note : "))
    moyenne += note
print("Votre moyenne est de :", moyenne / nbr_notes )

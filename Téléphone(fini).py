"""Ce code sert à représenter comment fonctionne le clavier numérique des anciens téléphones portables
A l'aide de listes et de boucles, j'ai réussi à recréer cette fonctionnalité pour la touche 2 et 3.
Tout d'abord les commandes pour se servir de ce script apres l'avoir exécuté bien evidemment sont : 2 ou 3 pour choisir sa liste, ensuite + et - pour se déplacer dans la liste séléctionnée au-paravant (une fois au bout de la liste pour revenir au debut il faut faire deux fois + et deux fois - au début pour aller à la fin), la commande "valider" sert a valider le caractère  chosi. Une fois cela fait il faut re-choisir sa liste et ré-utiliser les commandes précendentes pour continuer à écrire son message. Pour terminer son message et l'ecrire il faut faire "terminer", si votre message n'est pas celui souhaité vous pouvez faire "reset" pour le recommencer, voila à peu pres toutes les explications de ce script."""


liste_touche2 = ["a", 'b', 'c', '2', 'à', 'â', 'ä', 'ç', 'æ'] #liste de la touche 2 
liste_touche3 = ['d', 'e', 'f', '3', 'é', 'è', 'ë'] #liste de la touche 3 
M = "" #liste message en composition

print("Listes disponibles :\n")
print("Liste 2 :", liste_touche2, "\nListe 3 :", liste_touche3)
# Cette variable sert à donner l'information au code qu'on a terminé d'écrire le message.
terminer = 0
while terminer == 0:
    touche = input(
        "\nQuelle touche voulez vous utiliser entre  2 ou 3 ? (Pour confirmer  votre message, écrivez terminer et pour le supprimer faites reset) :") #premier input pour demander à l'utilisateur quelle liste désire-t-il ?
    if touche == "2":
        print("Caractères de la touche 2", liste_touche2)
        #si le premier input = 2 alors il séléctionne la liste 2
        L = liste_touche2[0]
        b = 0
        valider = 0
        print("\nCaractère Départ/Actuel :", L) #montre le caractère potentiellement séléctionné
        while valider == 0:
            deplacement = input(
                "\nPour aller à gauche dans la liste écrivez - et pour aller à droite écrivez + (Pour prendre le caractère actuel, écrivez valider) :")#maintenant dans la liste séléctionnée il demande ou voulez vous vous déplacer dans cette-ci ? (2)
            if deplacement == "+":
                if b == 8:  #déplacement vers la droite dans la liste
                    b = -1
                else:
                    b += 1
                    L = liste_touche2[b]
                    print("\nCaractère Actuel :", L) #montre le caractère potentiellement séléctionné
            elif deplacement == "-":  #déplacement vers la gauche dans la liste
                if b == 0:
                    b = 9
                else:
                    b -= 1
                    L = liste_touche2[b]
                    print("\nCaractère Actuel :", L)#montre le caractère potentiellement séléctionné
            elif deplacement == "valider":#valide le caractère actuel et l'ajoute dans le message acatuellement en composition
                M += L
                print("\nCaractères composant du message :", M)
                valider += 1 #montre le message composé actuellement.
            elif deplacement != "+" or "-" or "valider":
                print("\nErreur veuillez choisir entre +, - ou valider")#erreur, si la commande entrée n'existe pas.

    elif touche == "3":
        print("Caractères de la touche 3", liste_touche3)
        L1 = liste_touche3[0]#si le premier input= 3 alors séléctione la liste 3
        b1 = 0
        valider = 0
        print("\nCaractère Départ/Actuel :", L1)#montre le caractère potentiellement séléctionné
        while valider == 0:
            deplacement = input(
                "\nPour aller à gauche dans la liste écrivez - et pour aller à droite écrivez + (Pour prendre le caractère actuel, écrivez valider) :")#pareil que pour la 1ere touche, il demande ou voulez vous allez dans la liste séléctionnée(3)
            if deplacement == "+": #déplacement vers la droite dans la liste
                if b1 == 6:
                    b1 = -1
                else:
                    b1 += 1
                    L1 = liste_touche3[b1]
                    print("\nCaractère Actuel :", L1)#montre le caractere potentiellement séléctionné
            elif deplacement == "-": #déplacement vers la gauche dans la liste
                if b1 == 0:
                    b1 = 7
                else:
                    b1 -= 1
                    L1 = liste_touche3[b1]
                    print("\nCaractère Actuel :", L1) #montre le caractère potentiellement séléctionné
            elif deplacement == "valider":
                M += L1 #valide le caractère actuel et l'ajoute dans le message acatuellement en composition
                print("\nCaractères composant du message :", M)#montre le message ecrit actuellement
                valider += 1
            elif deplacement != "+" or "-" or "valider":
                print("\nErreur veuillez choisir entre +, - ou valider")
                #affiche ce messgae si aucune des commandes existantes sont utilisées.
    elif touche == "reset":
        M = "" # vide la liste message
        print("\nLa liste contenant le message vient d'être supprimée !")
    elif touche == "terminer": #renvoie le message finale de la liste de composition de message
        terminer += 1
        print("\nVoici votre message :\n\n",M)#ajoute ce texte à coté du message
    else:
        print("\nErreur, veuillez écrire 2, 3, terminer ou reset")#meme erreur qu'avant, écris ce message si la commande entrée est inexistante
import random
from math import*
#Configurer la Roue de Roulette
list = [i for i in range (0,37)]
#Gérer le Budget du Joueur

Budget_Initial=int(input("votre budget : "))
print("votre Budget est : ",Budget_Initial )
print("votre objectif est de maximiser votre gains avant de décider d'arreter !!!!")

while Budget_Initial>0:
    # Accepter les Paris
    num = int(input("Choisir un numéro entre 0 et 36 sur lequel vous souhaitez parier: "))
    while num not in list:
        print("Le numéro doit être entre 0 et 36.")
        num = int(input("Choisir un numéro entre 0 et 36 sur lequel vous souhaitez parier: "))

    argent = int(input("Combien d'argent souhaite vous miser sur ce numéro "))
    # Check the condition
    if argent <= Budget_Initial:
        print("Le budget est suffisant!")
    else:
        argent = int(input("encore une fois Combien d'argent souhaite vous miser sur ce numéro  il doit etre moins ou egale a vous budget"))

    # FaireTouener la Roue de Roulette
    numé = random.choice(list)  # random.choice(list)
    print("le numéro tiré c'est : ", numé)
    # Logique de Gain et Perte
    if numé == num:
        Budget_Initial = argent * 35
        print("a winnn !! ,votre nouveau budget c'est : ", Budget_Initial)
    else:
        Budget_Initial = Budget_Initial - argent
        print("youu lose !! , votre nouveau budget c'est : ", Budget_Initial)
    # Terminer le jeu
    reponse=input("Est ce que vous souhaite continuer a jouer entrer oui ou non ")
    if reponse =='oui':
        continue
    if reponse=='non':
        print(f"Merci d’avoir joué ! Votre budget final est {Budget_Initial} . À bientôt !")
        break
else:
    print("vous n'avais plus d'argent pour continuer")
print("nice game À bientôt !")

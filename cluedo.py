from tabulate import tabulate
import random
import os 

os.system('clear')

personnages = ['esteban', 'maman', 'papa', 'barbara', 'lou', 'raphael']
armes = ['pistolet', 'corde', 'poison', 'chandelier', 'banane', 'coussin']
lieux = ['cuisine', 'salon', 'chambre', 'toilette', 'couloir', 'terrasse']

cartes = [['esteban', 'pistolet','cuisine'], ['maman','corde','salon'],['papa','poison','chambre'],['barbara','chandelier','toilette'],['lou','banane','couloir'],['raphael','coussin','terrasse']]

colonnes = ['personnages', 'armes', 'lieux']

meurtre = []
meurtre.append(personnages[random.randint(0,5)])
meurtre.append(armes[random.randint(0,5)])
meurtre.append(lieux[random.randint(0,5)])

perso_innocents = [perso for perso in personnages if perso not in meurtre]
armes_innocents = [arme for arme in armes if arme not in meurtre]
lieux_innocents = [lieu for lieu in lieux if lieu not in meurtre]

#print(meurtre) # A supprimer pour jouer

running = True 
chances = 10

print('*'*10)

while running == True:
    print('-'*35)
    print(tabulate(cartes, headers=colonnes))
    print('-'*35)
    print()
    perso = input("Quelle personne : ")
    arme = input("Quelle arme : ")
    lieu = input("Quel lieu : ")

    hypothese = [perso, arme, lieu]

    if hypothese == meurtre:
        print("VOUS AVEZ GAGNE !!!")
        print('*'*10)
        running = False
        break

    contre = [] # Liste qui vas contenir toutes les cartes qui contre une hypothèse

    if hypothese[0] not in meurtre: # SI la personne n'est pas la bonne:
        # contre_perso = perso_innocents[random.randint(0,4)]
        contre.append(hypothese[0])
    
    if hypothese[1] not in meurtre: # SI l'arme n'est pas la bonne:
        # contre_arme = armes_innocents[random.randint(0,4)]
        contre.append(hypothese[1])
    
    if hypothese[2] not in meurtre: # SI le lieu n'est pas le bon:
        # contre_lieu = lieux_innocents[random.randint(0,4)]
        contre.append(hypothese[2])

    random_contre = contre[random.randint(0,len(contre)-1)] # on choisi un contre exemple aléatoire parmis ceux existants

    num_sous_liste = 0
    num_sous_liste_true = 0
    for sous_liste in cartes:
        num_sous_liste += 1
        if random_contre in sous_liste:
            num_sous_liste_true = num_sous_liste - 1
            for pos, elem in enumerate(sous_liste):
                if elem == random_contre:
                    position = pos
    
    cartes[num_sous_liste_true][position] = ' '

    print('\n----------')
    print(f">>> Votre hypothèse est fausse ! \n>>> Voici un contre : {random_contre}.\n")


#!/usr/bin/env python
# -*- coding: utf-8 -*-



from upemtk import *
from donnees import *
from grille import *
from personnage import *
from ennemis import *
from niveaualea import *
from level import *

from time import sleep,time
from random import randint




def jeu(largeur,hauteur,aleatoire):
    
    
    nomNiveau = 'n1'
    """
    Fonction qui met en relation les différentes fonctions nécessaires au bon fonctionnement du jeu
    """
    niveau = ''
    
    while True: #boucle principale du jeu
        
        if aleatoire == True:
            
            
            niveau = niveau_alea(a,b,pTerre,pDiamant,pRocher,pMur,taille_case,largeur,hauteur)
        else:
            niveau = lectureNiveau(nomNiveau)
            
        
            
        
        grille = construction_grille(niveau) # construit la liste de la grille avec la chaine du niveau en question
        
        if aleatoire != True:
            
            for ligne in range(len(grille)): # Vérifie que la grille est bien écrite
            
                if ligne != 0:
                    assert len(grille[ligne]) == len(grille[ligne-1]), 'Il manque des cases dans le niveau'
        
        
        perso_x,perso_y = compteurEtPosition(grille,'R')
        posSortie = compteurEtPosition(grille,'E')

        
        nbDiamant = 0
        parcoursRoche = 0
        decompte = 20
        tempseboulement = 0
        vardebug = 1
        debug = False
        joueurEcrase=False
        timeout = False
        direction =''
        start = time()



        while True:# boucle du niveau
            
            countDown = int(decompte - (time() - start)) # on récupère le temps restant en soustrayant le temps max associé au niveau, moins le temps qui est passé.

            if direction == '' and debug == True: # si mode debug on choisi un déplacement alétoirement
                direction = posibiliteDirection[randint(0,3)]

            # récupère l'évenement de la nouvelle direction
            direction, vardebug, debug = mise_a_jour_direction(direction,vardebug,debug)
            
            # On vérifie s'il est possible de se déplacer. Oui: efface la case du perso
            verifDeplace,verifDeplaceRocher = effaceDeplacementPerso(direction,grille,perso_x,perso_y)
                
            if tempseboulement % 20 ==0:
                tempseboulement = 0
                
                if verifDeplace == True:
                    scrolling(grille,direction)

                
                # on realise un déplacement de la grille en fonction de celui du joueur (caméra)
                gagne = persoSortie(perso_x,perso_y,posSortie,nbDiamant,diamantsRequis,grille)

                # Réaliser le déplacement. Affiche le perso sur la case en rapport avec la direction
                perso_x, perso_y, nbDiamant, direction,decompte = deplacementPerso(direction, grille, perso_x,perso_y, verifDeplace,verifDeplaceRocher, nbDiamant,decompte)

                # realise un eboulement des rochers qui le doivent, et vérifie si cela écrase le joueur
                joueurEcrase = eboulement(grille)
        
                
                if countDown == 0:
                    timeout = True

                if joueurEcrase == True or gagne == True or timeout == True:
                    
                    if timeout == True:
                        pass
                    else:
                        efface_tout()
                        rectangle(0, 0, largeur, hauteur, couleur='black', remplissage='black', epaisseur=1, tag='')
                        affichage_grille(grille, largeur, hauteur)
                        mise_a_jour()

                    sleep(1)
                    reset = finPartie(largeur,hauteur,joueurEcrase,gagne,timeout) # écran de fin de partie / attend une potentielle demande de reset ou fermeture du jeu

                    if reset == True:
                        break
                    else:
                        exit()


                ## -- -- mise à jour de l'affichage
                efface_tout()
                    
                rectangle(0, 0, largeur, hauteur,couleur='black', remplissage='black', epaisseur=1, tag='')
                affichage_grille(grille,largeur,hauteur)
                
                barreInfo(diamantsRequis,nbDiamant,countDown,coefscore)
               
                mise_a_jour()
            tempseboulement +=1 
    

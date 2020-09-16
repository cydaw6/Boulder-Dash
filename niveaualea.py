#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from grille import compteurEtPosition
from donnees import taille_case,largeur,hauteur
from time import time


def niveau_alea(a,b,pTerre,pDiamant,pMur,pRocher,taille_case,larg,h):

    while True:
        start = 0
        blocs = [pTerre, pDiamant, pRocher, pMur]  # liste des pourcentage des blocs
        largeur = a - 2
        hauteur = b - 2
        nbBlocs = (largeur + 1) * hauteur  # nombre de blocs de la map, avec soustraction du nombre de blocs de bordures
        rx, ry = randint(1, int((larg / 4) / taille_case)), randint(1, int(h / taille_case))


        done = False
        start = time()
        decompte = 2
        
        while done == False:
            

            element = ''
            niveau = [] # chaine finale du niveau
            niv = '' # chaine des blocs à l'intérieur des blocs de bordure
            l=[] # donnera une liste de tuples (le nombre qu'il doit y en avoir, type de bloc) dans le niveau selon la taille du niveau et le pourcentage choisi


            for i in range(4):

                if i == 0:
                    element = 'G'

                elif i == 1:
                    element = 'D'
                
                elif i == 2:
                    element = 'B'

                elif i == 3:
                    element = 'T'
                
                nbTypeElement= nbBlocs * blocs[i] / 100
                
                if nbTypeElement%1 > 0.50:
                    nbTypeElement +=1
                if element == 'G':
                    nbTypeElement -= 2
                    
                nbTypeElement = int(nbTypeElement)

                l.append((str(nbTypeElement),element))

            pa = pTerre + pRocher
            pb = pa + pDiamant
            pc = pb + pMur
            
            i = 0
            while i != nbBlocs: # tant que toutes les cases du niveau ne sont pas remplis
                x = randint(1,100) 
                
                if x <= pTerre:
                    element = 0
                
                elif x > pTerre and x <= pa:
                    element = 1
                    
                elif x > pa and x <= pb:
                    element = 2
                    
                elif x > pb and x <= pc:
                    element = 3

                nbObjet,objet = l[element]
                nbObjet = int(nbObjet)
                
                if nbObjet != 0: # si le nombre de blocs restants à placer du type actuel de bloc n'est pas nul
                    
                    niv += objet # on ajoute le caractère du bloc à la chaîne du niveau
                    nbObjet -= 1 # on diminue le nombre de bloc à placer de ce type de bloc
                    
                    l[element] = (str(nbObjet),objet)
                    
                    i+=1

                t = nbBlocs - i

                if t == 2:
                    niv = list(niv)
                    nb = randint(3,largeur*hauteur-3)
                    niv.insert(nb,'E')
                    i+=1
                elif t == 1:
                    
                    nb = ((ry-1)*a)+rx

                    niv.insert(nb,'R')
                    i+=1

            ligne = ''
            i=0

            for y in range(hauteur+1):
                if y == 0 or y == hauteur:
                    c = 'W'*(largeur+1)+'\n'
                    niveau.append(c)
                    
                if y == hauteur:
                    break

                for x in range(largeur+1):

                    if x == 0:
                        ligne += 'W'
                    elif x == largeur:
                        ligne += 'W\n'
                        
                    elif i < nbBlocs:

                        ligne += niv[i]
                    
                    i+=1
                niveau.append(ligne)

                ligne = ''
                
            niveau = ''.join(niveau)

            if 'E' in niveau and 'R' in niveau:
                return niveau

            if int((decompte - (time()-start))) == 0:
                break
            
            
        
    



if __name__ == '__main__':


    # a,b : largeur/hauteur du niveau

    a,b = 40,10


    # pourcentages pour chaque type de blocs dans le niveau 

    pTerre = 75
    pDiamant = 3
    pRocher = 15
    pMur = 7

    print(niveau_alea(a,b,pTerre,pDiamant,pRocher,pMur,taille_case,largeur,hauteur))

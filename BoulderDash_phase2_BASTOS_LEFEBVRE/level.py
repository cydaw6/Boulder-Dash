#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os



def lectureNiveau(nomniveau):

    niveau = ''

    niv = os.path.join(os.getcwd(),"niveaux",nomniveau+'.txt')
                
    with open(niv) as fichier :
        fichier.readline()
        for lines in fichier:
            for lettre in lines:
                niveau = niveau + lettre
    
    return niveau


# -*- coding: utf-8 -*-

from random import *


def alea(x):
    """Renvoie True avec une probabilité de x%"""
    if random() * 100 < x:
        return True
    else:
        return False


def sauvegarder_partie():
    """Sauvegarde les paramètres et la progression dans le jeu dans un pickler
    ( dossier en binaire )"""
    pass


def charger_partie():
    """"""
    pass


def charger_parametres():
    """Extrait les paramètres d'un fichier texte dedié"""
    pass

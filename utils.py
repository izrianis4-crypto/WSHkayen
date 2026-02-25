"""
Module StudentStats.
"""


def calcul_moyenne(liste_notes):
    """
    Calcule la moyenne d'une liste de notes.

    Args:
        liste_notes (list): Liste des notes.

    Returns:
        float: Moyenne des notes.
    """
    if len(liste_notes) == 0:
        return 0

    somme = 0

    for note in liste_notes:
        somme = somme + note

    moyenne = somme / len(liste_notes)

    return moyenne
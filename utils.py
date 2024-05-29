import logging
from API import google_drive_api


# Configuration des logs
logging.basicConfig(
    level=logging.DEBUG,  # Niveau de journalisation (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format des messages de log
    filename="app.log",  # Nom du fichier de log
    filemode="w",  # Mode d'écriture du fichier ('w' pour écrire à chaque fois)
)


files_names = []
total_progress = 0


def get_valeur_progression(actuelle, total):
    """renvoie le pourcentage de la progression actuelle

    Args:
        actuelle (int): progression actuelle
        total (int): valeur max de la progression

    Returns:
        int: entier du pourcentage de la progression
    """
    return round(actuelle / total * 100)


def etats_true(sous_liste):
    for element in sous_liste:
        if not element:
            return False
    return True


def etats_false(sous_liste):
    for element in sous_liste:
        if element:
            return False
    return True


def etats_liste(liste_de_listes):
    if etats_true(liste_de_listes):
        return 1
    if etats_false(liste_de_listes):
        return -1
    return 0


def import_names_files():
    global files_names
    global total_progress
    TEXT_SNS_FOLDER_DRIVE = "1uubK1tqm4K5RP9KiezJfoPZ86Az5eAiw"
    list_sheet_files = google_drive_api.list_files_in_folder(TEXT_SNS_FOLDER_DRIVE)
    for sublist in list_sheet_files:
        files_names.append(sublist[0])
    files_names.sort()
    total_progress = len(files_names)

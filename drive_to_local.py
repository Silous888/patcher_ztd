# from API import google_sheet_api
# from API import google_drive_api

import json
import utils
import googleSheetAPI

TEXT_SNS_FOLDER_DRIVE = "1uubK1tqm4K5RP9KiezJfoPZ86Az5eAiw"

EN_JSON_DRIVE = "1n1U5DqSNdFNG42_PskbLrGtb1QsfL3hmRqBjEfmAucc"

EXPORT_FOLDER_TEST = "F:\\Documents\\traduction_DreamTeam\\428\\export"

OBJECT_FOLDER_TEST = "F:\\Documents\\traduction_DreamTeam\\428\\object"

EXPORT_FOLDER = ".\\export"

OBJECT_FOLDER = ".\\object"

TEST = False

if TEST:
    EXPORT_FOLDER = EXPORT_FOLDER_TEST
    OBJECT_FOLDER = OBJECT_FOLDER_TEST


SCRIPT_FOLDER = EXPORT_FOLDER + "\\shibuya_desktop_data_core_patch.wad\\script\\en\\to.sns"

EN_JSON_FOLDER = EXPORT_FOLDER + "\\shibuya_desktop_data_core.wad\\localization\\game"

progression_actuelle = 0


def replace_every_files_text(instance_worker):
    for i in range(len(utils.files_names)):
        name = utils.files_names[i]
        if instance_worker.liste_choix_fichiers[i]:
            instance_worker.set_text_progress(name)
            # google_sheet_api.open_spreadsheet(google_drive_api.get_id_by_name(name))
            print(name)
            # list_value_sheet = google_sheet_api.get_sheet(0)
            list_value_sheet = googleSheetAPI.get_matrice_sheet(name)
            replace_text_in_xml_txt(list_value_sheet, name)
            incrementer_progression(instance_worker)


def replace_text_in_xml_txt(list_value_sheet, name_file):
    filepath = SCRIPT_FOLDER + "\\" + name_file
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

        it = 1
        for item in data:
            if len(list_value_sheet[it]) < 3:
                continue
            if len(list_value_sheet[it][2]) != 0:
                if list_value_sheet[it][2] == '¤':
                    item['val'] = ""
                else:
                    item['val'] = replace_strange_char(list_value_sheet[it][2])
            else:
                item['val'] = item['key']
            it += 1

        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def replace_en_json(instance_worker):
    file_name = "en.json"
    filepath = EN_JSON_FOLDER + "\\" + file_name
    instance_worker.set_text_progress(file_name)
    list_value_sheet = googleSheetAPI.get_matrice_sheet(file_name)

    with open(filepath, 'r', encoding='utf-8', ) as f:
        data = json.load(f)
        for i in range(len(list_value_sheet)):
            if len(list_value_sheet[i]) <= 3:
                continue
            if list_value_sheet[i][0] in data:
                data[list_value_sheet[i][0]] = convertir_double_slash_en_simple(list_value_sheet[i][3])
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def convertir_double_slash_en_simple(path):
    """converti les slash en double slash dans un chaine de caractère,
    pour éviter les problèmes

    Args:
        path (str): path windows

    Returns:
        str: path windows avec des double slash à la place des simples
    """
    path = path.replace("\\'", "\'")
    return path.replace('\\n', '\n')


def replace_strange_char(text):
    list_strange_char = ["001C", "001D", "0017", "0014", "0015", "0019", "001A",
                         "001B", "0018", "0016", "00A0", "001E", "001F"]

    for char in list_strange_char:
        text = text.replace(char, f"\\u{char}\"")
    return text


def incrementer_progression(instance_worker, valeur=1):
    """incrémente la barre de progression

    Args:
        instance_worker (worker): sert à accéder à la barre de progression
        valeur (int, optional): de combien on incrémente. Defaults to 1.
    """
    global progression_actuelle
    progression_actuelle = progression_actuelle + valeur
    instance_worker.set_value_progressbar(
        utils.get_valeur_progression(progression_actuelle, utils.total_progress)
    )


def update_texte_progression(instance_worker, message):
    """change le texte de progression

    Args:
        instance_worker (worker): sert à accéder à au label du texte
        message (str): texte à afficher
    """
    instance_worker.set_text_progress(message)

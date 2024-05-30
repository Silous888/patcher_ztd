# from API import google_sheet_api
# from API import google_drive_api

import json
import polib
import utils
import googleSheetAPI

TEXT_XML_FOLDER_DRIVE: str = "1f-s3R9eeV8mSqRHcJfyJcehyIsm1MSpk"

US_PO_DRIVE: str = "11P4qp0Lu9be63yWvPZtjQ9ZW7YuqW6sqVR3o7aNgrBM"

progression_actuelle: int = 0

ZTD_PATCH_DATA_FOLDER: str = ".\\ZTD_patch_data\\mod_dlg\\"


def replace_every_files_text(instance_worker):
    """for each file, replace text in, if selected"""
    for i, name in range(utils.files_names):
        if instance_worker.liste_choix_fichiers[i]:
            instance_worker.set_text_progress(name)
            print("insertion texte fichier " + name)
            list_value_sheet = googleSheetAPI.get_matrice_sheet(name)
            replace_text_in_xml(list_value_sheet, name)
            incrementer_progression(instance_worker)


def replace_text_in_xml(list_value_sheet: list[list[str]], name_file: str):
    """main part to change text in an xml file

    Args:
        list_value_sheet (list[list[str]]): matrix of string with every value in the sheet
        name_file (str): name of the file
    """
    filepath = "?????????????" + "\\" + name_file
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


def replace_us_po(instance_worker):
    """replace values of us.po with values in the google sheet
    """
    file_name = "us.po"
    filepath = ZTD_PATCH_DATA_FOLDER + file_name
    instance_worker.set_text_progress(file_name)
    list_value_sheet = googleSheetAPI.get_matrice_sheet(US_PO_DRIVE)
    print(list_value_sheet)
    po = polib.pofile(filepath)
    for i, entry in enumerate(po):
        print(i)
        print(list_value_sheet[i][2])
        translated_line = list_value_sheet[i][2]
        if len(translated_line) == 0:
            continue
        translated_line = convert_double_slash_to_slash_n(translated_line)

        entry.msgstr = translated_line
        po.save()


def convert_double_slash_to_slash_n(text: str):
    """convert double slash to slash n"""
    return text.replace('\\\\', '\n')


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

"""main of the program"""
import os
from fileFolderUI import FileFolderUI
import utils
import drive_to_local
import ze_ztd_tool
from API import steam_game_api

# pyinstaller --onefile --name ZTD_Patch_Automatique --icon=./ressource/DreamteamLogo.ico main.py

utils.import_names_files()


def process(instance_worker):
    """main function of the program
    """
    gamepath_directory: str = steam_game_api.find_game_path("Zero Escape")

    org_pak_folder: str = ".\\ZTD_patch_data\\org_pak\\"
    org_pak: str = "00000000.cfsi"

    if not os.path.exists(os.path.join(org_pak_folder, org_pak)):
        drive_to_local.update_texte_progression(instance_worker, "copie fichier d'origine du jeu...")
        steam_game_api.copy_data_from_steam_game_folder("Zero Escape", org_pak_folder, org_pak, overwrite=False)

    drive_to_local.replace_every_files_text(instance_worker)

    drive_to_local.replace_us_po(instance_worker)

    drive_to_local.download_images(instance_worker)

    drive_to_local.update_texte_progression(instance_worker, "recompilation")
    ze_ztd_tool.repack_ztd()
    ze_ztd_tool.copy_file_in_gamefolder(gamepath_directory)

# -------------------- Main code -------------------
if __name__ == "__main__":
    var = FileFolderUI()
    var.process_func = lambda: process(var.get_worker())
    var.has_progressbar = True
    var.has_lineedit = False
    var.run()

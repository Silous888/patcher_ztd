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
    gamepath_directory = steam_game_api.find_game_path("Zero Escape")

    # drive_to_local.replace_every_files_text(instance_worker)
    # drive_to_local.replace_us_po(instance_worker)

    # drive_to_local.update_texte_progression(instance_worker, "recompilation")
    ze_ztd_tool.repack_ztd()
    ze_ztd_tool.copy_file_in_gamefolder(gamepath_directory)


# -------------------- Main code -------------------
if __name__ == "__main__":
    var = FileFolderUI()
    var.process_func = lambda: process(var.get_worker())
    var.has_progressbar = True
    var.has_lineedit = False
    var.run()

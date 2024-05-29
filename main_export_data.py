"""File to export data from the game 428 Shibuya Scramble"""
import os
from API import steam_game_api
import shibuya_tools_api

# pyinstaller --onefile --name 428_Patch_extractor --icon=./ressource/DreamteamLogo.ico main_export_data.py


def process():
    """whole program, export data from the game in a folder
    """
    gamepath_directory: str | int = steam_game_api.find_game_path("428_shibuya_scramble_en")
    name_game_exe = "428 Shibuya Scramble.exe"
    gamepath = os.path.join(gamepath_directory, name_game_exe)
    export_folder: str = ".\\export\\"
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    shibuya_tools_api.export_game(gamepath, export_folder)


if __name__ == "__main__":
    process()

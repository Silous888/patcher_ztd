"""call the repack process"""

import subprocess


PATH_ZTD_DATA_TOOL: str = "ZTD_patch_data"

PATH_REPACK_SCRIPT: str = "ze_ztd_repack.bat"

PATH_PATCH_PAK: str = "patch_pak\\00000000.cfsi"


def repack_ztd():
    """repack the game"""
    subprocess.run(PATH_REPACK_SCRIPT,
                   shell=True,
                   check=False,
                   cwd=PATH_ZTD_DATA_TOOL)


def copy_file_in_gamefolder(path_gamefolder: str):
    """copy the patched file in the gamefolder

    Args:
        path_gamefolder (str): path of the gamefolder
    """
    command: list[str] = ["copy",
                          PATH_PATCH_PAK,
                          path_gamefolder]

    print("fichier 00000000.cfsi en cours de copie dans le dossier du jeu...")
    subprocess.run(command, shell=True,
                   check=False,
                   cwd=PATH_ZTD_DATA_TOOL)
    print("fichier 00000000.cfsi copié !")

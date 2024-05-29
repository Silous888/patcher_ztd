"""call the repack process"""

import subprocess


TOOL_ZTD: str = "ZTD_patch_data\\ze_ztd_repack.bat"


def repack_ztd():
    """repack the game"""
    subprocess.run(TOOL_ZTD,
                   shell=True,
                   creationflags=subprocess.CREATE_NO_WINDOW,
                   check=False)

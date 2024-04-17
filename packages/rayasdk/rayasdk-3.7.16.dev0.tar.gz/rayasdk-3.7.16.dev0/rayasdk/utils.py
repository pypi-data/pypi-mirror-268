import os
import json
import progressbar
import platform
import subprocess


import rayasdk.constants as constants
from rayasdk.messages import *
from rayasdk.logger import log_warning


class MyProgressBar:

    def __init__(self):
        self.pbar = None


    def __call__(self, block_num, block_size, total_size):
        if self.pbar is None:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


def is_snake_case(s: str):
    """
    Returns True if s is in snake case, False otherwise.
    """
    if not s.islower():
        return False
    if '__' in s:
        return False
    if s.startswith('_') or s.endswith('_'):
        return False
    if not all(c.isalpha() or c.isdigit() or c == '_' for c in s):
        return False
    return True


def validate_app_id_and_folder_name(app_id: str):
    APP_MAIN_FOLDER_NAME = os.path.basename(
        os.path.normpath(constants.CURRENT_PATH))
    if APP_MAIN_FOLDER_NAME != app_id:
        raise Exception('The app_id and the folder name are different')
    if not is_snake_case(app_id):
        raise Exception('The app_id have to be in snake case format')
    return True


def open_connection_file():
    try:
        with open(
                file=constants.CONNECTION_SETTINGS_PATH,
                mode='r',
                encoding='utf-8'
            ) as f:
            connection_settings = json.load(f)
        return connection_settings
    except OSError:
        raise Exception(
            (f'the file "{constants.CONNECTION_SETTINGS_FILE}" was not found, '
             'run \'rayasdk connect\''))


def change_directory(path):
    if os.path.isabs(path):
        os.chdir(path)
        return path
    else:
        abs_path = os.path.join(os.getcwd(), path)
        os.chdir(abs_path)
        return abs_path


def get_app_id():
    app_id = None
    try:
        with open(constants.EXECSETTINGS_PATH, 'r', encoding='utf-8') as f:
            exec_settings = json.load(f)
        app_id = exec_settings[constants.JSON_EXECINFO_APPID]
    except OSError:
        raise Exception(MSG_FOLDER_NOT_RAYA_APP)
    except KeyError as key:
        raise Exception(
            f'{key} key not found on {constants.EXECSETTINGS_FILE}.'
        )
    return app_id , exec_settings


def check_x11_server_running():
    flag = False
    if platform.system() == 'Linux':
        try:
            subprocess.check_output(['xdpyinfo'])
            flag = True
        except Exception:
            pass
    elif platform.system() == 'Darwin':
        flag = os.path.isdir(constants.MAC_X11_SERVER)
    
    if not flag:
        log_warning(MSG_X11_NOT_RUNNING)
        if platform.system() == 'Linux':
            log_warning(MSG_X11_NOT_RUNNING_LINUX)
        elif platform.system() == 'Darwin':
            log_warning(MSG_X11_MAC_OS_RECOMMENDATION)
    return flag

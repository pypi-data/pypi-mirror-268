# Copyright 2020 Unlimited Robotics

import os
import json
from shutil import copyfile

import rayasdk.constants as constants
from rayasdk.logger import log_error, log_verbose, log_info, log_status
from rayasdk.utils import validate_app_id_and_folder_name


class URInitializer:
    COMMAND = 'init'

    def __init__(self):
        pass


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help='initialize Raya project in current folder.'
        )
        self.parser.add_argument(
            '--app-id',
            help='application unique identificator',
            type=str
        )
        self.parser.add_argument(
            '--app-name',
            help='application name',
            type=str
        )


    def create_files_tree(self):
        try:
            os.mkdir(constants.DOC_PATH)
            os.mkdir(constants.RES_PATH)
            os.mkdir(constants.SRC_PATH)
            os.mkdir(constants.VSCODE_PATH)
            copyfile(constants.APP_PATH_ORIG,
                     constants.APP_PATH_DEST)
            copyfile(constants.MANIFEST_PATH_ORIG,
                     constants.MANIFEST_PATH_DEST)
            copyfile(constants.ENTRYPOINT_PATH_ORIG,
                     constants.ENTRYPOINT_PATH_DEST)
            copyfile(constants.VSCODE_SETTINGS_PATH_ORIG,
                     constants.VSCODE_SETTINGS_PATH_DEST)
            copyfile(constants.GITIGNORE_PATH_ORIG,
                     constants.GITIGNORE_PATH_DEST)
        except OSError as exc:
            log_info(exc)
            raise Exception(f'Could not create files tree')
        return True


    def create_json_exec_info(self):
        exec_settings = {}
        exec_settings[constants.JSON_EXECINFO_APPID] = self.args.app_id
        exec_settings[constants.JSON_EXECINFO_APPNAME] = self.args.app_name
        try:
            with open(constants.EXECSETTINGS_PATH, 'w', encoding='utf-8') as f:
                json.dump(exec_settings, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            log_error(f'Could not write file "{constants.EXECSETTINGS_FILE}".')
            return False
        return True


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs

        # if the app is not provided use the folder name
        if self.args.app_id is None:
            self.args.app_id = os.path.basename(
                os.path.normpath(constants.CURRENT_PATH)
            )
        # Check if the parent has the same name that the app id
        validate_app_id_and_folder_name(self.args.app_id)

        # Check if the directory is empty
        if len(os.listdir(constants.CURRENT_PATH)) != 0:
            raise Exception('Current directory is not empty.')

        # Files tree
        log_verbose('Creating application files tree...')
        self.create_files_tree()

        # Json SDK info
        log_verbose('Creating exec file...')
        self.create_json_exec_info()

        log_status('App initialized correctly!')
        return True

# Copyright 2020 Unlimited Robotics
import tempfile
from pathlib import Path

from rayasdk.messages import *

RAYAENV_DOCKER_VERSION_DEFAULT = '0.0.0'
GARYSIM_VERSION_DEFAULT = '0.0.0'
GARYSIM_VERSION = GARYSIM_VERSION_DEFAULT
RAYAENV_DOCKER_VERSION = RAYAENV_DOCKER_VERSION_DEFAULT

# alias for bash
CUSTOM_COMMAND_ALIAS = 'launch_command'

# Json SCAN Keys
JSON_SCAN_ID = 'ROBOT_ID'
JSON_SCAN_IP = 'ROBOT_IP'
JSON_SCAN_SERIAL = 'ROBOT_SERIAL'
JSON_SCAN_DOMAIN = 'RAYA_DOMAIN'
JSON_SCAN_RAYA_VERSION = 'RAYA_VERSION'
JSON_SCAN_PORT = 'PORT'

# ssh ROBOT
SSH_USER = 'rayadevel'
SSH_PORT = '2222'
SSH_APP_FOLDER = '~/apps/'

# Json SDK Info Keys
JSON_EXECINFO_APPID = 'app-id'
JSON_EXECINFO_APPNAME = 'app-name'
JSON_EXECINFO_SIM = 'simulation'
JSON_EXECINFO_ROB_CONN = 'robot-connection'
JSON_EXECINFO_ROB_ID = 'robot-id'
JSON_EXECINFO_ROB_IP = 'ip-address'
JSON_EXECINFO_ROB_SERIAL = 'robot-serial'
JSON_EXECINFO_ROB_DOMAIN = 'raya-domain'
JSON_EXECINFO_ROB_PORT = 'port'
JSON_EXECINFO_ROB_RAYA_VERSION = 'raya-version'

# Folders
TEMP_URSDK_FOLDER = 'ursdk'
TEMPLATES_FOLDER = 'template'
DOC_FOLDER = 'doc'
LOG_FOLDER = 'log'
RES_FOLDER = 'res'
SRC_FOLDER = 'src'
SKILLS_FOLDER = 'skills'
VSCODE_FOLDER = '.vscode'

# Files
LAST_SCANNING_FILE = 'last_scanning.json'
ENTRYPOINT_FILE = '__main__.py'
VSCODE_SETTINGS_FILE = 'launch.json'
APP_FILE = 'app.py'
MANIFEST_FILE = 'manifest.json'
EXECSETTINGS_FILE = 'exec_settings.json'
CONNECTION_SETTINGS_FILE = 'connection.json'
GITIGNORE_FILE = '.gitignore'

# Exclusions on sync app
EXCLUDE_FOLDER = ['__pycache__', '.git']

# System paths
TEMP_PATH = Path(tempfile.gettempdir())
CURRENT_PATH = Path().absolute()
URSDK_PATH = Path(__file__).parent.absolute()
UR_HOME = Path.home() / '.ur'
SIMS_HOME = UR_HOME / 'simulator'
SIMS_APPS = SIMS_HOME / 'apps'
SIMS_DATA_APPS = SIMS_HOME / 'data_apps'
SIMS_DATA_APPS_DEVEL = SIMS_HOME / 'data_apps_devel'
SSH_KEY_PRIV = UR_HOME / 'id_raya'
SSH_KEY_PUB = UR_HOME / 'id_raya.pub'

# Derived folder paths
URSDK_TEMP_PATH = TEMP_PATH / TEMP_URSDK_FOLDER
TEMPLATES_PATH = URSDK_PATH / TEMPLATES_FOLDER
DOC_PATH = CURRENT_PATH / DOC_FOLDER
LOG_PATH = CURRENT_PATH / LOG_FOLDER
RES_PATH = CURRENT_PATH / RES_FOLDER
SRC_PATH = CURRENT_PATH / SRC_FOLDER
MANIFEST_PATH = CURRENT_PATH / MANIFEST_FILE
SKILLS_PATH = CURRENT_PATH / SKILLS_FOLDER
VSCODE_PATH = CURRENT_PATH / VSCODE_FOLDER

# derived files paths
LAST_SCANNING_PATH = URSDK_TEMP_PATH / LAST_SCANNING_FILE
ENTRYPOINT_PATH_DEST = CURRENT_PATH / ENTRYPOINT_FILE
MANIFEST_PATH_DEST = CURRENT_PATH / MANIFEST_FILE
EXECSETTINGS_PATH = CURRENT_PATH / EXECSETTINGS_FILE
VSCODE_SETTINGS_PATH_DEST = VSCODE_PATH / VSCODE_SETTINGS_FILE
APP_PATH_DEST = SRC_PATH / APP_FILE
CONNECTION_SETTINGS_PATH = URSDK_TEMP_PATH / CONNECTION_SETTINGS_FILE
GITIGNORE_PATH_DEST = CURRENT_PATH / GITIGNORE_FILE

# template path

ENTRYPOINT_PATH_ORIG = TEMPLATES_PATH / ENTRYPOINT_FILE
VSCODE_SETTINGS_PATH_ORIG = TEMPLATES_PATH / VSCODE_SETTINGS_FILE
APP_PATH_ORIG = TEMPLATES_PATH / APP_FILE
MANIFEST_PATH_ORIG = TEMPLATES_PATH / MANIFEST_FILE
GITIGNORE_PATH_ORIG = TEMPLATES_PATH / GITIGNORE_FILE

# Docker Environment
RAYAENV_DOCKER_UR_ROOT = SIMS_HOME / 'ur_root'
RAYAENV_DOCKER_UR_ROOT_REPO = 'https://github.com/Unlimited-Robotics/raya_root_folder_simulation.git'
RAYAENV_DOCKER_UR_ROOT_REPO_BRANCH = 'main'
RAYAENV_DOCKER_IMGNAME = 'raya_os'
RAYAENV_DOCKER_IMGNAME_DEV = 'raya_sim_dev'
RAYAENV_DOCKER_IMG_VERSION_NAME = 'sim'
RAYAENV_DOCKER_IMG_VERSION_GPU = 'sim_gpu'

# VCS (Version Control System)
RAYA_OS_COMPONENTS = ['SDK', 'Unity', 'Docker']
#VCS_URL = 'https://dev.robotics.dev.webiz.ge/vcs'
# url = f'{VCS_URL}/version?major={self.__get_major(version)}&medium={self.__get_minor(version)}&platform={self.host_os}'
VCS_URL = 'https://raw.githubusercontent.com/Unlimited-Robotics/dirty_vcs/prod/vcs_info.json'
SYSTEM_DICT = {'Linux': 'linux', 'Windows': 'windows', 'Darwin': 'mac'}

# Skills
SKILLS_PYPI_INDEX = 'https://unlimited-robotics.github.io/skills/'

# Mac X11 Server
MAC_X11_SERVER = '/Applications/Utilities/XQuartz.app'
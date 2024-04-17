import json
import copy
from packaging.requirements import InvalidRequirement, Requirement

from rayasdk.exceptions import *
from rayasdk.utils import get_app_id
from rayasdk.logger import log_error, log_warning
from rayasdk.skills.dependencies_installer import SkillDepInstaller
import rayasdk.constants as constants

class SkillInstaller:
    COMMAND = 'install'

    def __init__(self) -> None:
        pass

    # Private
    
    def _get_index_skill_on_list(self, data_list, name):
        index = -1
        for i, item in enumerate(data_list):
            if item.get("name") == name:
                index = i
                break
        return index
    
    def _validate_pep508(self,version):
        return
        try:
            Requirement(version)
        except InvalidRequirement:
            raise Exception(f'Invalid version {version}')
    
    # Public
    
    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help='Install a skill into a RaYa app'
        )
        self.parser.add_argument(
            'skill',
            help='Name of the skill'
        )
        self.parser.add_argument(
            'version',
            nargs='?',
            default='latest',
            help='Version argument',
        )


    def run(self, args, unknownargs) -> None:
        get_app_id()
        if args.version != 'latest':
            version = args.version
            if not args.version.startswith(('>=', '<=', '==', '~=', '!=', '<', '>')):
                version = f'=={args.version}'
            self._validate_pep508(version)
        else:
            version = args.version
        
        # Get the manifest.json file
        try:
            with open(constants.MANIFEST_PATH, 'r') as file:
                manifest_data = json.load(file)
                manifest_data_old = copy.deepcopy(manifest_data)
        except FileNotFoundError:
            raise SkillManifestNotFound(
                f'\'{constants.MANIFEST_FILE}\' not found'
            )
        except ValueError:
            raise Exception(f'\'{constants.MANIFEST_FILE}\' wrong formated')
        
        # Check if dependencies.skills exists
        if 'dependencies' not in manifest_data:
            manifest_data['dependencies'] = {}
        if 'skills' not in manifest_data['dependencies']:
            manifest_data['dependencies']['skills'] = []
        
        skills_registered = manifest_data['dependencies']['skills']
        
        # Search for the skill on the manifest data
        skill_index_manifest = self._get_index_skill_on_list(
            name=args.skill,
            data_list=skills_registered
        )
        log_warning(
            f'Adding the skill \'{args.skill}\' version = \'{version}\''
        )
        if skill_index_manifest == -1:
            if version == 'latest':
                skills_registered.append({
                    'name': args.skill,
                })
            else:
                skills_registered.append({
                    'name': args.skill,
                    'version': version,
                })
        elif version != 'latest':
            skills_registered[skill_index_manifest]['version'] = version
                    
        # save the json file
        with open(constants.MANIFEST_PATH, 'w', encoding='utf-8') as file:
             json.dump(manifest_data, file, ensure_ascii=False, indent=4)
             
        skill_installer = SkillDepInstaller() 
        # Install Skills
        try:
            log_warning('Downloading skills...')
            skill_installer.install_skills()
        except Exception as error:
            log_error(error)
            print('Error installing skills')
            with open(constants.MANIFEST_PATH, 'w', encoding='utf-8') as file:
                json.dump(manifest_data_old, file, ensure_ascii=False, indent=4)
            return False
        return True
    
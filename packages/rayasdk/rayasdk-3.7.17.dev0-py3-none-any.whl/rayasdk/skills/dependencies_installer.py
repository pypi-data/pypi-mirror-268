import json
import os
import shutil
import subprocess
import fcntl
import sys
import select


import rayasdk.constants as constants
from rayasdk.utils import get_app_id
from rayasdk.logger import log_warning, log_error, log_success
from rayasdk.exceptions import *


class SkillDepInstaller:
    COMMAND = 'install_deps'

    def __init__(self) -> None:
        pass

    # Private
    
    def _find_manifest_files(self, directory):
        manifest_files = []
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename == constants.MANIFEST_FILE:
                    manifest_files.append(os.path.join(root, filename))
        return manifest_files
    
    
    def _delete_skills_folder_contents(self, execute=True):
        if execute:
            shutil.rmtree(
                path=constants.SKILLS_PATH,
                ignore_errors=True
            )
    
    
    def _handle_input(self):
        try:
            user_input = input()
            self.process.stdin.write(user_input + '\n')
            self.process.stdin.flush()
        except EOFError:
            pass


    def _install_skills_requiered(self, skills):
        skills_cmd = ''
        for skill in skills.split(' '):
            skills_cmd+= f'\'{skill}\' '
        command = (
            'python3 -m pip install '
            f'--extra-index-url {constants.SKILLS_PYPI_INDEX} '
            f'--target={constants.SKILLS_PATH} {skills_cmd}'
        )
        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            shell=True, 
            bufsize=1
        )
        fcntl.fcntl(self.process.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
        fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, os.O_NONBLOCK)
        fcntl.fcntl(self.process.stderr, fcntl.F_SETFL, os.O_NONBLOCK)
        fds = [self.process.stdout, self.process.stderr]
        stdout_data = ""
        stderr_data = ""

        while True:
            readable, _, _ = select.select(fds + [sys.stdin], [], [])
            if sys.stdin in readable:
                self._handle_input()
            for fd in fds:
                if fd in readable:
                    data = fd.read()
                    if fd == self.process.stdout:
                        stdout_data += data
                    else:
                        stderr_data += data
                    # print(data, end='')

            if self.process.poll() is not None:
                break
        stdout_data += self.process.stdout.read()
        stderr_data += self.process.stderr.read()
        return_code = self.process.returncode
        return return_code , stdout_data, stderr_data


    # Public
    

    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help='Download and install the skills dependencies'
        )
        self.parser.add_argument(
            '--no-delete',
            action='store_false',
            help='It will not delete the contents of the skills folders'
        )


    def install_skills(self):
        # Read the manifest of the app
        with open(constants.MANIFEST_PATH, 'r') as json_file:
            manifest_json = json.load(json_file)
        app_skills_json = manifest_json['dependencies']['skills']
        
        # Check if the app has skills to download
        if len(app_skills_json) == 0:
            log_warning(
                'There is no skills in the '
                f'\'{constants.MANIFEST_FILE}\' of the app'
            )
            return False
        
        # Parse the skills to list
        skills = ' '.join(
            f"{d['name']}{d.get('version','').replace(' ', '')}"\
            for d in app_skills_json
        )

        # Install the skills
        try:
            return_code, std_out, std_err = self._install_skills_requiered(
                skills=skills
            )
            if return_code != 0:
                self._delete_skills_folder_contents()
                raise Exception(std_err)
            else:
                lines = std_out.split('\n')
                log_success(f'{lines[-3]}')
                log_success(f'{lines[-2]}')
            
        except KeyboardInterrupt:
            raise Exception('Installation canceled')
        
        # Create the init.py
        with open(f'{constants.SKILLS_PATH}/__init__.py', 'w') as file:
            pass
            


    def run(self, args, unkownargs) -> None:
        # Check if the Current Path is an app
        get_app_id()
        
        # Check Delete skills folder flag
        self._delete_skills_folder_contents(execute=args.no_delete)
        
        # Install Skills
        try:
            self.install_skills()
        except Exception as error:
            log_error(error)
            return False
        return True

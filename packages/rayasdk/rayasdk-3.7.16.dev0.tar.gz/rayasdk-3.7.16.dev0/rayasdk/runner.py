# Copyright 2020 Unlimited Robotics

import json
import subprocess
import os
import importlib

import rayasdk.constants as constants
from rayasdk.messages import *
from rayasdk.logger import log_error, log_info, log_status
from rayasdk.sshKeyGen import SshKeyGen
from rayasdk.utils import change_directory, open_connection_file
from rayasdk.utils import validate_app_id_and_folder_name
from rayasdk.utils import check_x11_server_running
from rayasdk.utils import get_app_id

class URRunner:

    COMMAND = 'run'

    def __init__(self):
        pass


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            add_help=False,
            help="connect current raya project to a robot or simulator.")
        self.parser.add_argument(
            '--debug',
            help='runs applications in debug mode',
            action="store_true",
            default=False,
        )
        self.parser.add_argument(
            '--only-sync',
            help='Syncs the app on the connected robot',
            action="store_true",
            default=False
        )
        self.parser.add_argument(
            '--display-host',
            help='opens an x11 server on the robot',
            action="store_true",
            default=False,
        )


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs

        
        if len(self.unknownargs) != 0:
            execution_path = self.unknownargs[0]
            if not str(execution_path).startswith('-'):
                if os.path.exists(execution_path):
                    change_directory(execution_path)
                    del execution_path
                    globals()[constants] = importlib.reload(constants)
                else:
                    log_error(
                            f'The path \'{execution_path}\' does not exist'
                        )
                    return False

        # Open exec_settings file
        try:
            app_id, exec_settings  = get_app_id()
        except Exception as error:
            log_error(str(error))
            return False
        
        # Check if the parent has the same name that the app id
        if not validate_app_id_and_folder_name(app_id):
            log_error('The name of the folder is different from the app-id.')
            return False

        # Execute app
        try:
            connection_settings = open_connection_file()
            connection_settings['app_id'] = exec_settings[
                constants.JSON_EXECINFO_APPID]

            host = connection_settings[constants.JSON_EXECINFO_ROB_CONN][
                    constants.JSON_EXECINFO_ROB_IP]
            connection_settings[
                'hostname'] = f'{constants.SSH_USER}@{host}'
            connection_settings['host'] = host
            port = connection_settings[constants.JSON_EXECINFO_ROB_CONN][
                        constants.JSON_EXECINFO_ROB_PORT]
            
            if connection_settings[constants.JSON_EXECINFO_SIM]:
                log_status(MSG_SYNC_APP_SIM)
            else:
                log_status((
                    f'{MSG_SYNC_APP_ROBOT} '
                    f'\'{connection_settings["hostname"]}:{port}\'...'
                ))

            self.sync_app(connection_settings=connection_settings)
            if self.args.only_sync:
                log_status(MSG_SYNC_APP_SUCCESS)
                return True

            log_status(MSG_LAUNCHING_APP)
            exit_code = self.launch_app(
                    app_id=connection_settings['app_id'],
                    host_url=connection_settings['hostname'],
                    args=self.unknownargs,
                    port=port,
                    debug=self.args.debug
                )

            log_status(f'{MSG_APP_FINISHED} with exit code {exit_code}')
            return True
        except Exception as error:
            log_error(str(error))
            return False


    def sync_app(self, connection_settings):
        hostname = connection_settings['hostname']
        app_id = connection_settings['app_id']
        host = connection_settings['host']
        port = connection_settings[constants.JSON_EXECINFO_ROB_CONN][constants.JSON_EXECINFO_ROB_PORT]

        try:
            origin_path = os.getcwd()
            folders_excluded = ' '.join([f'--exclude \'{folder}\'' for folder in constants.EXCLUDE_FOLDER])
            command = ((
                    'rsync '
                    '--archive '
                    '--delete '
                    f'{folders_excluded} '
                    f'--rsh=\'ssh -p {port} '
                    '-o BatchMode=yes '
                    f'-i {constants.SSH_KEY_PRIV}\' '
                    f'{origin_path}/ '
                    f'{hostname}:{constants.SSH_APP_FOLDER}/{app_id}'
                ))
            subprocess.run(
                    command, 
                    shell=True,
                    capture_output=True
                ).check_returncode()
        except subprocess.CalledProcessError as e:
            SshKeyGen.check_ssh_error(
                    error=e.stderr.decode("utf-8"),
                    host=host,
                    port=port
                )


    def launch_app(self, app_id, host_url, args, port, debug=False):
        execution_route = f'%s%s' % (constants.SSH_APP_FOLDER, app_id)

        if debug:
            cmd = (
                    'python3 -m debugpy --listen 5678 --wait-for-client '
                    './__main__.py '
                )
        else:
            cmd = f'python3 __main__.py '
        cmd += ' '.join(args)

        real_robot_flag = not host_url.endswith('localhost')
        x_11_flag = '-X -C ' if check_x11_server_running() else ''
        if self.args.display_host:
            x_11_flag = ''
        

        if debug and real_robot_flag:
            command = (('ssh -2 -t '
                        f'{x_11_flag}'
                        '-o LogLevel=QUIET '
                        f'-i {constants.SSH_KEY_PRIV} '
                        '-L 5678:localhost:5678 '
                        f'-p {port} {host_url} '
                        f'\'cd {execution_route} && {cmd}\''))
        else:
            command = (('ssh -t '
                        f'{x_11_flag}'
                        '-o LogLevel=QUIET '
                        f'-i {constants.SSH_KEY_PRIV} '
                        f'-p {port} {host_url} '
                        f'\'cd {execution_route} && {cmd}\''))

        if debug:
            log_info('Waiting for debug client (VSCode)...')

        exit_code = subprocess.call(command, shell=True)
        log_info('')
        return exit_code

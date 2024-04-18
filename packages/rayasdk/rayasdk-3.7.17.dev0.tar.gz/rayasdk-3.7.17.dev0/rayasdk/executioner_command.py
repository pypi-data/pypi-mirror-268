# Copyright 2020 Unlimited Robotics
import subprocess

import rayasdk.constants as constants
from rayasdk.messages import *
from rayasdk.logger import log_status, log_info
from rayasdk.utils import open_connection_file


class URExecCommand:

    COMMAND = 'command'

    def __init__(self):
        pass


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND, 
            help='Sends a command and executes on the RayaOS')
        self.parser.add_argument(
            'command_name',
            nargs=1,
            type=str,
            help='Command to execute'
        )

    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        connection_settings = open_connection_file()
        
        host = connection_settings[constants.JSON_EXECINFO_ROB_CONN][
                constants.JSON_EXECINFO_ROB_IP]
        
        
        connection_settings['hostname'] = f'{constants.SSH_USER}@{host}'
        connection_settings['host'] = host
        log_status((
            f'{MSG_SCRIPT_RUNNING} \'{connection_settings["hostname"]}\'...'
        ))
        
        self.execute_script(
                connection_settings=connection_settings,
                command_name=self.args.command_name[0],
                args=self.unknownargs
            )
        return True


    def execute_script(self, connection_settings, command_name, args):
        host_url = connection_settings['hostname']
        ssh_port = connection_settings[constants.JSON_EXECINFO_ROB_CONN][constants.JSON_EXECINFO_ROB_PORT]
        cmd = f'{command_name} ' + ' '.join(args)
        # command_to_run = f'./{command_name}.sh ' + ' '.join(args)
        # log_status(f'\'{command_to_run}\'')
        
        cmd = f'\'{constants.CUSTOM_COMMAND_ALIAS} {cmd}\''
        command_name = ((
                'ssh -t '
                '-o LogLevel=QUIET '
                f'-i {constants.SSH_KEY_PRIV} '
                f'-p {ssh_port} {host_url} '
                f'{cmd}'
            ))
        subprocess.call(command_name, shell=True)
        log_info('')
        
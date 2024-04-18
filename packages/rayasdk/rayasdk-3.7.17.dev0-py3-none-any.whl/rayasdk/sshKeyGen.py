# Copyright 2020 Unlimited Robotics

import os
from pathlib import Path
import sys
import subprocess
import glob
import paramiko

import rayasdk.constants as constants
from rayasdk.logger import log_info, log_warning, log_error, log_status

# Constants
CUR_USER_HOME = os.path.expanduser('~')
PLATFORM = sys.platform


class SshKeyGen:

    def __init__(self, user, host, port=22):
        if PLATFORM == 'windows':
            # TODO implement this on ws
            self.PRIV_SSH_DIR = f'{CUR_USER_HOME}/.ssh'
        elif PLATFORM == 'linux' or PLATFORM == 'darwin':
            self.PRIV_SSH_DIR = f'{CUR_USER_HOME}/.ssh'
        else:
            raise Exception('System Not Found')

        if not os.path.exists(self.PRIV_SSH_DIR):
            if not self.__create_ssh_directory():
                raise Exception('Failed to create SSH directory')

        try:
            self.__push_key(user=user, host=host, port=port)
        except Exception as error:
            self.check_ssh_error(error=str(error), host=host, port=port)


    def __create_ssh_directory():
        ssh_directory = os.path.expanduser('~/.ssh')
        try:
            subprocess.run(['mkdir', '-m', '700', ssh_directory], check=True)
            return True
        except subprocess.CalledProcessError as e:
            return False


    def __key_present(self):
        '''Checks to see if there is an key already present. Returns a bool.'''
        matching_files = glob.glob(
            os.path.join(constants.UR_HOME, constants.SSH_KEY_PRIV))
        if matching_files:
            log_info('SSH key found')
            if not self.__check_key():
                return False
            return True
        return False


    def __gen_key(self):
        '''Generate a SSH Key.'''
        os.chdir(self.PRIV_SSH_DIR)
        if self.__key_present():
            return False
        # Generate private key
        log_info('Creating SSH Key')
        key = paramiko.RSAKey.generate(2048)
        key.write_private_key_file(constants.SSH_KEY_PRIV)
        with open(constants.SSH_KEY_PUB, 'w') as f:
            f.write(f'ssh-rsa {key.get_base64()}')
        os.chmod(constants.SSH_KEY_PUB, 0o400)
        return True
    
    
    def __check_key(self):
        '''Check the key'''
        permissions = oct(os.stat(constants.SSH_KEY_PUB).st_mode)[-3:]
        if permissions != '400':
            log_error(f'Error: Wrong Permission on {constants.SSH_KEY_PUB}, Removing key...')
            os.remove(constants.SSH_KEY_PUB)
            os.remove(constants.SSH_KEY_PRIV)
            return False
        return True


    def __push_key(self, user, host, port=22):
        '''Push an SSH Key to a remote server.'''
        self.__gen_key()

        log_status('Pushing key to remote server')
        command = f'eval "$(ssh-agent -s)" && ssh-add {constants.SSH_KEY_PRIV} && ' 
        command += f'ssh-copy-id '
        command += f'-i {constants.SSH_KEY_PRIV} -p {port} {user}@{host}'
        ssh_copy_process = subprocess.Popen(command,
                                            shell=True,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
        out, err = ssh_copy_process.communicate()
        if ssh_copy_process.returncode != 0:
            raise Exception(err.decode())


    @staticmethod
    def remote_host_change(host, port):
        command = (('ssh-keygen '
                    f'-f "{Path.home()/".ssh"/"known_hosts"}" '
                    f'-R "[{host}]:{port}"'))
        return subprocess.run(command,
                              shell=True,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL).check_returncode()


    @staticmethod
    def check_ssh_error(error, host, port):
        if 'REMOTE HOST IDENTIFICATION HAS CHANGED' in error:
            log_warning(('Remote Host Identification Has Changed'))
            SshKeyGen.remote_host_change(host=host, port=port)
            SshKeyGen(host=host,port=port, user=constants.SSH_USER)
        elif 'No route to host' in error:
            raise Exception(('No route to host.'))
        elif 'Connection refused' in error:
            raise Exception((
                'Connection refused. Check that the Ra-Ya system is running.'))
        elif 'Host key verification failed' in error:
            raise Exception(('Host key verification failed, '
                             'run \'rayasdk connect\'.'))
        else:
            raise Exception(error)

import subprocess
import psutil
import requests
import re

import rayasdk.constants as constants
from rayasdk.logger import log_error, log_info, log_success, log_warning
from rayasdk.messages import *
from rayasdk.container_handlers.docker_handler import DockerHandler
from rayasdk.simulator import URSimulator


class URVCS:

    COMMAND = 'update'

    def __init__(self):
        self.docker_handler = DockerHandler()
        self.simulator = URSimulator()
        self.GARYSIM_VERSION = self.simulator.GARYSIM_VERSION
        self.RAYAENV_DOCKER_VERSION = self.docker_handler.RAYAENV_DOCKER_VERSION
        self.RAYAENV_DOCKER_IMAGE_NAME = self.docker_handler.RAYAENV_DOCKER_IMAGE_NAME


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND, help='Update the SDK, Unity or Docker')


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        self.update_is_running()
        
        simulation_is_running = self.simulator.simulation_is_running()
        raya_os_running = self.docker_handler.check_running_container()
        if simulation_is_running:
            raise Exception(
                'Can\'t update there is a unity simulator instance active'
                )
        if raya_os_running != False:
            raise Exception(
                    'Can\'t update there is a RayaOS container running: '
                )
        
        
        log_info('Checking for updates...')
        try:
            if not self.full_updated(
            ) or not self.minor_updated(
            ) or not self.patch_updated(
            ) or self.simulator.simulator_not_found(
            ) or self.docker_handler.RayaOS_not_found(
            ):
                download_input = input(
                        f'Do you want to download '
                        'the Simulator and/or RayaOS? [Y/n]'
                    )
                if download_input not in ['y', 'Y', 'yes', 'Yes', 'YES', '']:
                    return False
                if not self.update_full():
                    log_error('Update failed.')
                    return False
            log_success('Everything is up to date')
            return True
        except requests.exceptions.ConnectionError:
            log_error(
                'There was a Connection Error, '
                'The Version Control System does not respond.'
            )
            return False


    def __get_major(self, version):
        return int(version.split('.')[0])


    def __get_minor(self, version):
        return int(version.split('.')[1])


    def __get_patch(self, version):
        try:
            patch = version.split('.')[2]
            if patch:
                patch_version = str(patch)
                patch_version = re.findall(r'^(\d+)', patch_version)[0]
                return patch_version
        except:
            return '0'


    def __local_version(self, component):
        '''
        Return the local version of the component
        '''
        if component == 'SDK':
            res = subprocess.check_output(
                "pip show rayasdk --version|grep Version | awk '{print $2}'",
                shell=True)
            return re.findall(r'\d+\.\d+\.\d+', res.decode('utf-8'))[0]
        elif component == 'Unity':
            return self.GARYSIM_VERSION
        elif component == 'Docker':
            return self.RAYAENV_DOCKER_VERSION


    def __get_latest_version(self, component):
        '''
        Return the latest version of the component
        '''
        # response = requests.request("GET", f'{VCS_URL}/latest/{component}')
        # return(data['versionId'])
        response = self.get_VCS_json(
                type_version='latest',
                component=component
            )
        for raya_component in response:
            if raya_component['name'] == component:
                return raya_component['versionId']


    def full_updated(self, component=None, show_msg=True):
        if component:
            local = self.__local_version(component)
            latest = self.__get_latest_version(component)
            diff_major = self.__get_major(latest) > self.__get_major(local)
            if diff_major:
                if show_msg:
                    log_warning((
                            f'{component} have a major update, '
                            f'current: \'{local}\' -> latest: \'{latest}\''
                        ))
                return False
            else:
                return True

        updated = True
        for raya_component in constants.RAYA_OS_COMPONENTS:
            local = self.__local_version(raya_component)
            latest = self.__get_latest_version(raya_component)
            diff_major = self.__get_major(latest) > self.__get_major(local)
            if diff_major:
                if show_msg:
                    log_warning((
                            f'{raya_component} have a major update, '
                            f'current: \'{local}\' -> latest: \'{latest}\''
                        ))
                updated = False
        return updated


    def update_full(self):
        # Update Unity
        if self.__get_latest_version('Unity') != self.__local_version(
                'Unity') or self.simulator.simulator_not_found():
            response = self.get_VCS_json(
                    type_version='latest',
                    component='Unity'
                )
            if not self.simulator.download_simulator(response=response):
                return False
            log_success('Simulator updated successfully')

        # Update Docker
        if self.__get_latest_version('Docker') != self.__local_version(
                'Docker') or self.docker_handler.RayaOS_not_found():
            version = self.__get_latest_version('Docker')
            if not self.docker_handler.download_raya_image(version):
                return False
            log_success('Raya_OS updated successfully')

        return True


    def minor_updated(self, component=None, show_msg=True):
        '''Function to check if the latest version is a minor version'''
        if component:
            local = self.__local_version(component)
            latest = self.__get_latest_version(component)
            same_major = self.__get_major(latest) == self.__get_major(local)
            diff_minor = self.__get_minor(latest) > self.__get_minor(local)
            if same_major and diff_minor:
                if show_msg:
                    log_warning((
                            f'{component} have a minor update, '
                            f'current: \'{local}\' -> latest: \'{latest}\''
                        ))
                return False
            else:
                return True

        updated = True
        for raya_component in constants.RAYA_OS_COMPONENTS:
            local = self.__local_version(raya_component)
            latest = self.__get_latest_version(raya_component)
            same_major = self.__get_major(latest) == self.__get_major(local)
            diff_minor = self.__get_minor(latest) > self.__get_minor(local)
            if same_major and diff_minor:
                if show_msg:
                    log_warning((
                            f'{raya_component} have a minor update, '
                            f'current: \'{local}\' -> latest: \'{latest}\''
                        ))
                updated = False
        return updated


    def update_minor(self, component):
        '''Update the component and return True if the update was successful'''
        download_input = input(
            f'Do you want to download '
            'the Simulator and the Docker Image? [Y/n]\''
        )
        if download_input not in ['y', 'Y', 'yes', 'Yes', 'YES', '']:
            return False
        if component == 'Unity':
            response = self.get_VCS_json(type_version='minor',
                                         component='Unity')
            version = self.__get_latest_version(component)
            if self.simulator.download_simulator(response=response):
                return True
        elif component == 'Docker':
            version = self.__get_latest_version(component)
            if self.docker_handler.download_raya_image(version):
                return True
        return False


    def patch_updated(self, component=None, show_msg=True):
        '''Function to check if the latest version is a patch'''
        if component:
            local = self.__local_version(component)
            latest = self.__get_latest_version(component)
            same_major = self.__get_major(latest) == self.__get_major(local)
            diff_patch = self.__get_patch(local) < self.__get_patch(latest)
            same_minor = self.__get_minor(latest) == self.__get_minor(local)
            if same_major and same_minor and diff_patch:
                if show_msg:
                    log_warning((
                            f'{component} have an patch update it is '
                            f'going to be updated to version \'{latest}\', '
                            f'current \'{local}\''
                        ))
                return False
            else:
                return True

        updated = True
        for raya_component in constants.RAYA_OS_COMPONENTS:
            local = self.__local_version(raya_component)
            latest = self.__get_latest_version(raya_component)
            same_major = self.__get_major(latest) == self.__get_major(local)
            same_minor = self.__get_minor(latest) == self.__get_minor(local)
            diff_patch = self.__get_patch(local) < self.__get_patch(latest)
            if same_major and same_minor and diff_patch:
                if show_msg:
                    log_warning((
                            f'{raya_component} have an patch update it '
                            f'is going to be updated to version \'{latest}\', '
                            f'current \'{local}\''
                        ))
                updated = False
        return updated

    def update_patch(self, component):
        '''Update the component and return True if the update was successful'''
        if component == 'Unity':
            response = self.get_VCS_json(
                    type_version='patch',
                    component='Unity'
                )
            version = self.__get_latest_version(component)
            if self.simulator.download_simulator(response=response):
                return True
        elif component == 'Docker':
            version = self.__get_latest_version(component)
            if self.docker_handler.download_raya_image(version):
                return True
        return False


    def get_latest_version(self, component):
        return self.__get_latest_version(component=component)


    def get_VCS_json(self,
                type_version: str = 'latest',
                component: str = None
            ):
        try:
            response = requests.request("GET", constants.VCS_URL)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            raise e
        except Exception as e:
            log_error(e)
        return None


    def update_is_running(self):
        instances = 0
        process_args = ['rayasdk', 'update']
        for process in psutil.process_iter(['cmdline']):
            if process.info['cmdline']:
                cmdline_args = process.info['cmdline']
                if len(cmdline_args
                       ) >= len(process_args) + 1 and cmdline_args[1].endswith(
                           process_args[0]
                       ) and cmdline_args[2:] == process_args[1:]:
                    instances += 1
        if instances >= 2:
            raise Exception('The update command is already executing')

# Copyright 2020 Unlimited Robotics
import os
import subprocess
import urllib
import tarfile
import platform
import re
import psutil

from simple_file_checksum import get_checksum
from time import sleep
from pathlib import Path

import rayasdk.constants as constants
from rayasdk.messages import *
from rayasdk.utils import MyProgressBar
from rayasdk.logger import log_error, log_info, log_status, log_warning
from rayasdk.container_handlers.docker_handler import DockerHandler


class URSimulator:

    COMMAND = 'simulator'

    def __init__(self):
        self.host_os = platform.system()
        self.SIM_BINARY = None
        self.GARYSIM_URL = None
        self.SIM_TARPATH = None
        self.GARYSIM_SHA256 = None
        self.SIMS_HOME = constants.SIMS_HOME
        self.GARYSIM_VERSION = None
        self.init_sim_path_os()


    def init_sim_path_os(self, version=None):
        self.GARYSIM_VERSION = self.get_simulation_version(version)
        self.PREFIX_SIM = 'raya_simulator'
        if self.host_os == 'Linux':
            self.SIM_PATH = self.SIMS_HOME / Path(
                f'{self.PREFIX_SIM}_{self.GARYSIM_VERSION}_linux')
            self.EXECUTABLE = 'Linux.x86_64'

        elif self.host_os == 'Windows':
            self.SIM_PATH = self.SIMS_HOME / Path(
                f'{self.PREFIX_SIM}_{self.GARYSIM_VERSION}_windows')
            self.EXECUTABLE = 'Windows.exe'

        # TODO: MAC version - M1
        elif self.host_os == 'Darwin':
            self.SIM_PATH = self.SIMS_HOME / Path(
                f'{self.PREFIX_SIM}_{self.GARYSIM_VERSION}_mac')
            self.EXECUTABLE = 'Mac.App'
        
        self.SIM_TARPATH = Path(f'{self.SIM_PATH}.tar.gz')
        self.SIM_BINARY = str(self.SIM_PATH / Path(self.EXECUTABLE))


    def get_simulation_version(self, version=None):
        # Simulator version
        sim_versions = [
            re.search(r'\d+\.\d+\.\d+', folder_name).group()
            for folder_name in os.listdir(constants.SIMS_HOME)
            if os.path.isdir(os.path.join(constants.SIMS_HOME, folder_name))
            and folder_name.startswith('raya_simulator_')
        ]
        sim_versions.sort()
        if version is not None and version in sim_versions:
            return version
        elif version == 'latest' or version is None:
            if sim_versions:
                return sim_versions[-1]
            else:
                return constants.GARYSIM_VERSION_DEFAULT
        else:
            log_error(f'\'{version}\' is not a valid simulator version')
            log_warning(f'Available: {sim_versions}')


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help='Run the simulator container and the unity simulator'
        )
        self.parser.add_argument(
            '--debug',
            help='Runs only the unity simulation for dev version of the container',
            action='store_true'
        )
        self.parser.add_argument(
            '--sim-version',
            help='Runs a specific unity simulator version',
            default='latest',
            type=str,
        )
        self.parser.add_argument(
            '--rayaos-version',
            help='Runs a specific Ra-Ya OS image version',
            default='latest',
            type=str,
        )


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        self.init_sim_path_os(self.args.sim_version)

        if not os.path.exists(self.SIM_BINARY):
            log_error('Simulator not found, run rayasdk update to download it')
            return False

        # If debug flag not set run container
        container_process = None
        if not self.args.debug:
            try:
                log_status(MSG_RAYA_OS_IMAGE)
                container_process = DockerHandler().launch_container(
                        version=self.args.rayaos_version
                    )
                if type(container_process) == bool:
                    return False
                sleep(5)
            except KeyboardInterrupt:
                pass

        # Run unity simulation
        log_status(MSG_UNITY_SIM)
        if self.simulation_is_running():
            log_error('There is already a unity simulation running')
            return False
        simulator_process = subprocess.Popen([str(self.SIM_BINARY)] +
                                             self.unknownargs,
                                             stdout=subprocess.PIPE)

        if container_process is not None:
            while True:
                if container_process.poll() is not None:
                    break
            container_process.terminate()
        else:
            try:
                simulator_process.wait()
            except KeyboardInterrupt:
                pass

        simulator_process.terminate()
        return True


    def simulator_not_found(self):
        return not os.path.exists(f'{self.SIM_BINARY}')


    def download_simulator(self, response=None):
        # Set parameters from local constants file
        sim_url = self.GARYSIM_URL
        garysim_sha256 = self.GARYSIM_SHA256
        version = self.GARYSIM_VERSION
        if response is not None:
            # Get parameters from VCS API
            for component in response:
                if component['name'] == 'Unity':
                    response = component
            sim_url = response["link"]
            garysim_sha256 = response["checksum"]
            version = response["versionId"]
           
        sim_tarpath = f'{constants.SIMS_HOME}/simulator_{version}.tar.gz'
        
        # Download simulator from url
        if not os.path.exists(sim_tarpath):
            log_info(f'Downloading Ra-Ya simulator v{version}...')
            try:
                urllib.request.urlretrieve(sim_url, sim_tarpath, MyProgressBar())
            except urllib.error.HTTPError:
                log_error(f'Download error, the url {sim_url} does not exist.')
                return False

        # Verify checksum
        try:
            log_info(f'Checking downloaded file...')
            sha256 = get_checksum(sim_tarpath, algorithm="SHA256")
        except FileNotFoundError:
            log_error('Download error, try again.')
            return False
        if garysim_sha256 != sha256:
            log_error('Checksum validation failed, try again.')
            return False

        # Extract folder
        log_info(f'Extracting...')
        simtar = tarfile.open(sim_tarpath)
        simtar.extractall(constants.SIMS_HOME)
        os.remove(sim_tarpath)
        return True
    
    
    def simulation_is_running(self):
        for process in psutil.process_iter(['cmdline']):
            if process.info['cmdline']:
                cmdline_args = process.info['cmdline']
                if cmdline_args[0].endswith(
                        self.EXECUTABLE
                ) and self.PREFIX_SIM in cmdline_args[0]:
                    return True
        return False

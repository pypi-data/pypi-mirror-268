#!/usr/bin/env python

# Copyright 2020 Unlimited Robotics

import argparse
import os
import sys
import platform
import shutil
import subprocess
from git import Repo, GitCommandError

import rayasdk.constants as constants
from rayasdk.connect import URConnect
from rayasdk.vcs import URVCS
from rayasdk.logger import log_error, log_verbose, log_info, set_logger_level
from rayasdk.logger import log_success, log_warning
from rayasdk.scanner import URScanner
from rayasdk.initializer import URInitializer
from rayasdk.runner import URRunner
from rayasdk.simulator import URSimulator
from rayasdk.killer import URKiller
from rayasdk.executioner_command import URExecCommand
from rayasdk.tools_command import URTools
from rayasdk.skills_manager import URSkillManager

class URSDK:

    def __init__(self):
        self.wrong_init = False
        # Check for temp folder
        if not self.init_ursdk_folder():
            self.wrong_init = True
        # Check .ur folder
        if not self.check_global_folder():
            log_error(f'Could not create .ur folder')
            self.wrong_init = True

        if self.wrong_init:
            return None
        
        self.command_objects = []
        self.command_objects.append(URInitializer())
        self.command_objects.append(URScanner())
        self.command_objects.append(URConnect())
        self.command_objects.append(URRunner())
        self.command_objects.append(URSimulator())
        self.command_objects.append(URKiller())
        self.command_objects.append(URVCS())
        self.command_objects.append(URExecCommand())
        self.command_objects.append(URTools())
        self.command_objects.append(URSkillManager())
        self.init_parser()


    def init_parser(self):
        # Init top parser
        self.argparser = argparse.ArgumentParser(
            description='Unlimited Robotics SDK',
        )
        group = self.argparser.add_mutually_exclusive_group()
        group.add_argument("-v",
                           "--verbose",
                           action="store_true",
                           help="increase output verbosity.")
        group.add_argument("-q",
                           "--quiet",
                           action="store_true",
                           help="don't print on stdout.")
        subparsers = self.argparser.add_subparsers(help='SDK Command',
                                                   dest='command')
        subparsers.required = True
        # Init subparsers
        for obj in self.command_objects:
            obj.init_parser(subparsers)
        # Parse arguments
        self.args, self.unknownargs = self.argparser.parse_known_args()
        # Setup Logger
        set_logger_level(self.args.verbose, self.args.quiet)


    def check_global_folder(self):
        try:
            # create folders that are needed in the .ur path
            os.makedirs(constants.SIMS_APPS, exist_ok=True)
            os.makedirs(constants.SIMS_DATA_APPS, exist_ok=True)
            os.makedirs(constants.SIMS_DATA_APPS_DEVEL, exist_ok=True)
            os.makedirs(constants.RAYAENV_DOCKER_UR_ROOT, exist_ok=True)
            self.init_ur_root_folder()
        except OSError as error:
            log_error(error)
            return False
        except subprocess.CalledProcessError as error:
            return False
        return True


    def init_ur_root_folder(self):
        # if ur_root does not have the .git folder and have something inside
        if not os.path.exists(constants.RAYAENV_DOCKER_UR_ROOT/'.git') and len(
                os.listdir(constants.RAYAENV_DOCKER_UR_ROOT)) != 0:
            log_warning('UR user folder does not have .git folder')
            os.makedirs(f'{constants.RAYAENV_DOCKER_UR_ROOT}.old', exist_ok=True)
            command = (
                f'rsync -a {constants.RAYAENV_DOCKER_UR_ROOT}/ '
                f'{constants.RAYAENV_DOCKER_UR_ROOT}.old'
            )
            
            # delete ur_root folder
            subprocess.run(command, shell=True, check=True, capture_output=True)
            delete_command = [
                'sudo', 
                'rm', 
                '-rf', 
                constants.RAYAENV_DOCKER_UR_ROOT
            ]
            subprocess.run(delete_command, check=True)

        # if ur_root not exist or is empty clone it
        if not os.path.exists(constants.RAYAENV_DOCKER_UR_ROOT) or len(
                os.listdir(constants.RAYAENV_DOCKER_UR_ROOT)) == 0:
            log_warning('Preparing UR user folder...')
            try:
                Repo.clone_from(
                        url=constants.RAYAENV_DOCKER_UR_ROOT_REPO,
                        to_path=constants.RAYAENV_DOCKER_UR_ROOT,
                        branch=constants.RAYAENV_DOCKER_UR_ROOT_REPO_BRANCH,
                        depth=1
                )
                log_success('UR user folder created')
            except GitCommandError as e:
                log_error('Clone failed')
                log_error(f'An error occurred: {str(e)}')


        # if ur_root.old exist make a rsync to the new one
        if os.path.exists(str(constants.RAYAENV_DOCKER_UR_ROOT)+'.old'):
            log_warning('.old folder found, syncing...')
            rsync_command = [
                "rsync",
                "-av",
                str(constants.RAYAENV_DOCKER_UR_ROOT)+ '.old/',
                str(constants.RAYAENV_DOCKER_UR_ROOT)+ '/',
            ]
            subprocess.check_output(rsync_command)
            
            # delete .old folder
            subprocess.run(command, shell=True, check=True, capture_output=True)
            delete_command = [
                'sudo',
                'rm', 
                '-rf', 
                str(constants.RAYAENV_DOCKER_UR_ROOT)+ '.old/'
            ]
            subprocess.run(delete_command, check=True)
            log_warning('Sync succesfull')
            

    def init_ursdk_folder(self):
        if not os.path.exists(constants.URSDK_TEMP_PATH):
            log_verbose((
                    f'Folder {constants.URSDK_TEMP_PATH} does not exists, '
                    'creating it.'
                ))
            try:
                os.mkdir(constants.URSDK_TEMP_PATH)
            except OSError as exc:
                log_error(
                    f'Folder {constants.URSDK_TEMP_PATH} could not be created.'
                )
                return False
            return True
        else:
            log_verbose(f'Folder {constants.URSDK_TEMP_PATH} found.')
            return True


    def run(self):
        try:
            # Execute Command
            for obj in self.command_objects:
                if self.args.command == type(obj).COMMAND:
                    return obj.run(self.args, self.unknownargs)
        except Exception as e:
            log_error(str(e))
            return False


def main():
    try:
        if platform.system() not in ['Linux', 'Windows', 'Darwin']:
            log_info(f'Platform \'{platform.system()}\' not supported.')
            exit(1)
        
        ursdk = URSDK()

        if ursdk.wrong_init:
            log_verbose('Initialize with error.')
            sys.exit(1)
        
        ret = ursdk.run()
        if not ret:
            log_verbose('Finished with error.')
            sys.exit(1)
        else:
            sys.exit(0)
    except KeyboardInterrupt:
        log_info('Interrupted by user.')
        sys.exit(1)


if __name__ == "__main__":
    main()

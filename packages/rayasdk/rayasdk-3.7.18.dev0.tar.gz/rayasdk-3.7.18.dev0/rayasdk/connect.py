# Copyright 2020 Unlimited Robotics
import subprocess
import json

import rayasdk.constants as constants
from rayasdk.sshKeyGen import SshKeyGen
from rayasdk.logger import log_verbose, log_info, log_warning


class URConnect:

    COMMAND = 'connect'

    def __init__(self):
        pass


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND, help="execute current Raya project.")
        group = self.parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--robot-id',
                           help='robot identificator (from scan list)',
                           type=str)
        group.add_argument('--robot-ip',
                           help='robot ip (from scan list)',
                           type=str)
        group.add_argument('--simulator',
                           help='connect the project to the simulator',
                           action="store_true")
        group.add_argument('-s', '--show-connection',
                           help='show the current connection',
                           action="store_true")


    def show_connection(self):
        print('Current connection:')
        try:
            with open(file=constants.CONNECTION_SETTINGS_PATH,
                      mode='r',
                      encoding='utf-8') as f:
                settings = json.load(f)
                if settings[constants.JSON_EXECINFO_SIM]:
                    print('  Simulator')
                else:
                    robot_connection = settings[constants.JSON_EXECINFO_ROB_CONN]
                    print(f'  Robot ID: {robot_connection[constants.JSON_EXECINFO_ROB_ID]}')
                    print(f'  Robot IP: {robot_connection[constants.JSON_EXECINFO_ROB_IP]}')
                    print(f'  Robot Serial: {robot_connection[constants.JSON_EXECINFO_ROB_SERIAL]}')
                    print(f'  Robot Domain: {robot_connection[constants.JSON_EXECINFO_ROB_DOMAIN]}')
                    print(f'  Robot Port: {robot_connection[constants.JSON_EXECINFO_ROB_PORT]}')
                    print(f'  Robot Raya Version: {robot_connection[constants.JSON_EXECINFO_ROB_RAYA_VERSION]}')
        except FileNotFoundError:
            print('  No connection found')


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        if self.args.show_connection:
            self.show_connection()
            return True

        robot_id = self.args.robot_id
        robot_ip = self.args.robot_ip.split(':')[0] if self.args.robot_ip else ''
        robot_domain = self.args.robot_ip.split(':')[1] if self.args.robot_ip and len(self.args.robot_ip.split(':')) > 1 else '0'
        try:
            exec_settings = dict()
            exec_settings[constants.JSON_EXECINFO_SIM] = False
            exec_settings[constants.JSON_EXECINFO_ROB_CONN] = dict()
            robot_connection = exec_settings[constants.JSON_EXECINFO_ROB_CONN]
            robot_connection[constants.JSON_EXECINFO_ROB_ID] = ''
            robot_connection[constants.JSON_EXECINFO_ROB_IP] = ''

            if self.args.simulator:
                exec_settings[constants.JSON_EXECINFO_SIM] = True
                robot_connection[constants.JSON_EXECINFO_ROB_ID] = 'simulator'
                robot_connection[constants.JSON_EXECINFO_ROB_IP] = 'localhost'
                robot_connection[constants.JSON_EXECINFO_ROB_SERIAL] = 'simulator'
                robot_connection[constants.JSON_EXECINFO_ROB_DOMAIN] = '0'
                robot_connection[constants.JSON_EXECINFO_ROB_PORT] = constants.SSH_PORT
                robot_connection[constants.JSON_EXECINFO_ROB_RAYA_VERSION] = '0.0.1'
                # Send ssh key to simulation
                SshKeyGen(user=constants.SSH_USER,
                          host=robot_connection[constants.JSON_EXECINFO_ROB_IP],
                          port=robot_connection[constants.JSON_EXECINFO_ROB_PORT]
                )
                log_info(f'You have successfully connected to the simulator')
            else:
                with open(file=constants.LAST_SCANNING_PATH,
                          mode='r',
                          encoding='utf-8') as f:
                    scanned_robots = json.load(f)
                # Check if robot is in last scan
                for robot in scanned_robots:
                    scanned_robot = scanned_robots[robot]
                    
                    is_robot_id_connection = robot_id and\
                        robot_id in scanned_robot["ROBOT_ID"]

                    is_robot_ip_connection = robot_ip != '' and\
                        robot_ip in scanned_robot.get("ROBOT_IP", []) and\
                        robot_domain == scanned_robot.get("RAYA_DOMAIN", '')

                    if is_robot_id_connection or is_robot_ip_connection:
                        if constants.JSON_EXECINFO_ROB_CONN not in exec_settings:
                            robot_connection = {}

                        if robot_connection[
                                constants.JSON_EXECINFO_ROB_ID] != '':
                            raise NameError(
                                (f'\'{robot_id}\' was detected with '
                                 'multiple IP addresses, connect using the'
                                 ' \'--robot-ip\' argument instead.'))

                        robot_connection[constants.JSON_EXECINFO_ROB_ID] = \
                            scanned_robot[constants.JSON_SCAN_ID]
                        robot_connection[constants.JSON_EXECINFO_ROB_IP] = \
                            scanned_robot[constants.JSON_SCAN_IP]
                        robot_connection[constants.JSON_EXECINFO_ROB_SERIAL] = \
                            scanned_robot[constants.JSON_SCAN_SERIAL]
                        robot_connection[constants.JSON_EXECINFO_ROB_DOMAIN] = \
                            scanned_robot[constants.JSON_SCAN_DOMAIN]
                        robot_connection[constants.JSON_EXECINFO_ROB_PORT] = \
                            scanned_robot[constants.JSON_SCAN_PORT]
                        robot_connection[constants.JSON_EXECINFO_ROB_RAYA_VERSION] = \
                            scanned_robot[constants.JSON_SCAN_RAYA_VERSION]

                # If the robot was not found on the scan raise exception
                if robot_connection[constants.JSON_EXECINFO_ROB_ID] == '':
                    if robot_id:
                        raise NameError(
                            (f'Robot ID "{robot_id}" not found in scan info, '
                             'verify it or scan again.'))
                    elif robot_ip:
                        raise NameError(
                            (f'Robot IP "{robot_ip}:{robot_domain}" not found in scan info, '
                             'verify it or scan again.'))
                    else:
                        raise KeyError('')
                if robot_connection[constants.JSON_EXECINFO_ROB_RAYA_VERSION] == '0.0.0' \
                        and exec_settings[constants.JSON_EXECINFO_SIM] == False:
                    log_warning(
                        'You connected to an old version '
                        'of the RaYa discovery service, running this version '
                        'alongside newer versions may cause unexpected behavior, '
                        'such as running aplicattions on the wrong port.'
                    )

                # Send ssh key to robot
                SshKeyGen(user=constants.SSH_USER,
                          host=robot_connection[constants.JSON_EXECINFO_ROB_IP],
                          port=robot_connection[constants.JSON_EXECINFO_ROB_PORT])
                log_info(f'You have successfully connected to '
                         f'{robot_connection[constants.JSON_EXECINFO_ROB_ID]}:'
                         f'{robot_connection[constants.JSON_EXECINFO_ROB_IP]}')

            # Save connection globally
            with open(
                file=constants.CONNECTION_SETTINGS_PATH,
                mode='w',
                encoding='utf-8'
            ) as f:
                settings = dict()
                settings[constants.JSON_EXECINFO_SIM] = exec_settings[
                    constants.JSON_EXECINFO_SIM]
                settings[constants.JSON_EXECINFO_ROB_CONN] = exec_settings[
                    constants.JSON_EXECINFO_ROB_CONN]
                json.dump(settings, f, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            raise Exception((
                f'Last scan was empty or wasn\'t executed, '
                'execute \'rayasdk scan\' and check '
                'if the robot is appears in the scan.'
            ))
        except subprocess.SubprocessError:
            raise Exception("SSH Key not send, Check if raya_os is running")
        except NameError as error:
            raise Exception(str(error))
        except KeyError as error:
            log_info(error)
            raise Exception((f'Scanning info malformed, '
                             'please scan again by running "rayasdk scan".'))

        log_verbose('\nCorrect!')
        return True

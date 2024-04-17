# Copyright 2020 Unlimited Robotics

from os import system, name
import json
import select
import sys
import time
from tabulate import tabulate
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

import rayasdk.constants as constants
from rayasdk.logger import log_info

robots_info = dict()


class URScanner:
    COMMAND = 'scan'

    def __init__(self):
        pass


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND, help='Discover robots in the local network.')
        self.parser.add_argument(
            '-t','--time',
            help='Total time that execute the scan',
        )


    def __save_last_scan(self, path):
        global robots_info
        with open(path, 'w', encoding='utf-8') as f:
            all_robots = dict()
            if len(robots_info) == 0:
                json.dump(all_robots, f, ensure_ascii=False, indent=4)
                return False
            
            for robot in robots_info:
                for index, info_robot in robots_info[robot].items():
                    key = f'{index}_{robot}'
                    all_robots[key] = info_robot
            json.dump(all_robots, f, ensure_ascii=False, indent=4)
        return True


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        zeroconf = Zeroconf()
        listener = MyListener(print=True)
        ServiceBrowser(Zeroconf(), '_gary-robot._tcp.local.', listener)
        seconds_to_scan = None
        if self.args.time:
            seconds_to_scan = int(self.args.time)
        try:
            update_table()
            while True:
                if select.select([sys.stdin,], [], [], 0.0)[0]:
                    input_str = sys.stdin.readline().strip()
                    if input_str == '':
                        break

                zero = Zeroconf()
                listener = MyListener(print=False)
                browser = ServiceBrowser(
                        zc=zero,
                        type_='_gary-robot._tcp.local.',
                        listener=listener
                    )
                time.sleep(1)
                browser.cancel()
                zero.close()
                
                self.__save_last_scan(path=constants.LAST_SCANNING_PATH)
                if seconds_to_scan is not None:
                    seconds_to_scan -= 1
                    if seconds_to_scan <= 0:
                        raise KeyboardInterrupt
        except KeyboardInterrupt:
            pass
        finally:
            zeroconf.close()

        try:
            if not self.__save_last_scan(path=constants.LAST_SCANNING_PATH):
                log_info('No robots found.')
            else:
                log_info('Scan finish correctly')
        except FileNotFoundError:
            raise Exception(
                    f'Could not write file {constants.LAST_SCANNING_PATH}.'
                )
        return True


class MyListener(ServiceListener):

    def __init__(self, print=False) -> None:
        self.print = print
        super().__init__()


    def save_on_list(self, zc: Zeroconf, type_: str, name: str):
        global robots_info
        info = zc.get_service_info(type_, name)
        try:
            robots_info[name]
        except Exception:
            robots_info[name] = dict()
        try:
            for ip in info._ipv4_addresses:
                try:
                    # v2 of raya service
                    robots_info[name][str(ip)] = {
                        'ROBOT_ID': info.properties['ROBOT_ID'.encode()].decode(),
                        'ROBOT_SERIAL':
                        info.properties['ROBOT_SERIAL'.encode()].decode(),
                        'ROBOT_IP': str(ip),
                        'PORT': info.port,
                        'RAYA_DOMAIN': info.properties['RAYA_DOMAIN'.encode()].decode(),
                        'RAYA_VERSION': info.properties['RAYA_VERSION'.encode()].decode(),
                    }
                except Exception:
                    #v1 of raya service
                    robots_info[name][str(ip)] = {
                        'ROBOT_ID': info.properties['ROBOT_ID'.encode()].decode(),
                        'ROBOT_SERIAL':
                        info.properties['ROBOT_SERIAL'.encode()].decode(),
                        'ROBOT_IP': str(ip),
                        'PORT': constants.SSH_PORT,
                        'RAYA_DOMAIN': '0',
                        'RAYA_VERSION': '0.0.0',
                    }
                if self.print:
                    update_table()
        except AttributeError:
            pass


    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        self.save_on_list(zc=zc, type_=type_, name=name)


    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        self.save_on_list(zc=zc, type_=type_, name=name)


    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        global robots_info
        robots_info.pop(name, None)
        if self.print:
            update_table()


def update_table():
    global robots_info
    # Screen out all the robot found in scan
    list_robots = []
    if len(robots_info) > 0:
        clear()
        for robot in list(robots_info.items()):
            for address in list(robot[1].items()):
                list_robots.append(address[1].values())
    log_info('Press enter to exit...\n')
    log_info(
        tabulate(
            tabular_data=list_robots, 
            headers=['Robot ID', 'Serial', 'IP Address', 'Port', 'Ra-Ya Domain', 'RAYA_VERSION'],
            tablefmt='pretty'
            )
    )
    log_info('')


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

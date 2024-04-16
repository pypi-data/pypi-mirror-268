# Copyright 2020 Unlimited Robotics
import argparse

from rayasdk.logger import log_error, set_logger_level
from rayasdk.tools.FSM_creation import FSMCreator


class URTools:

    COMMAND = 'tools'

    def __init__(self):
        self.tools_objects = []
        self.tools_objects.append(FSMCreator())
    
    
    def init_children_parser(self, argparser):
        self.subparsers = argparser.add_subparsers(
                help='SDK Tool',
                dest='tool'
            )
        self.subparsers.required = True
        # Init subparsers
        for obj in self.tools_objects:
            obj.init_parser(self.subparsers)


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help="Ra-Ya SDK Tools executioner")        
        self.init_children_parser(self.parser)
        

    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        try:
            # Execute Tool
            for obj in self.tools_objects:
                if self.args.tool == type(obj).COMMAND:
                    return obj.run(self.args, self.unknownargs)
        except Exception as e:
            log_error(str(e))
            return False

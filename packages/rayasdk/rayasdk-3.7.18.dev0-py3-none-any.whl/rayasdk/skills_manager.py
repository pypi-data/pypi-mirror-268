# Copyright 2020 Unlimited Robotics
import argparse

from rayasdk.logger import log_error, set_logger_level
from rayasdk.skills.installer import SkillInstaller
from rayasdk.skills.dependencies_installer import SkillDepInstaller


class URSkillManager:

    COMMAND = 'skills'

    def __init__(self):
        self.skills_objects = []
        self.skills_objects.append(SkillInstaller())
        self.skills_objects.append(SkillDepInstaller())
    
    
    def init_children_parser(self, argparser):
        self.subparsers = argparser.add_subparsers(
                help='Raya Skills manager',
                dest='skills'
            )
        self.subparsers.required = True
        # Init subparsers
        for obj in self.skills_objects:
            obj.init_parser(self.subparsers)


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help="Ra-Ya SDK Skills manager")        
        self.init_children_parser(self.parser)
        

    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs
        try:
            # Execute skill
            for obj in self.skills_objects:
                if self.args.skills == type(obj).COMMAND:
                    return obj.run(self.args, self.unknownargs)
        except Exception as e:
            log_error(str(e))
            return False

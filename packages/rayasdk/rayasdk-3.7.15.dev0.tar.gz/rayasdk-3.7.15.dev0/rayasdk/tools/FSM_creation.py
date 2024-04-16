import os

class FSMCreator:
    COMMAND = 'fsmCreate'

    def __init__(self) -> None:
        pass

    # Private

    def __save_states(self):
        # Read the STATES array from states.pyb'
        with open('states.py', 'a') as states_file:
            states_line = ''
            for state in self.states_arr:
                states_line += f'\"{state}\",\n'
            states_file.write(f'\nSTATES = [\n{states_line}]')
            

    def __generate_actions(self):
        # Generate the functions in actions.py
        import_statement = "from raya.tools.fsm import BaseActions\n"
        import_statement += "from src.app import RayaApplication\n"
        import_statement += f"from src.FSMs.{self.FSM_NAME}.helpers import Helpers\n\n"

        class_definition = f"class Action(BaseActions):\n"
        class_definition += "\tdef __init__(self, app: RayaApplication, helpers: Helpers):\n"
        class_definition += "\t\tself.app = app\n"

        enter_leave_methods = "\n"
        for state in self.states_arr:
            state = state.strip()
            enter_leave_methods += f"\tasync def enter_{state}(self):\n\t\tpass\n\n"
            enter_leave_methods += f"\tasync def leave_{state}(self):\n\t\tpass\n"

        code = f"{import_statement}\n{class_definition}{enter_leave_methods}"

        with open('actions.py', "w") as file:
            file.write(code)
    

    def __generate_transitions(self):
        import_statements = "from raya.tools.fsm import BaseTransitions\n"
        import_statements += "from src.app import RayaApplication\n"
        import_statements += f"from src.FSMs.{self.FSM_NAME}.helpers import Helpers\n\n"

        class_definition = "class Transitions(BaseTransitions):\n\n"
        class_definition += "\tdef __init__(self, app: RayaApplication, helpers: Helpers):\n"
        class_definition += "\t\tsuper().__init__()\n"
        class_definition += "\t\tself.app = app\n"
        class_definition += "\t\tself.helpers = helpers\n"

        transitions_methods = "\n"
        for state in self.states_arr:
            state = state.strip()
            transitions_methods += f"\tasync def {state}(self):\n"
            transitions_methods += f"\t\tpass\n\n"
            
        code = f"{import_statements}\n{class_definition}{transitions_methods}"

        with open('transitions.py', 'a') as transitions_file:
            transitions_file.write(code)
        

    def __generate_helpers(self):
        import_statements = "from raya.exceptions import *\n"
        import_statements += "from src.app import RayaApplication\n\n"

        class_definition = "class Helpers:\n"
        class_definition += "\tdef __init__(self, app: RayaApplication):\n"
        class_definition += "\t\tself.app = app\n"
        class_definition += "\t\tself.last_ui_result = None\n\n"

        code = f"{import_statements}\n{class_definition}"

        with open('helpers.py', 'a') as helper_file:
            helper_file.write(code)
            
    
    def __create_FMSs_parent_folder(self):
        parent_folder = 'src/FSMs'
        os.makedirs(parent_folder, exist_ok=True)
        os.chdir(parent_folder)
        with open('__init__.py', 'w'):
            pass 


    def __create_FMSs_folder(self):
        os.makedirs(self.FSM_NAME)
        os.chdir(self.FSM_NAME)
        with open('__init__.py', 'w'):
                pass 
    
    # Public
    
    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND, help="Creation tool for FSM")
        self.parser.add_argument(
            '-s',
            '--states',
            nargs='+',
            help='States ex: --states State1 State2 State3',
            required=True
        )

    
    def run(self, args, unknownargs) -> None:
        print(args)
        self.states_arr = args.states
        self.FSM_NAME = input("Enter the FSM name: ")
        
        self.__create_FMSs_parent_folder()
        self.__create_FMSs_folder()
        self.__save_states()
        self.__generate_actions()
        self.__generate_transitions()
        self.__generate_helpers()
        print("Files generated successfully.")
    
from enum import Enum

verbose = False
quiet = False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class colors:
    # Regular Colors
    Black = '\033[0;30m'  # Black
    Red = '\033[0;31m'  # Red
    Green = '\033[0;32m'  # Green
    Yellow = '\033[0;33m'  # Yellow
    Blue = '\033[0;34m'  # Blue
    Purple = '\033[0;35m'  # Purple
    Cyan = '\033[0;36m'  # Cyan
    White = '\033[0;37m'  # White

    # Bold
    BBlack = '\033[1;30m'  # Black
    BRed = '\033[1;31m'  # Red
    BGreen = '\033[1;32m'  # Green
    BYellow = '\033[1;33m'  # Yellow
    BBlue = '\033[1;34m'  # Blue
    BPurple = '\033[1;35m'  # Purple
    BCyan = '\033[1;36m'  # Cyan
    BWhite = '\033[1;37m'  # White

    # Underline
    UBlack = '\033[4;30m'  # Black
    URed = '\033[4;31m'  # Red
    UGreen = '\033[4;32m'  # Green
    UYellow = '\033[4;33m'  # Yellow
    UBlue = '\033[4;34m'  # Blue
    UPurple = '\033[4;35m'  # Purple
    UCyan = '\033[4;36m'  # Cyan
    UWhite = '\033[4;37m'  # White

    # Background
    On_Black = '\033[40m'  # Black
    On_Red = '\033[41m'  # Red
    On_Green = '\033[42m'  # Green
    On_Yellow = '\033[43m'  # Yellow
    On_Blue = '\033[44m'  # Blue
    On_Purple = '\033[45m'  # Purple
    On_Cyan = '\033[46m'  # Cyan
    On_White = '\033[47m'  # White

    # High Intensity
    IBlack = '\033[0;90m'  # Black
    IRed = '\033[0;91m'  # Red
    IGreen = '\033[0;92m'  # Green
    IYellow = '\033[0;93m'  # Yellow
    IBlue = '\033[0;94m'  # Blue
    IPurple = '\033[0;95m'  # Purple
    ICyan = '\033[0;96m'  # Cyan
    IWhite = '\033[0;97m'  # White

    # Bold High Intensity
    BIBlack = '\033[1;90m'  # Black
    BIRed = '\033[1;91m'  # Red
    BIGreen = '\033[1;92m'  # Green
    BIYellow = '\033[1;93m'  # Yellow
    BIBlue = '\033[1;94m'  # Blue
    BIPurple = '\033[1;95m'  # Purple
    BICyan = '\033[1;96m'  # Cyan
    BIWhite = '\033[1;97m'  # White

    # High Intensity backgrounds
    On_IBlack = '\033[0;100m'  # Black
    On_IRed = '\033[0;101m'  # Red
    On_IGreen = '\033[0;102m'  # Green
    On_IYellow = '\033[0;103m'  # Yellow
    On_IBlue = '\033[0;104m'  # Blue
    On_IPurple = '\033[0;105m'  # Purple
    On_ICyan = '\033[0;106m'  # Cyan
    On_IWhite = '\033[0;107m'  # White


class LogLevels(Enum):
    VERBOSE = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    SUCCESS = 5
    STATUS = 6


def set_logger_level(_verbose, _quiet):
    global verbose, quiet
    verbose = _verbose
    quiet = _quiet


def log(level, msg, end='\n', flush=False):
    if level == LogLevels.INFO or (level == LogLevels.VERBOSE and verbose):
        if not quiet:
            print(msg, end=end, flush=flush)
    elif level == LogLevels.ERROR:
        print(msg, end=end, flush=flush)
    elif level == LogLevels.WARNING:
        print(msg, end=end, flush=flush)
    elif level == LogLevels.SUCCESS:
        print(msg, end=end, flush=flush)
    elif level == LogLevels.STATUS:
        print(msg, end=end, flush=flush)


def log_verbose(msg, end='\n', flush=False):
    log(LogLevels.VERBOSE, msg, end=end, flush=flush)


def log_info(msg, end='\n', flush=False):
    log(LogLevels.INFO, msg, end=end, flush=flush)


def log_warning(msg, end='\n', flush=False):
    log(LogLevels.WARNING,
        f'{bcolors.WARNING}WARNING:{bcolors.ENDC} {msg}',
        end=end,
        flush=flush)


def log_error(msg, end='\n', flush=False):
    log(LogLevels.ERROR,
        f'{bcolors.FAIL}ERROR:{bcolors.ENDC} {msg}',
        end=end,
        flush=flush)


def log_success(msg, end='\n', flush=False):
    log(LogLevels.SUCCESS,
        f'{bcolors.OKGREEN}SUCCESS:{bcolors.ENDC} {msg}',
        end=end,
        flush=flush)


def log_status(msg, end='\n', flush=False):
    log(LogLevels.STATUS,
        f'{colors.IGreen}{msg}{bcolors.ENDC}',
        end=end,
        flush=flush)
    # for color_code in vars(colors).values():
    #     log(LogLevels.INFO,
    #         f'{color_code}{msg}{bcolors.ENDC}',
    #         end=end,
    #         flush=flush)

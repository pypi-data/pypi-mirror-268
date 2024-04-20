MSG_DOCKER_NOT_INSTALLER = (
    'Docker is not installed or the current user doesn\'t have permissions'
    ' to run it. \n'
    'If you have Docker installed, run it and then run this script again.\n'
    'If you do not have Docker, visit Ra-Ya documentation to install it.')

MSG_DOCKER_NOT_RUNNING = (
    'Please verify that Docker Desktop is running. '
    'You just need to search for the application and open it.')

MSG_DOCKER_LOCAL_FEATS_DISABLED = (
    'The local features that involve docker are disabled, '
    'in order to use it install or run docker.'
)

MSG_DOCKER_CONTAINER_NOT_RUNNING = (
    'Please verify that RAYA_OS is running on the robot.'
)

MSG_FULL_UPDATE = (
    '\nWe have a new version of RayaOS available\n'
    'Would you like to update?[Y/n]\n'
)

MSG_MINOR_UPDATE = (
    f'\nRayaOS found a minor version change\n'
    'Would you like to update?[Y/n]\n'
)

MSG_NO_UPDATES = ('It seems there are no updates available\n')

MSG_NO_VCS = ('Could get VCS')

# runner
MSG_LAUNCHING_APP = ('Launching app...')

MSG_SYNC_APP_SIM = ('Syncing the app on the simulation...')

MSG_SYNC_APP_ROBOT = ('Syncing the app on the host')

MSG_SYNC_APP_SUCCESS = ('App sync succesfully')

MSG_WAIT_DEBUG_CLIENT = ('Waiting for debug client (VSCode)...')

MSG_APP_FINISHED = ('App finished')

# simulator
MSG_RAYA_OS_IMAGE = ('Opening RayaOS image...')

MSG_UNITY_SIM = ('Opening Raya unity simulator...')

# custom command
MSG_SCRIPT_RUNNING = ('Executing command on')

# run
MSG_FOLDER_NOT_FOUND = ('The folder does not exist')

MSG_FOLDER_NOT_RAYA_APP = ('The folder is not a Raya app')

# X11 messages
MSG_X11_NOT_RUNNING = (
    'X11 server is not running, '
    'the grafical interface of the app will be displayed on the robot.'
)

MSG_X11_NOT_RUNNING_LINUX = (
    'X11 server is not running, ensure that you have installed X11 server.'
)

MSG_X11_MAC_OS_RECOMMENDATION = (
    'We recommend to install XQuartz to run the graphical interface of the app'
)
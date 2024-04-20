# Documentation

# Usage

```bash
rayasdk [-h] [-v | -q] command {command-options}
```

Optional arguments:

- `h` `--help`: show this help message and exit.
- `v` `--verbose`: increase output verbosity.
- `q` `--quiet`: don't print on stdout.

Positional arguments:

- `command`: SDK Command

Commands:

- [`simulator`](https://www.notion.so/simulator-b4e672e9171a4a8fa10ec6ce52820a60) : Runs the simulator and the Raya os image
- [`init`](https://www.notion.so/init-982ee5d195dd41558b8846a792791372) : Initialize Raya project in the current folder.
- [`scan`](https://www.notion.so/scan-e79f54c3a0b748b0944699cb89340c0b) : Discover robots in the network.
- [`connect`](https://www.notion.so/connect-28e716904b9e4ef8939ebdf72141a1b1) : Connect raya to a robot or simulator.
- [`run`](https://www.notion.so/run-6ad438cd37a0496cb84153cb5199147b) : Execute current Raya project.
- [`update`](https://www.notion.so/update-1beba97f488b45f894b0b3ac9a714388) : Updates the Raya simulator.
- [`kill`](https://www.notion.so/kill-b4f7a26695ba4c5f80baf4ae7907808b) : Kill all Ra-Ya apps that are executed.

Developer notes: [Notes](https://www.notion.so/Notes-df05362c32244e6b83bc6504160a76ef) 

# `simulator`

Runs the unity simulator

Usage:

```bash
rayasdk simulator [-d] [-h] {simulation-flags}
```

Optional arguments:

- `--help`: Show this help message and exit
- `--debug`: Runs only the unity simulator

Example:

```bash
rayasdk simulator
```

# `init`

Initialize Raya project in the current folder.

Usage:

```bash
rayasdk init [-h] --app-id APP_ID [--app-name APP_NAME]
```

Required arguments:

- `--app-id APP_ID`: Application unique identificator (It has to be in snake_case format)

Optional arguments:

- `--app-name APP_NAME`: Application name
- `h` `--help`: Show this help message and exit

Example:

```bash
rayasdk init --app-id helloworld --app-name 'Hello World'
```

# `scan`

Discover robots in the local network

Usage: 

```bash
rayasdk scan [-h]
```

Optional arguments:

- `h` `--help`: Show this help message and exit

Example:

```bash
rayasdk scan
```

Output:

```bash
# rayasdk scan
Press enter to exit...

Robot ID         Serial           IP Address
---------------  ---------------  --------------
GARY_COLOMBIA    GARY_COLOMBIA    192.168.20.55
GARY_COLOMBIA_1  GARY_COLOMBIA_1  172.25.188.155
```

# `connect`

Connect the current Raya project to a robot or simulator. The connection settings are global and are stored in ~/.ur/connection.json

Usage:

```bash
rayasdk connect [-h] [--robot-id ROBOT_ID | --robot-ip ROBOT_IP | --simulator]
```

Required mutually exclusive arguments:

- `--robot-id ROBOT_ID`: Robot identificator (from scan list).
- `--robot-ip ROBOT_IP`: Robot ip (from scan list or if you know it).
- `--simulator`: Connect the project to the simulator.

Optional arguments:

- `h` `--help`: Show this help message and exit

Example:

Connection to robot

```bash
rayasdk connect --robot-ip 192.168.20.55
```

Output:

```bash
# rayasdk connect --robot-ip 192.168.20.55
RayaOS is not up to date, if you wish to update, please run "rayasdk update"
SSH key found. Pushing key to remote server
The authenticity of host '[192.168.20.55]:2222 ([192.168.20.55]:2222)' can't be established.
ED25519 key fingerprint is ...
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/home/ur-sb/.local/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed

/home/ur-sb/.local/bin/ssh-copy-id: WARNING: All keys were skipped because they already exist on the remote system.
		(if you think this is a mistake, you may want to use -f option)

You have successfully connected to GARY_COLOMBIA
```

Connection to simulator

```bash
rayasdk connect --simulator
```

```bash
# rayasdk connect --simulator
You have successfully connected to the simulator
```

# `update`

Check for a partial or full download of the Ra-ya Simulator and the Raya-os Image, This will create the following structure in `~/.ur`

```
~/.ur
├── simulator
	└── raya_simulator_1.0.4_linux
			└── ...
└── versions.txt
```

Usage:

```bash
rayasdk update [-h]
```

Optional arguments:

- `h` `--help`: Show this help message and exit

Example

```bash
rayasdk update
```

Output

```bash
# rayasdk update
Checking for updates...
Checking for full update...
...
Downloading Ra-Ya simulator v1.0.4...
...
Extracting...
Simulator updated successfully
Removing old Ra-Ya containers and images...
Docker image 'raya_os:1.0.10' not found.
Downloading Ra-Ya OS v1.0.10 (only once)...
Copying gs://raya_files/Common/TestingVCS/raya_os_1.0.10.zip...
- [1/1 files][  1.8 GiB/  1.8 GiB] 100% Done   3.8 MiB/s ETA 00:00:00           
Operation completed over 1 objects/1.8 GiB.                                      
Extracting Ra-Ya OS image.
Creating image...
...
Loaded image: unlimited_robotics/raya_os/gary_unity:1.0.10
Update completed successfully.
```

# `run`

Execute the current Raya project according to the connection settings.

Usage:

```bash
rayasdk run [-d]
```

Optional arguments:

- `--debug`: Wait for the vscode client for debug purposes.

Example

```bash
rayasdk run
```

# `kill`

Kill all Ra-Ya apps that are executed by the user rayadevel.

Usage:

```bash
rayasdk kill [-h]
```

Optional arguments:

- `h` `--help`: Show this help message and exit

Example

```bash
rayasdk run
```

# Notes

- The credentials if you want to connect over ssh to the robot using the rayadevel user are 
USER: rayadevel 
Password: gary 
Port:2222
- The app is deleted when the container is closed, the route for the apps that are being runned is /opt/raya_os/rayadevel/apps/{APP_ID}
- In the simulator the .ur/simulator/apps folder gets mounted, if this folder is deleted the container will not use it, so if you try to run an app it is going to fail, close the container, run any command in the sdk and run the bringup again
- In your home folder there is going to be a folder called .ur that contains two files and a file that saves the current robot that is going to be used in the run option and a folder with the simulator and the apps that are used in the simulation.
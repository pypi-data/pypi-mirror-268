import platform
import docker
import subprocess
import os

import rayasdk.constants as constants
from rayasdk.messages import *
from rayasdk.logger import log_info, log_error, log_error, log_warning

_docker_running_locally = True

class DockerHandler():

    def __init__(self):
        global _docker_running_locally
        self.raya_imgs = {}
        self.docker_client: docker.DockerClient = None
        self.RAYAENV_DOCKER_VERSION = constants.RAYAENV_DOCKER_VERSION_DEFAULT
        self.RAYAENV_DOCKER_IMAGE_NAME = None
        self.docker_running_locally = _docker_running_locally
        try:
            if not self.docker_running_locally:
                return
            self.check_docker_instalation()
            self.check_if_gpu()
            self.docker_image_version()
        except Exception as e:
            log_warning(e)
            log_warning(MSG_DOCKER_LOCAL_FEATS_DISABLED)
            _docker_running_locally = False


    # Private methods


    def __remove_old_images(self, latest_version: str):
        log_info(('Removing old Ra-Ya images ...'))
        for image in self.docker_client.images.list(all=True):
            if image.tags and self.RAYAENV_DOCKER_IMAGE_NAME not in ":".join(
                    image.tags):
                continue
            if any(
                    item.startswith(self.RAYAENV_DOCKER_IMAGE_NAME)
                    for item in image.tags):
                # if the latest image exist do not delete it
                if any(
                        str(item) ==
                        f'{self.RAYAENV_DOCKER_IMAGE_NAME}:{latest_version}'
                        for item in image.tags):
                    continue
                remove_old_image = input(
                        ('Found a old raya image with the tags:\n'
                        f'{image.tags}\n'
                        'Would you like to delete it?[y/N]\n')
                    )
                if remove_old_image in ['y', 'Y', 'yes', 'Yes', 'YES']:
                    self.docker_client.images.remove(image.id, force=True)
                    log_info((f'\'{image.tags[0]}\' Image removed'))


    def __download_image(self, version: str):
        if self.check_image(version=version):
            log_info(
                    ('The Ra-Ya OS image already exist: '
                    f'{self.RAYAENV_DOCKER_IMAGE_NAME}:{version}')
                )
            return True

        log_info(f'Downloading Ra-Ya OS v{version} (only once)...')
        image_name = f'{self.RAYAENV_DOCKER_IMAGE_NAME}:{version}'
        try:
            if os.system(f'docker pull {image_name}') != 0:
                raise KeyboardInterrupt('')
        except KeyboardInterrupt:
            log_error('Failed to download Ra-Ya OS image. Please try again.')
            return False
        return True


    def __check_docker_locally(func):
        def wrapper(self, *arg, **kw):
            global _docker_running_locally
            if _docker_running_locally:
                return func(self, *arg, **kw)
            else:
                raise Exception(MSG_DOCKER_LOCAL_FEATS_DISABLED)
        return wrapper
        

    # Public methods


    def check_docker_instalation(self):
        # Check docker installation
        try:
            self.docker_client = docker.from_env()
        except docker.errors.DockerException:
            # maybe required for MAC as well:
            if platform.system() == 'Windows' or platform.system() == 'Darwin':
                raise Exception(MSG_DOCKER_NOT_RUNNING)
            else:
                raise Exception(MSG_DOCKER_NOT_INSTALLER)
        return True


    def check_if_gpu(self):
        return_code = subprocess.call(
            'docker info | grep "Runtimes:" | grep "nvidia"',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        if return_code != 0:
            img_gpu = constants.RAYAENV_DOCKER_IMG_VERSION_NAME
        else:
            img_gpu = constants.RAYAENV_DOCKER_IMG_VERSION_GPU
        self.RAYAENV_DOCKER_IMAGE_NAME = (
            f'unlimitedrobotics/'
            f'{constants.RAYAENV_DOCKER_IMGNAME}.{img_gpu}.prod')


    def docker_image_version(self):
        # Docker image version
        self.check_docker_instalation()
        images = list()
        for image in self.docker_client.images.list(all=True):
            for subtag in image.tags:
                if subtag.startswith(self.RAYAENV_DOCKER_IMAGE_NAME):
                    try:
                        images.append(subtag.split(':')[1])
                    except:
                        pass
        images.sort()

        if images:
            self.RAYAENV_DOCKER_VERSION = images[-1]
        return images


    def download_raya_image(self, version: str):
        self.__remove_old_images(version)
        if not self.__download_image(version=version):
            return False
        return True


    def check_image(self, version: str = None):
        if version is None:
            version = self.RAYAENV_DOCKER_VERSION

        for image in self.docker_client.images.list(all=True):
            if image.tags and self.RAYAENV_DOCKER_IMAGE_NAME not in ":".join(
                    image.tags):
                continue
            if f'{self.RAYAENV_DOCKER_IMAGE_NAME}:{version}' in image.tags:
                return True
        return False


    def RayaOS_not_found(self):
        return not self.check_image()


    @__check_docker_locally
    def launch_container(self, output_file='', silent=False, version=None):
        # Check if ur root folder exist
        if not os.path.exists(constants.RAYAENV_DOCKER_UR_ROOT) or len(
                os.listdir(constants.RAYAENV_DOCKER_UR_ROOT)) == 0:
            log_error(
                f'\'{constants.RAYAENV_DOCKER_UR_ROOT}\' files does not exist')
            return False
        
        #Check if container is already running
        container_name = self.check_running_container()
        if container_name is not False:
            log_error(
                'There is already a RayaOS container called: '
                f'\'{container_name}\''
            )
            return False
        
        # if version is defined check if is valid
        if version is not None and version != 'latest':
            image_versions = self.docker_image_version()
            if version in image_versions:
                self.RAYAENV_DOCKER_VERSION = version
            else:
                log_error(f'\'{version}\' is not a valid Ra-Ya OS version')
                log_warning(f'Available: {image_versions}')
                return False
        
        command = (
                f'cd {constants.RAYAENV_DOCKER_UR_ROOT}/scripts && '
                f'./run.container.sh {self.RAYAENV_DOCKER_VERSION}'
            )
        docker_command = f'{command} '
        if silent:
            if output_file:
                docker_command += f'> {str(output_file)}'
            else:
                docker_command += f'> /dev/null'
        else:
            if output_file:
                docker_command += f'| tee {str(output_file)}'
        return subprocess.Popen(docker_command, shell=True)


    @__check_docker_locally
    def kill_apps(self):
        container_name = self.check_running_container()
        if container_name is False:
            raise Exception('The RayaOS container is not running.')
        log_info(f'Killing all running apps...')
        command = 'pkill -9 -u rayadevel'
        docker_command = (f'docker exec -it {container_name} {command}')
        subprocess.call(docker_command, shell=True)


    @__check_docker_locally
    def check_running_container(self):
        # Check running container
        container_name = None
        container_dev_name = None

        for container in self.docker_client.containers.list(all=True):
            if str(container.name).startswith(
                    constants.RAYAENV_DOCKER_IMGNAME
                ):
                container_name = container.name
            elif container.name == constants.RAYAENV_DOCKER_IMGNAME_DEV:
                container_dev_name = container.name

        if container_name is None and container_dev_name is None:
            return False
        elif container_name is not None and container_dev_name is not None:
            raise Exception('Dev and Release container are running, stop one.')

        if container_name:
            return container_name
        elif container_dev_name:
            return container_dev_name
        else:
            return False

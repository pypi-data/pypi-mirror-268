from setuptools import setup, find_packages
import re

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
def get_lib_version():
    VERSIONFILE='rayasdk/_version.py'
    verstrline = open(VERSIONFILE, "rt").read()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
    return verstr

setup(
    name='rayasdk',
    packages=find_packages(),
    version=get_lib_version(),
    license='MIT',
    description='Raya SDK - Unlimited Robotics Software Development Kit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Unlimited Robotics',
    author_email='camilo@unlimited-robotics.com',
    url='',
    python_requires=">=3.8",
    download_url='',
    package_data={'': ['./template/*']},
    keywords=['robotics', 'unlimited-robotics', 'gary'],
    install_requires=[
        'raya',
        'tabulate', 
        'importlib_metadata', 
        'tqdm', 
        'docker', 
        'progressbar',
        'simple_file_checksum', 
        'gsutil', 
        'zeroconf', 
        'paramiko',
        'psutil',
        'GitPython'
    ],
    entry_points={
        'console_scripts': [
            'rayasdk = rayasdk.__main__:main',
        ],
    },
)

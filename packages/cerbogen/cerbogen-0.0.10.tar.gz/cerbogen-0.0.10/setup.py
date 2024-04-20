from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

# Custom installation class to run setup.py after installation
class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.call(['python', '-m', 'cerbogen.setup'])

setup(
    name='cerbogen',
    version = '0.0.10',
    description='A Python package for CerboTech',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Clarence Parmar',
    author_email='git.clarence@gmail.com',
    url='https://github.com/clarenceparmar/cerbogen',
    packages=find_packages(),
    package_data={'': ['ffmpeg/*']},
    install_requires=[
        "matplotlib", "pydub", "numpy", "wave", "librosa", "pywin32"
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    cmdclass={
        'install': PostInstallCommand,
    }
)
